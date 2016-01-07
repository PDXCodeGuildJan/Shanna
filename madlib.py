# Make a madlib that prompts the user for 5 words/phrases and adds them to a silly story

madlib = "Volcanoes are the best places for throwing your " 


adjective = input("Please give an adjective: ")
plural_noun = input("Please give a plural noun: ") 

madlib = madlib + adjective + " " + plural_noun + ". Most people avoid volcanoes, but they can be very useful. First, you should " #adding pl noun to madlib

verb= input("Please give a verb: ")

madlib = madlib + verb + " the volcano that is right for you.  You'll need a "

noun = input("Please give a noun: ")

madlib = madlib + noun + ", a shovel, and an enthusiastic friend.  Take a deep breath, toss in all your "

plural_noun= input("Please give a plural noun: ")

madlib = madlib + plural_noun + ", and enjoy a pleasant future."

print(madlib)


