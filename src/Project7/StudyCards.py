##The original source code is from The Complete Coding for Beginners Course(2024) Section 16

import os
import ast
import random
import time
fileName="FlashCards.txt"

def exitIfNoCards():
    if not os.path.exists(fileName):
        print("There is mno available cards. Exiting the program...")
        exit()


def readCradsFromFile():
    cards=[]
    if os.path.exists(fileName):
        with open(fileName,"r") as file:
            cards= ast.literal_eval(file.read())
    return cards

def gessCards():
    global cards
    while len(cards)>0:
        index = random.randint(0,len(cards)-1)
        wordEn = cards[index][0]
        wordEs = cards[index][1]
        answer= input(wordEn + "? ")
        if answer == wordEs:
            print("Correct!")
            del cards[index]
        else:
            print("Your answer is wrong, try again.")



exitIfNoCards()
cards = readCradsFromFile()
print("You have "+str(len(cards))+ " cards to guess.")
input("Press ENTER to begin")
timeStart = time.time()
gessCards()
timeEnd = time.time()
duration = int(timeEnd- timeStart)
print("You guessed all the cards in "+ str(duration)+ " seconds.")
print("End of the program")