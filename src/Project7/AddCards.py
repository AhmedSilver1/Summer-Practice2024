##The original source code is from The Complete Coding for Beginners Course(2024) Section 16

from googletrans import Translator
import os
import ast


translator = Translator()
fileName="FlashCards.txt"
cards = []


def readCradsFromFile():
    cards=[]
    if os.path.exists(fileName):
        with open(fileName,"r") as file:
            cards= ast.literal_eval(file.read())
    return cards

def displayCards(cards):
    print("The current card list contains "+ str(len(cards))+" card.")
    for i,card in enumerate(cards):
        print(str(i+1)+"."+ card[0]+ " : "+ card[1])


def translateWord(wordEn):
    wordEs = translator.translate(wordEn, src="en", dest="es").text
    return wordEs



def createNewCard():
    global cards
    wordEn = input("Type a word in English to get the Spanish translation: ")
    wordEs = translateWord(wordEn)
    newCard = (wordEn, wordEs)
    print(newCard)
    answer = input("Do you want to save this card? (yes/no) ")
    if answer == "yes":
        cards.append(newCard)


def saveCardsToFile():
    answer = input("Do you want to save the card to the file? (yes/no)")
    if answer == "yes":
        print("Saving cards..")
        with open(fileName, "w") as file:
            file.write(str(cards))

cards = readCradsFromFile()
displayCards(cards)
while True:
    createNewCard()
    answer= input("Do you want to translate another word? (yes/no) ")
    if answer == "no":
        break



print(cards)
saveCardsToFile()
print("End of program.")
