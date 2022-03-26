import random, sys, keyboard

attemptNo = 0
bestAttempt = 0
bestAttemptNo = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz '
text = 'hello'
textIndex = 0

def type(monkeyName, alphabet, text):
    global bestAttempt, bestAttemptNo
    textIndex = 0
    noMistakes = True
    while(noMistakes):
        pickedLetter = random.choice(alphabet)
        if(pickedLetter == text[textIndex]):
            textIndex += 1
            if (textIndex == len(text)):
                print("Full text has been typed")
                print("Monkeys name is " + monkeyName)
                print("On attempt number " + str(attemptNo))
                sys.exit(0)
        else:
            if (textIndex > bestAttempt):
                bestAttempt = textIndex
                bestAttemptNo = attemptNo
            noMistakes = False
    return

while(True):
    if(keyboard.is_pressed("q")):
        print("Best Attempt " + str(bestAttempt) + " on attempt number " + str(bestAttemptNo))
        print("Program Quit on attempt number " + str(attemptNo))
        break

    attemptNo += 1
    type("Quincy", alphabet, text.lower())
    
