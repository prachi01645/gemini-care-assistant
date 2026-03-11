import json
import streamlit as st
import pandas as pd
from google import genai

# Gemini API
client = genai.Client(api_key="GEMINI_API_KEY")

st.set_page_config(page_title="IoT Care Assistant", layout="wide")

st.title("AI-Powered IoT Care Assistant")

# Load IoT data
with open("data/iot_data.json", "r") as file:
    data = json.load(file)

activities = data["activity_log"]

# Convert to DataFrame
df = pd.DataFrame(activities)

# Layout with two columns
col1, col2 = st.columns(2)

# -----------------------
# LEFT SIDE – Activity Data
# -----------------------
with col1:

    st.subheader("Activity Log")

    st.dataframe(df)

    df["movement_flag"] = df["activity"].apply(
        lambda x: 0 if x == "no_movement" else 1
    )

    st.subheader("Movement Timeline")

    st.line_chart(df["movement_flag"])


# -----------------------
# RIGHT SIDE – Activity Stats
# -----------------------
with col2:

    st.subheader("Activity Distribution")

    activity_counts = df["activity"].value_counts()

    st.bar_chart(activity_counts)

    st.subheader("Activity Breakdown")

    st.write(activity_counts)


# -----------------------
# Pattern Detection
# -----------------------

no_movement_count = 0
alert = None
reason = ""
confidence = 0

for entry in activities:

    if entry["activity"] == "no_movement":
        no_movement_count += 1
    else:
        no_movement_count = 0

    if no_movement_count >= 3:

        alert = "Possible prolonged inactivity detected"
        reason = "Three consecutive no_movement signals"
        confidence = 85
        break

if alert is None:

    alert = "Normal activity pattern detected"
    reason = "Movement signals are within normal range"
    confidence = 95


st.subheader("System Alert")

st.write("Alert:", alert)
st.write("Reason:", reason)
st.write("Confidence:", str(confidence) + "%")


# -----------------------
# Role Selection
# -----------------------

role = st.selectbox(
    "Select User Role",
    ["caregiver", "family", "supervisor"]
)


if st.button("Generate AI Explanation"):

    prompt = f"""
    You are an intelligent elderly care assistant.

    Activity Data:
    {activities}

    Alert:
    {alert}

    Reason:
    {reason}

    Confidence:
    {confidence}%

    User Role:
    {role}

    Explain the situation clearly.
    Do not provide medical diagnosis.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    explanation = response.text

    st.subheader("AI Explanation")

    st.write(explanation)


    # Download report button
    report = f"""
    ALERT REPORT

    Alert: {alert}
    Reason: {reason}
    Confidence: {confidence}%

    AI Explanation:
    {explanation}
    """

    st.download_button(
        label="Download Report",
        data=report,
        file_name="iot_care_report.txt",
        mime="text/plain"
    )
