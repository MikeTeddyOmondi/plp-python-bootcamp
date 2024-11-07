import json
import difflib  # To suggest close matches for misspelled words

# Step 1: Load the dictionary data from a JSON file
with open("data.json") as file:
    data = json.load(file)  # Load JSON data into a dictionary

def get_definition(word):
    """
    Returns the definition of a word from the dictionary data.
    
    Parameters:
        word (str): The word to look up.
        
    Returns:
        str: Definition of the word or an appropriate message.
    """
    word = word.lower()  # Convert word to lowercase for case-insensitive matching
    
    if word in data:
        return data[word]  # Return the definition if found in the dictionary
    else:
        # Step 5: Intelligent suggestion for misspelled words using difflib
        close_matches = difflib.get_close_matches(word, data.keys())
        if close_matches:
            # Suggest the closest matching word
            suggestion = close_matches[0]
            yn = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ")
            if yn.lower() == 'y':
                return data[suggestion]
            elif yn.lower() == 'n':
                return "The word does not exist in the dictionary."
            else:
                return "We didn't understand your input."
        else:
            return "The word does not exist in the dictionary."

