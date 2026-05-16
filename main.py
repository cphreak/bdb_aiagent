import os, sys
sys.path.insert(0, '/Users/scl/src/bootdotdev/python/aiagent')
import argparse
from dotenv import load_dotenv
import prompts
from config import MAX_ITERATIONS

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
verbose = False
from google import genai
from google.genai import types
from functions.call_function import available_functions, call_function

client = genai.Client(api_key=api_key)

# if len(sys.argv) < 2:
#     print(f"{sys.argv[0]} <prompt>")
#     sys.exit(1)
# else:
#     user_prompt = sys.argv[1]
# if len(sys.argv) > 2:
#     if sys.argv[2] == "--verbose":
#         verbose = True

# user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# verbose = True

def main():
    print("Hello from aiagent!")
    candidates = ""

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
        ]

    for _ in range(MAX_ITERATIONS):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(tools = [ available_functions ] ,system_instruction=prompts.system_prompt),
            )

        if response.candidates != None:
            for c in response.candidates:
                messages.append(c)
                # print(f"messages: {messages}"

        if response.usage_metadata == None:
            raise RuntimeError("failed response!")
            exit(1)
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        function_results = list()
        if response.function_calls != None:
            for f in response.function_calls:
                # print(f"Calling function: {f.name}({f.args})")
                function_call_result = call_function(f)
                if function_call_result.parts == None:
                    raise RuntimeError("Empty Content.parts in response")
                if function_call_result.parts[0].function_response == None:
                    raise RuntimeError("Empty .parts[0].function_response")
                if function_call_result.parts[0].function_response.response == None:
                    raise RuntimeError("Empty .parts[0].function_response.response")
                function_results.append(function_call_result.parts[0])
                messages.append(types.Content(role="user", parts=function_results))
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        else:

            print(f"Response: ")
            print(response.text)
            exit(0)


    print(f'Reached maximum interations without a result!')
    exit(1)




if __name__ == "__main__":
    main()
