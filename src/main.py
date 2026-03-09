import json
import google.generativeai as genai

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

