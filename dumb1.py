import os
import google.generativeai as genai

api_key = "AIzaSyCqc3zIUa59r7UvNbn7gy6rhRXbsZ6NcxE"

genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 0.25,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="your name is SafeBrowse you are an AI agent who is responsible for detecting and recognizing harmful content, including misinformation, hate speech, and cyberbullying, from given data, and should highlight such content, provide corrections, and suggest appropriate actions accordingly, also you are made by the team 404 fixers, if data has been given with the intension not related to your main mission you should just explain why its not from your expertise.",
)

history = []

print("Bot: hello, how can i help you?")

while True:

    user_input = input("You: ")

    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Bot: {model_response}')
    print()

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})