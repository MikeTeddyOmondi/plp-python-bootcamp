from dictionary_lookup import get_definition

def main():
    print("Welcome to the Dictionary Lookup Program!")
    
    while True:
        word = input("Enter a word to look up, or 'exit' to quit: ")
        if word.lower() == 'exit':
            print("Exiting the dictionary lookup program. Goodbye!")
            break
        
        # Step 4: Print the definition or handle the word not found
        definition = get_definition(word)
        
        # Print each meaning on a new line if there are multiple definitions
        if isinstance(definition, list):
            print(f"\nDefinitions for '{word}':")
            for meaning in definition:
                print(f"- {meaning}")
        else:
            print(definition)

# Run the program
main()
