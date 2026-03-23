import google.generativeai as genai

genai.configure(api_key="AIzaSyCCBpObDpncoozfjGag2iO_D2ZwUIzCQ_g")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Say hello")

print(response.text)
