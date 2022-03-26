import random
import keyboard
import sys



class Typewriter:
    def __init__(self, alphabet):
        self.alphabet = alphabet


class Monkey:

    def __init__(self, typewriter, name):
        self.typewriter = typewriter
        self.name = name

    def type(self, text):
        self.textIndex = 0
        self.noMistakes = True
        while(self.noMistakes):
            pickedLetter = random.choice(self.typewriter.alphabet)
            if(pickedLetter == text[self.textIndex]):
                self.textIndex += 1
                if (self.textIndex == len(text)):
                    print("Full text has been typed")
                    print("Monkeys name is " + self.__str__())
                    print("On attempt number " + str(attemptNo))
                    sys.exit(0)
            else:
                self.noMistakes = False

    def __str__(self):
        return self.name


alphabet1 = 'abcdefghijklmnopqrstuvwxyz '
text = 'hello'

attemptNo = 0
bestAttempt = 0
bestAttemptNo = 0

typewriter1 = Typewriter(alphabet1)
monkey1 = Monkey(typewriter1, 'Quincy')

while(True):
    if(keyboard.is_pressed("q")):
        print("Best Attempt " + str(bestAttempt))
        print("Program Quit on attempt number " + str(attemptNo))
        break

    attemptNo += 1
    monkey1.type(text.lower())
    if (monkey1.textIndex > bestAttempt):
        bestAttempt = monkey1.textIndex
        bestAttemptNo = attemptNo
