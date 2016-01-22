"""Implements a very simple phone book using a dictionary"""
import re
__author__= "Shanna Louise"

# Initialize our dictionary, which will store our phone numers
phonebook = {}
#debug this whole dadgum thing
#add search and search by number to menu option, add print_phonebook to menu option
#scrub search terms, phone number inputs, handle typos (inc cases) 
#modify phone book to scrub phone number and format it the same way
def main():
   """The main driver function of our phonebook."""
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
   #of the pattern that you want.  You have to catch it in variable scrubbed_name
   #re is notation calling up regex module. results= re.search(regex pattern, search string)
   #we want a regex pattern that gets only the words, not the white space around 
   #scrub and reformat phone number to follow (xxx) xxx-xxxx pattern
   #remove all but the numbers. Find all characters that aren't numbers and remove them
   #replace with empty string
   regex = "[0-9]+"
   #make sure you can notate what this is doing
   nums = re.findall(regex, phonenumber)
   new_num = ""
   for every_num in nums:
      new_num += every_num
   
   #introduce the correct formatting
   #there is a better way to do this in regex
   formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
   print(formatted_num)

   phonebook[name] = formatted_num
   print("New contact: "+ name +  " was added with number: " + formatted_num)
   print("")

def delete_contact(name):
   """Removes the given contact from the phone book."""
   del phonebook[name]
   print(name, "was removed from the phonebook. ")

def search(name):
   """Find and print the info of a contact, when given the name."""
   number = phonebook[name]
   print(name, "'s number is", number, "\n")

def search_by_number(search_number):
   """Find who a certain number is associated with."""
   #this returns a list of tuples with key: value pairs
   #can also be written: "for key, value in dictionary.items" You can assign key and value
   result = " "
   for name, number in phonebook.items(): 
      if search_number == number:
         print(number, "'s name is" , name , "/n")
         result
   #when ordering this, always have the if key is in dict first, then the if it isn't scenario
   if result == "":
      print("Sorry, no contact has that number.  You're not alone, though. \n")

def print_phonebook():
   """Prints all contacts in the phone book, all tidy. """
   print("Contacts:")
   print("----------------------------------------------")
   for name in phonebook:
      print(name, ":\t", phonebook[name], "\n")

if __name__ == '__main__':
   main()

