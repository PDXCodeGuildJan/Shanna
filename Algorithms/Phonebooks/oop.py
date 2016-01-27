"""A phone book program implemented with classes."""

__author__ = "Shanna Louise"

import re

def main():
   #test the Contact and Address classes with Harvey Shadoan
   harvey = Contact("Harvey", "Shadoan")
   harvey.phone_num ="4053902348"
   harvey.email = "professorpuppy@gmail.com"
   harvey.update_address("Home", city="Choctaw", state="OK")
   print(harvey)
   
class Contact:
   """This defines the Contact object to store information about people."""

   def __init__(self, f_name, l_name):
      self.first_name = f_name #self.first_name is the property on the object, f_name is the variable we pass to the object
      self.last_name = l_name 

      self.phone_num = ""
      self.addresses = {}
      self.email = ""

   def update_address(self, address_key, street=None, unit=None,
                     city=None, state=None, zip_code=None, country=None):
                     #address_key is the type of phoneumber, a string "Home" or "Work"

      if address_key in self.addresses:
         #if there already an address key in the person's address dictionary, 
         #we'll get out what was stored there and set it inside temp_address 
         temp_address = self.addresses[address_key]
      #make a new Address object
      else:
         temp_address = Address() 


      if street: #will resolve to false if street is empty, and so it won't do this if there's no street
         temp_address.street = street #this sets the memory location of address to whatever  
                                   # variable we pass it
      if unit:
         temp_address.unit = unit

      if city: 
         temp_address.city = city

      if state:
         temp_address.state = state

      if zip_code:
         temp_address.zip_code = zip_code
      
      if country:
         temp_address.country = country

      #assigns the address to the given key for the Contact 
      #"inside the self.address dictionary store at the key "Home": the value this address"
      #EACH CONTACT IS A MEMORY LOCATION THAT'S PASSED WHEN SOMEONE LOOKS UP "CONTACT NAME"
      self.addresses[address_key] = temp_address


   def format_phone_num(self, phone_num):
      """Format the phone number of the contact."""
      regex = "[0-9]+"
      #regex is catching all numbers 
      nums = re.findall(regex, phone_num)
      
      new_num = ""
      for every_num in nums:
         new_num += every_num
      #introduce the correct formatting
      formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
      self.phone_num = formatted_num

   def __str__(self):
      """Print out the contact's information, fancy-fancy."""
      #initialize formatted string. The .format takes whatever's in the curly brackets    
      #and replace them with whatever's stored in first and last name
      formatted_str = "{0} {1}".format(self.first_name, self.last_name)

      if self.phone_num:
         #formats the phone number
         self.format_phone_num(self.phone_num)
         #add the formatted number to the formatted string
         formatted_str += "\nPhone: {0}". format(self.phone_num)

      if self.email:
         formatted_str += "\nEmail: {0}".format(self.email)

      #if there is at least one address
      if self.addresses:
         formatted_str += "\nAddresses:"
         formatted_str += "\n---------------------------------------"

         #loop through all the addresses and print them
         #get all the key, value pairs of the addresses using the Dictionary.Items function
         for key, address in self.addresses.items():
            #loop through all the address and print them
            formatted_str += "\n{0}:".format(key)
            formatted_str += "\n{0}".format(address)
            formatted_str += "\n-------------------"

      return formatted_str



#beer fetching robot
#mail-orders a diving board,
#builds a volcano

# everyone knows that
# volcanoes eat broken things
# code becomes ashes

#beer fetching robot
#fills volcano with beer
#troubles forgotten


class Address:
   """This defines the Address object to be used with Contact."""

   def __init__(self):
      self.street = "" 
      self.unit = ""
      self.state = ""
      self.state = ""
      self.zip_code = ""
      self.country = ""

      
   def __str__(self):
      """Print out the address fancy-fancy."""
   
      formatted_str = ""
      formatted_str += "{0} {1}".format(self.street, self.unit)
      formatted_str += "\n{0} {1}".format(self.city, self.state)
      formatted_str += "\n{0}".format(self.zip_code)
      formatted_str +="\n{0}".format(self.country)

      

      return formatted_str

#if you type help(thingyoujustimported) it will show all the built-in functions

if __name__== '__main__':
   main()
    
      
