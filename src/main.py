import json
import requests
import os

# 🔐 Get API key safely
API_KEY = os.getenv("GEMINI_API_KEY")

# ❗ If not set, fallback (you can temporarily paste key here)
if not API_KEY:
    API_KEY = "PASTE_YOUR_NEW_KEY_HERE"

# 📂 Load IoT data
with open("iot_data.json", "r") as file:
    data = json.load(file)

print("\n📊 Data Loaded\n")

# 🌐 Gemini API URL
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 🧠 Function to call Gemini
def ask_gemini(prompt):
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Error in response. Check API key or request."

# 📝 Daily Summary
summary_prompt = f"""
You are an AI care assistant.

Summarize this activity in simple terms.
Do NOT give medical advice.

Data:
{data}
"""

summary = ask_gemini(summary_prompt)

print("📝 Daily Summary:")
print(summary)

# ⚠️ Alert detection
alert = any(entry["activity"] == "no_movement" for entry in data)

if alert:
    print("\n⚠️ Alert: No movement detected!")
else:
    print("\n✅ Activity looks normal")

# 💬 Interactive assistant
while True:
    user_query = input("\n💬 Ask something (type 'exit' to quit): ")

    if user_query.lower() == "exit":
        print("👋 Exiting")
        break

    prompt = f"""
    You are a helpful care assistant.

    Rules:
    - No medical diagnosis
    - Keep answers simple

    Data:
    {data}

    Question:
    {user_query}
    """

    answer = ask_gemini(prompt)
    print("\n🤖", answer)
