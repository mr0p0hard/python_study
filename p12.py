#Program for random observing a bad words
#Mark1
import random

WORDS = ("Bitch", "Whore", "Shit", "Dumb", "Fuck", "Motherfucker")
#CopyPaste
jumble = ""
while WORDS:
    position = random.randrange(len(WORDS))
    jumble += WORDS[position] + " "
    WORDS = WORDS[:position] + WORDS[(position + 1):]

print(jumble)
input("Press ENTER to exit")
