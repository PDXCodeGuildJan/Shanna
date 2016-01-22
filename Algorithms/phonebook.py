"""Implements a very simple phone book using a dictionary"""
import re
__author__= "Shanna Louise"

# Initialize our dictionary, which will store our phone numers
phonebook = {}
#debug this whole dadgum thing
#fix search by number case sensitive tangle
#regex function 
#modify phone book to scrub phone number and format it the same way
#add a "do you want to add another? " option to add contact
#you can learn .format for strings to tidy columns (string formatting)
def main():
   """The main driver function of our phonebook."""

   #Load any existing data into phone book
   load_phonebook()
   print("Phone book after load:", phonebook)
   print ("Welcome to the phone book.\nIt's all going to be ok. ")
   option = " "
   while option != "E" :
      #Ask the user what they want to do
      option = input("(A)dd\n(D)elete Contacts\n(P)rint Contacts\n"
                  "(S)earch by Name\n(N)umber Search\n(E)xit.\n"
                  "Which would you like to do? \n")
      option = option.upper()
      if option == "A":
         name = input("What is the new contact's name? ")
         number = input("What is " + name + "'s number? ")
         add_contact(name, number) 
   #THIS ISN'T WORKING BUT KEEP TRYING
#         pass
#         answer = input("Would you like to add another contact? \n"
#                          "(Y)es\n(N)o"
#           if answer == "Y":
#                  add_contact(name, number)
      elif option == "D" :
         name = input("What contact are you removing? ")
         delete_contact(name)
         print
      elif option == "S":
         name = input ("What name would you like to search? ")
         search(name)
      elif option == "N":
         number = input("What number would you like me to match with a person? ")
         search_by_number(number)
      elif option == "E":
         print("Thanks, and so long. You're trying your best. ")
         exit()
      elif option == "P" : 
         print_phonebook()
      else: 
         print("I'm a computer and I didn't understand. Try again, human. ")
def add_contact(name, phonenumber):
   """Adds the given contact information to the phonebook.."""
   #remove any lingering white space that might have been added.  You have to pass the regex
   #of the pattern that you want.  You have to catch it in variable 
   #re is notation calling up regex module. results= re.search(regex pattern, search string)
   #we want a regex pattern that gets only the words, not the white space around 
   #scrub and reformat phone number to follow (xxx) xxx-xxxx pattern
   #remove all but the numbers. Find all characters that aren't numbers and remove them
   #replace with empty string
   regex = "[0-9]+"
   #regex is catching all numbers GET HELP EXPLAINING THIS SECTION
   nums = re.findall(regex, phonenumber)
   new_num = ""
   for every_num in nums:
      new_num += every_num
   #introduce the correct formatting
   #there is a better way to do this in regex but i don't know it
   formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
   print(formatted_num)
   #in phonebook, the key(which is name) is updated with the formatted number
   phonebook[name] = formatted_num
   print("New contact: "+ name +  " was added with number: " + formatted_num)
   print("")

   #save updated phonebook
   save_phonebook()

def delete_contact(name):
   """Removes the given contact from the phone book."""
   del phonebook[name]
   print(name, "was removed from the phonebook. ")
   #save updated phonebook
   save_phonebook()

def search(name):
   name = name.upper()
   """Find and print the info of a contact, when given the name."""
   number = phonebook[name]  
   print(name, "'s number is", number, "\n")

def search_by_number(search_number):
   """Find who a certain number is associated with."""
   #this returns a list of tuples with key: value pairs
   #can also be written: "for key, value in dictionary.items" You can assign key and value
   #if you make a function for your regex number fixing, you could save code.
   #call it right before you result
   result = " "
   for name, number in phonebook.items(): 
      if search_number == number:
         print(number,"'s name is" , name , "/n")
         result
   #when ordering this, always have the if key is in dict first, then the if it isn't scenario
   if result == "":
      print("Sorry, no contact has that number.  You're not alone, though \n")

def print_phonebook():
   """Prints all contacts in the phone book, all tidy. """
   print("Contacts:")
   print("----------------------------------------------")
   for name in phonebook:
      print(name, ":\t", phonebook[name], "\n")

#save phonebook data to a file
#load data from a file into a phonebook
#autosave phonebook after any data modifications
#load of phonebook program, load saved file
def save_phonebook():
   """Save the contents of the phone book to a file."""
   open_file = open("phonebook.txt", "w")
   #convert dictionary to string, as write expects strings
   open_file.write(str(phonebook))
   open_file.close()

def load_phonebook():
   """Load the phone book data from the save file."""
#  Gives function permission to update global variable
#  If we're updating the memory address of a global variable, (like
#  convert from a string to a dictionary-that changes the location),we have to
#  give the computer permission to update the global 
   global phonebook
   #Open the file in write mode first, to create one if does not already exist
   
   load_file = open("phonebook.txt", "w")
   load_file.close()
   input()
   #Open file in read mode so we can read from it
   load_file = open("phonebook.txt" , "r")
   phonebook_data = load_file.read()
   load_file.close()
   # If phonebook data has any data stored in it, load it in the dictionary
   if phonebook_data:
      #Convert from string back to dictionary
      phonebook = eval(phonebook_data)
if __name__ == '__main__':
   main()
