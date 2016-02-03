pass
#this function multiplies all numers in a list

def multiply(numbers):
   total = 0
#for as many times as there are numbers in the list
   for x in numbers:
#the new total = total * x 
      total *=x
   return total
print(multiply((8,2,3,0,7)))
   
for phonebook.py
         name = input("What is the new contact's name? ")
         number = input("What is " + name + "'s number? ")
         add_contact(name, number) 
         answer = input("Would you like to add another contact? \n"
                          "(Y)es\n(N)o"
         while answer == "Y":
            (name, number) = input("What is the new contact's name? ")
            add_contact(name, number)

def new_contact():
   name = input("What is the new contact's name? ")
   number = input("What is the new contact's number?")
   new_contact(name, number)
   print(name + "has been added to the phone book.")
   
