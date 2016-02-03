   #your function is catching the phone numbers and reformatting them
   #make a variable for what regex is catching
   #you can call this funciton



def number_fix(number):
   search_pattern = "[0-9]+"
   nums = re.findall(search_pattern, number)
   new_num = ""
   for number in nums:
      new_num += every_num
   



   formatted_num = "(" + new_num[0:3] + ")" + new_num[3:6:] + "-" + new_num[6:]
   print(formatted_num)

   number_fix()







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

scrubbed_num = scrub(caught_num)
def scrub
