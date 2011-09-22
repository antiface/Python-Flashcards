import sys
import random

def printWelcomeMessage():
	print("Welcome")
	
def getFileName():
	'''Asks user to type in the name of the file where 'flash cards' are stored''' 
	fileName = input("Please type in the the name of your index card file: ")
	return fileName


def readFlashCards(fileName):
    """Read in flash cards from the named file, and return as a list of tuples."""
    flashCards = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                flashCards.append(eval(line))
    return flashCards
	
def presentAllCards(listOfFlashCards):
	'''Presents each flashcard in the list one by one'''
	for flashCard in listOfFlashCards:
		presentCard(flashCard)
		
def presentCard(flashCard, guessNumber=0):
	'''Displays one flashcard. Prints question, asks for input, checks if user types in quit, checks if questions is right. If not it says try again, if wrong again it displays correct answer.''' 
	print(flashCard[0])
	answer = input()
	checkIfQuitting(answer)
	if answer == flashCard[1]:
		print("Right! \n")
		return
	elif guessNumber == 0:
		print("No, that's wrong. The first letter is: ", flashCard[1][0], "\n")
		presentCard(flashCard, 1)
	else:
		print("Still wrong. Correct answer is: ", flashCard[1], "\n") 

def checkIfQuitting(answer):
	'''If the user types 'quit', then exit program.'''
	if answer == 'quit':			
		sys.exit()
		
def shuffle(list):
	'''Creates another list and shuffles created list. Returns newly created shuffled list'''
	shuffledList = []
	shuffledList.extend(list)
	random.shuffle(shuffledList)
	return shuffledList
	
def main():
	printWelcomeMessage()
	fileName = getFileName()
	i = 1
	while i > 0:
		#returns a list of all the flash cards 
		flashCards = readFlashCards(fileName)
		shuffledList = shuffle(flashCards)
		presentAllCards(shuffledList)


main()
