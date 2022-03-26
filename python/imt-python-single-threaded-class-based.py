import random

class Typewriter:
    def __init__(self, alphabet):
        self.alphabet = alphabet
    

class Monkey:

    def __init__(self, typewriter, name):
        self.typewriter = typewriter
        self.name = name
        self.textIndex = 0
        self.noMistakes = True
    
    def type(self, text):
        while(self.noMistakes):
            pickedLetter = random.choice(self.typewriter.alphabet)
            if(pickedLetter == text[self.textIndex]):
                self.testIndex += 1
            else:
                print(self.__str__() + " Failed after " + str(self.textIndex) + " letters")
                self.noMistakes = False

    def __str__(self):
        return self.name


alphabet1 = 'abcdefghijklmnopqrstuvwxyz '
text = 'Hello World'
typewriter1 = Typewriter(alphabet1)
monkey1 = Monkey(typewriter1, 'Quincy')

monkey1.type(text.lower())