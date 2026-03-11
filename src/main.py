import json
import google.generativeai as genai


# --------------------------------
# Configure Gemini API
# --------------------------------
genai.configure(api_key="GEMINI_API_KEY")

# --------------------------------
# Load IoT Data
# --------------------------------
with open("data/iot_data.json", "r") as file:
    data = json.load(file)

print("\nIoT Data Loaded:")
print(data)

activities = data["activity_log"]

# --------------------------------
# Pattern Detection Layer
# --------------------------------
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
        alert = "Possible prolonged inactivity detected."
        reason = "3 consecutive 'no_movement' signals detected in IoT activity log."
        confidence = 85
        break

if alert is None:
    alert = "No abnormal behaviour detected."
    reason = "Normal activity patterns observed."
    confidence = 95

print("\nSystem Alert:", alert)
print("Reason:", reason)
print("Confidence Score:", str(confidence) + "%")

# --------------------------------
# Role Selection
# --------------------------------
role = input("\nEnter role (caregiver / family / supervisor): ")

if role == "caregiver":
    role_instruction = "Provide clear caregiving advice and next steps."

elif role == "family":
    role_instruction = "Explain the situation simply and calmly without causing worry."

elif role == "supervisor":
    role_instruction = "Provide a detailed analysis of the detected pattern."

else:
    role_instruction = "Explain the situation clearly."

# --------------------------------
# AI Prompt
# --------------------------------
prompt = f"""
You are an intelligent elderly care assistant.

IoT Activity Data:
{activities}

Detected Alert:
{alert}

Reason:
{reason}

Confidence Score:
{confidence}%

User Role:
{role}

Instructions:
{role_instruction}

Explain the situation clearly.
Do not provide medical diagnosis.
Focus only on interpreting the activity data and suggesting safe actions.
"""

# --------------------------------
# Gemini AI Model
# --------------------------------
model = genai.GenerativeModel("models/gemini-flash-latest")

response = model.generate_content(prompt)

# --------------------------------
# Output
# --------------------------------
print("\n--- AI Care Assistant Explanation ---")
print(response.text)

# Configure Gemini API
genai.configure(api_key="AIzaSyDRfG1RVkxV6PPaY8zS3EUk4S1BDlHh8gk")

# Load IoT health data
with open("data/iot_data.json", "r") as file:
    iot_data = json.load(file)

print("IoT Data Loaded:")
print(iot_data)

# Create prompt for Gemini
prompt = f"""
You are a healthcare assistant.

Patient IoT health data:
{iot_data}

Analyze the data and give simple health advice.
"""

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(prompt)

print("\n----- Gemini Health Advice -----")
print(response.text)


