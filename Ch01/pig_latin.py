"""Pig Latin word Translator"""

VOWELS = "aeiouy"
OUTPUT = "\033[1;92m{}\033[0m"

def main():
    """Prompts user for a string and returns it's into pig latin"""
    print("Welcome to the pig latin translation system.")

    while True:
        user = input("Please enter a word to convert to pig latin:\n")

        if user[0] in VOWELS:
            print(OUTPUT.format(user + "way"))

        else:
            print(OUTPUT.format(user[1:]+user[0]+"ay"))

        choice = input("Would you like to run again? (n/Y)\n")
        if choice.lower() in ("exit", "quit", "q", "no", "n"):
            break

if __name__ == "__main__":
    main()
