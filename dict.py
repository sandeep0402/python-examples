import json
from difflib import get_close_matches

dc = json.load(open('data/dict-data.json'))


def translate(word):
    if word in dc:
        return dc[word]
    elif word.lower() in dc:
        return dc[word.lower()]
    elif word.upper() in dc:
        return dc[word.upper()]
    elif word.capitalize() in dc:
        return dc[word.capitalize()]
    elif word.title() in dc:
        return dc[word.title()]
    elif len(get_close_matches(word, dc.keys())) > 0:
        print(f" Do you mean by {get_close_matches(word, dc.keys())[0]}.")
        decision = input("Press y for yes or n for No")
        if decision.lower() == 'y':
            return dc[get_close_matches(word, dc.keys())[0]]
        else:
            return "Please enter input again."
    else:
        return "Nothing found here"


def print_dict(output):
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


word = input("Enter the word here:")
output = translate(word)
print_dict(output)
