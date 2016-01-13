#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["constellation", "artichoke" , "burlesque", "volcano", "uncanny" , "ravioli" , "trampoline" ]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over. Computer picks word from list, dashifies it, prompts for input
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words. Can also use random.choice for this

   numinlist=len(words) #finds how many words in list
   num=randint(0, (numinlist-1)) #returns the location of random word from list, represented by a number
   foundword=words[num]   #uses that number location to get the corresponding word from list
   listedWord=list(foundword)   #makes the randomly selected word into a list object
   # Make another list the same length as the word, but with '_' instead of letters. This will track progress.
   currentState = []   #creates a list called currentState
   for x in listedWord: #the for loop will iterate over every character in listedword
      currentState.append("_") #for every character in listedword, add a dash to current state
   
   printHangperson(currentState)   # Print the initial state of the game
   incorrect = [] #creates an empty list for storing wrong guesses

   # Start the game! Loop until the user either wins or loses. This while loop runs the whole game.

   while currentState != listedWord and numWrong < 6: #numWrong = remaining turns
   #First, ask user to guess, and store the information in variable "guess"
      guess=userGuess() #calls userGuess function 
      bundledLists = updateState(guess, currentState, incorrect) 
      currentState = bundledLists[0]
      incorrect = bundledLists [1]
      printHangperson(currentState) #calls function Hangperson and passes it the currentState variable
      if currentState == listedWord: #if the currentState equals the listed word you won
         print ("Yay!  You won!")
      elif numWrong >= 6: #if your wrong tries numWrong is more than six, you lose
         print ( "Sorry, you're dead. ")



#Variables
# guess: a character guessed by the user
# currentState: the current state of the word/game, changed with each guess
#numWrong: the times a user has guessed incorrectly
#numInWord is how many times a letter guess appears in the random word
#index is the position in the list we're checking

def updateState(guess, currentState, incorrect):
   global numWrong 

   # First, determine if the letter guessed is in the word.
   # If it isn't, tell the user and update the numWrong var
   # If it is, congratulate them and update the state of the game.

   numInWord = listedWord.count(guess) #num of letters in word the listed word
   if numInWord == 0: 
      numWrong = numWrong +1 #can shorthand with numWrong +=1. Updates numWrong with each missed try
      incorrect.append(guess) #this adds the incorrect answers to the list we created to hold them.
      print ("Nope. Try again, please.")
   else numInWord > 0: 
      print("Way to go! You found {0} of the letter {1} in the mystery word ".format(numInWord, guess))
      #can also say print ("Way to go! You found" str(numInWord) + "of the letter" + {guess} + "in the mystery word. ")

#while we still have letters to find, keep looping
   numFound = 0 #this is the # of times a letter appears in a word.
   index = 0 #first position in list
   while numFound < numInWord and index < len(listedWord): #AND THIS ONE TOO IN WORDS 
      if listedWord[index] == guess: #if variable stored @ index 0 (the first position) of the listedword is the same as the guess
         currentState[index] = guess #this list[position] format inserts the guess in the index location of the dashy word
         numFound+=1 #this updates the number of letters we've found 

      index +=1 #shorthand for updating index variable, runs the loop checking the next position each time
   return currentState

def userGuess():
   guess = input("Guess a letter in the word! (Type 'exit' to stop playing) ") #prompts for guess
   while len(guess) != 1: #accepts only single letters  
      if guess == "exit":#check if input is "exit" and exit, if it is
         exit()
      #if not, ask them to guess again
      else: # accepts only single characters
         guess=input("Guess another character.")
   return guess #returns a letter

   

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word. Pass current state.
def printHangperson(state, incorrect):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")
   print (incorrect)
   print ()

# This line runs the program on import of the module
hangperson()
