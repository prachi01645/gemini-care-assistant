import json
import os
import google.generativeai as genai

# 🔑 Setup Gemini API
genai.configure(api_key="AIzaSyAUi_KEvhdx1H01a6T3JYRqiXsUBDf3JZY")

# 📂 Load IoT data
with open("iot_data.json", "r") as file:
    data = json.load(file)

print("\n📊 IoT Activity Data Loaded Successfully!\n")

# 🧠 STEP 1: Daily Summary
summary_prompt = f"""
You are an AI care assistant.

Summarize the user's daily activity in simple and clear language.

Rules:
- Do NOT give medical advice
- Keep it short and easy
- Mention if activity is normal or unusual

Data:
{data}
"""

summary_response = model.generate_content(summary_prompt)
summary_text = summary_response.text

print("📝 Daily Summary:")
print(summary_text)

# ⚠️ STEP 2: Simple Alert Detection
alert = False

for entry in data:
    if entry["activity"] == "no_movement":
        alert = True

if alert:
    print("\n⚠️ Alert: No activity detected for a long period. Please check.")
else:
    print("\n✅ Status: Activity looks normal.")

# 💬 STEP 3: Ask Assistant (INTERACTIVE PART)
while True:
    user_query = input("\n💬 Ask something about activity (or type 'exit'): ")

    if user_query.lower() == "exit":
        print("👋 Exiting assistant. Stay safe!")
        break

    prompt = f"""
    You are a helpful AI care assistant.

    Rules:
    - Do NOT give medical diagnosis
    - If unsure, suggest contacting a caregiver
    - Keep answers simple and clear

    IoT Data:
    {data}

    User Question:
    {user_query}
    """

    response = model.generate_content(prompt)
    print("\n🤖 Assistant:", response.text)
