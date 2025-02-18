import argparse

def print_prompt(prompt):
    print("Your prompt is:", prompt)

def main():
    parser = argparse.ArgumentParser(description="A simple script to print a prompt")
    parser.add_argument("prompt", help="The prompt to display")
    args = parser.parse_args()

    print_prompt(args.prompt)

if __name__ == "__main__":
    main()