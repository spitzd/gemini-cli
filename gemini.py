import google.generativeai as genai
import os

# ---

## Prepare Gemini

# Get API key from environment variable
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set it before running the script (e.g., export GEMINI_API_KEY='your_api_key_here').")
    exit(1) # Exit if the API key isn't found

model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')

# ---

## Get User Input

# Prompt the user to enter their question or prompt
user_prompt = input("Enter your question for Gemini: ")

# ---

## Generate Response

print("\nGenerating response...\n") # Provide feedback to the user

try:
    response = model.generate_content(user_prompt)
    print(response.text)
except Exception as e:
    print(f"An error occurred while generating the response: {e}")