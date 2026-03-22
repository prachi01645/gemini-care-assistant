import json
import os
from google import genai

# Create Gemini client
client = genai.Client(api_key=os.getenv("AIzaSyAUi_KEvhdx1H01a6T3JYRqiXsUBDf3JZY"))

# Load IoT data
with open("data/iot_data.json", "r") as file:
    iot_data = json.load(file)

print("IoT Data Loaded:", iot_data)

prompt = f"""
You are a healthcare AI assistant.

Patient IoT Data:
{iot_data}

Analyze the data and give simple health advice.
"""

# Generate AI response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n--- Gemini Care Assistant ---")
print(response.text)
