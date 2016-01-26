"""A program to translate Morse Code into English, and vice versa"""
from morse import morse
import re
__authors__ = "Dre and Shanna"


def main():

   write_code("Corgis are the best breed of dog, I don't care what you say.", "dragons.txt")
   """The main driver function of our translation program"""

   read_code("test_code.txt")

#takes a string containing a reference to the file containing Morse message
def read_code(morse_msg_filename):
   """This functions opens a file of Morse code and translates it into English"""
   #opens morse code message file. Open file is the file object variable, 
   open_file = open(morse_msg_filename)
   #dump contents of open_file and save them to a variable
   morse_msg = open_file.read()   
   #close the file using the file object
   open_file.close()
   #translates contents of Morse file
   #empty variable to hold newly decoded string
   decoded_string = ""
   #wherever there are seven spaces, make a list of the things between the seven-spaces
   list_of_words = re.split("       ", morse_msg)
   for word in list_of_words: 
      #wherever there are three spaces, make a string of the things between the three-spaces
      list_of_letters = re.split("   ", list_of_words)

   print(list_of_words)
   print (list_of_letters)

   #look into the morse dictionary at each letter: code tuple
   
      #if the searched for string (code) shows up in the tuples anywhere

         #create a new string of the keys associated with this value in tuples 
      
      #look back at the dictionary with the morse code parsed into morse_clumps

      #
      
#writes new English translation to string

#returns a string


#take English string and
#take string (filename you will write morse translation to)

def write_code(eng_string, morse_filename): 
   """This function takes an English string and translates it into Morse code"""
   #gets ready to hold a string of morse (translated from eng_string)
   encoded_string = ""
   #check all the letters in the English string
   for character in eng_string.upper():
   #if the english key is in dict
      if character in morse:
         #get the value at the letter key
         code = morse[character]
         #put morse value in an empty string, at the same position, and three spaces

         #which separate characters in morse.
         encoded_string += code + "   "
      #if character is a space in eng_string
      elif character == " ":
         #replace with seven morse spaces
         #opens a file with the given filename
         open_file = open(morse_filename, "w")
         #adds the encoded_string to the file
         open_file.write(encoded_string)
         #closes and saves file
         open_file.close()


if __name__=='__main__':
   main()  
