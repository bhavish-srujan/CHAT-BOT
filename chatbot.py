import os
from google import genai
from google.genai import types

# 1. Initialize the client. It automatically picks up the GEMINI_API_KEY environment variable.
client = genai.Client()

print("🤖 AI Chatbot Initialized! Type 'exit' or 'quit' to end the conversation.\n")

# 2. Initialize a stateful chat session with your system instruction
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="""
        You are a playful and flirty guy.
        Be charming, confident, witty, and teasing.
        Keep the flirting light and fun.
        Use occasional playful compliments and emojis.
        Do not be overly sexual or explicit.
        Keep responses natural and conversational.
        """
    )
)

while True:
    # 3. Get input from the user
    user_input = input("You: ")
    
    # 4. Check for exit conditions
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break
        
    if not user_input.strip():
        continue

    try:
        # 5. Send message to the chat session (it manages history automatically)
        response = chat.send_message(user_input)
        
        # 6. Extract and print the bot's reply
        print(f"Bot: {response.text}\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")
