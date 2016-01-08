adjective1 = input("Please give an adjective: ")
plural_noun1 = input("Please give a plural noun: ")
adjective2= input("Please give an adjective: ")
noun = input("Please give a noun: ")
plural_noun2= input("Please give a plural noun: ")

madlib='''Volcanoes are the best places for throwing your {} {}. 
Most people avoid volcanoes, but they can be very {}. 
First, you'll need to locate the volcano that is right for you. 
 Bring a {}, a shovel, and an enthusiastic friend.  Take a deep breath, 
toss in all your {}, and enjoy a pleasant future.'''.format(adjective1, plural_noun1, adjective2, noun, plural_noun2)

print(madlib)
