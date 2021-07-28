import random

words = ["STEPPER IT", "AMRITSAR", "TIME OUT"]
wpos = random.randint(0, 2)


wordMask = ""
wrongs = ""
max_attempts = 6
attempts = max_attempts
inputs = ""
hangman = ""


def build_mask_word():
    global wordMask, inputs
    wordMask = ""
    for ch1 in words[wpos]:
        if(ch1 == " "):
            wordMask = wordMask + "  "
        elif(ch1 in inputs):
            wordMask = wordMask + ch1
        else:
            wordMask = wordMask + "_ "


def find_replace_mask(ch):
    global wrongs, wordMask, attempts, inputs
    inputs = inputs + ch
    if ch in words[wpos]:
        build_mask_word()
    else:
        wrongs = wrongs + " " + ch
        attempts = attempts - 1


def print_hangman():
    global hangman
    hangman = ""
    if(max_attempts - attempts > 0):
        hangman += "\n   0 "
    if(max_attempts - attempts > 1):
        hangman += "\n   | "
    if(max_attempts - attempts > 2):
        hangman += "\n / |"
    if(max_attempts - attempts > 3):
        hangman += " \\"
    if(max_attempts - attempts > 4):
        hangman += "\n / "
    if(max_attempts - attempts > 5):
        hangman += "  \\"
    print("\n", hangman)


build_mask_word()
while(attempts > 0 and "_" in wordMask):
    print("wrongs -> ", wrongs)
    print("Attemps -> ", attempts)
    print_hangman()
    print(wordMask)
    ch = input("enter a letter: ")
    find_replace_mask(ch.upper())


print(wordMask)
print_hangman()
if(attempts > 0):
    print("You won !!!")
else:
    print("You loose :(")
