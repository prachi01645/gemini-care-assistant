import google.generativeai as genai

genai.configure(api_key="PASTE_YOUR_NEW_KEY_HERE")

model = genai.GenerativeModel("models/text-bison-001")

response = model.generate_content("Say hello")

print(response.text)
