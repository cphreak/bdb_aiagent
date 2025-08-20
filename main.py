import os, sys
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print(f"{sys.argv[0]} <prompt>")
    sys.exit(1)
else:
    prompt = sys.argv[1]


def main():
    print("Hello from aiagent!")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents = prompt
    )
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")





if __name__ == "__main__":
    main()
