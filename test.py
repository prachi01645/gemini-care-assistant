import google.generativeai as genai

genai.configure(api_key="AIzaSyBfyZbzOj5sRHW1vevYSR_aTRGWDp3o6C0")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Say hello")

print(response.text) 
