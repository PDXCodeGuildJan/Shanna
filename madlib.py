# Make a madlib that prompts the user for 5 words/phrases and adds them to a silly story

madlib = "Volcanoes are the best places for throwing your " 

adjective = input("Please give an adjective: ")

plural_noun = input("Please give a plural noun: ") 

madlib = madlib + adjective + " " + plural_noun + ". Most people avoid volcanoes, but they can be very "  #adding pl noun to # madlib changes value of original madlib variable to include the new input

adjective= input("Please give an adjective: ")

madlib = madlib + adjective + ". First, you'll need to locate the volcano that is right for you.  Bring a "

noun = input("Please give a noun: ")

madlib += noun + ", a shovel, and an enthusiastic friend.  Take a deep breath, toss in all your "

plural_noun= input("Please give a plural noun: ")

madlib += plural_noun + ", and enjoy a pleasant future." #madlib += is the same thing as madlib =madlib + 

print(madlib)


