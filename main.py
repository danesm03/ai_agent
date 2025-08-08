import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

#Import/connect API_KEY
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

#Instantiate client, messages, prompt definition
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]   

#Validate prompt provided and generate model response
if len(sys.argv) < 2:
    print("No prompt provided")
    sys.exit(1)
else:   
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

#Prompt information declarations
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count




#--verbose CLI Flagging
if "--verbose" in sys.argv: 
    print(
        f"{response.text}\nUser prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}"
        )
else: 
    print(response.text)


