import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    # Check if prompt argument was provided
    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        sys.exit(1)
    
    # Detect and remove the --verbose flag if present
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if arg != "--verbose"]
    
    # Check if there's still a prompt after removing --verbose
    if not args:
        print("Error: No prompt provided.")
        sys.exit(1)
    
    # Join all arguments after the script name into a single string
    user_prompt = " ".join(sys.argv[1:])
    
    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)
    
    # Create the message list
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    # Send a prompt to the Gemini model
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
)
    
    # Print the model's response    
    print(response.text)

    # If verbose flag is set, print extra debug info
    if verbose:
        print(f"\nUser prompt: {user_prompt}")
        if hasattr(response, "usage_metadata"):
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()
