import google.generativeai as genai

# Add your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")


# Example IoT activity data
iot_data = """
8:00 AM - User woke up
8:30 AM - Breakfast activity detected
9:00 AM - No movement detected
10:00 AM - No movement detected
11:00 AM - No movement detected
"""

prompt = f"""
You are an intelligent care assistant.

Analyze this IoT activity log and detect if something unusual
happened or if the user may need assistance.

Activity Log:
{iot_data}

Respond with a short alert if necessary.
"""

response = model.generate_content(prompt)

print("AI Alert:")
print(response.text)
