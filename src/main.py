import google.generativeai as genai
import json

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")
 
# Load IoT data from JSON
with with open("data/iot_data.json") as file:
    data = json.load(file)

activity_log = data["activity_log"]

prompt = f"""
You are an intelligent care assistant.

Analyze the following activity log and detect unusual patterns.

Activity Log:
{activity_log}

Explain if an alert should be triggered.
"""

response = model.generate_content(prompt)

print("AI Alert:")
print(response.text)
