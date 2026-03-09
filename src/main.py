import json
import google.generativeai as genai

# Configure Gemini API
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

# Load IoT data
with open("data/iot_data.json", "r") as file:
    iot_data = json.load(file)

# Create prompt for Gemini
prompt = f"""
You are a healthcare AI assistant.

Here is patient IoT health data:
{iot_data}

Analyze the data and give simple health advice.
"""

# Use Gemini model
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(prompt)

print("----- Gemini Care Assistant -----")
print(response.text)
