import json
from difflib import get_close_matches

json_data = open("Dictionary\data.json")
data = json.load(json_data)
def translate(word):
    if word in data:
        return data[word]
    else:
        match = str(*get_close_matches(word, data.keys(), n=1))
        if match:
            conformation = str(input(f"Did you meant {match} instead? y if yes or n if no: ")).lower()
            if conformation == "y":
                return translate(match)
            elif conformation == "n":
                return f"The word {word} doesn't exist. Please doublecheck it and try again."
            else:
                return "We didn't understand your entry..."
        else:
            return f"The word {word} doesn't exist. Please doublecheck it and try again."

word = str(input('Enter the word: ')).lower()

output = translate(word)

if type(output) == list:
    for index, meaning in enumerate(output, start=1):
        print(f"{index}. {meaning}")
else:
    print(output)