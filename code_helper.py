import argparse
import requests
import json

def get_code_suggestion(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1",
        "prompt": prompt
    }
    response = requests.post(url, json=data, stream=False)
    
    # # Debugging step: print the raw response
    # print("RAW RESPONSE TEXT:", response.text)
    
    # Only try to parse JSON after checking the response format
    # check the response status
    if response.status_code == 200:
        print("Generated Text:", end=" ", flush=True)
        # Iterate over the streaming response
        for line in response.iter_lines():
            if line:
                # Decode the line and parse the JSON
                decoded_line = line.decode("utf-8")
                result = json.loads(decoded_line)
                # Get the text from the response
                generated_text = result.get("response", "")
                print(generated_text, end="", flush=True)
    else:
        print("Error:", response.status_code, response.text)

def main():
    parser = argparse.ArgumentParser(description="A simple script to print a prompt")
    parser.add_argument("prompt", help="The prompt to display")
    args = parser.parse_args()

    get_code_suggestion(args.prompt)

if __name__ == "__main__":
    main()