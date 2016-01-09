#Greet w/instruction
#Assign house at random
#print house designation with description

from random import choice

def sorting_hat():
	print ("Welcome to Hogwarts. Please place the sorting hat on your head.")
	#PICK RANDOM HOUSE
	rand_item = choice(["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"])
#print characteristics of chosen house
	if rand_item == 'Hufflepuff':
		print (rand_item, "You belong in Hufflepuff, where they are just and loyal.  Those patient Hufflepuffs are true, and unafraid of toil.")
	elif rand_item == "Griffindor":
		print (rand_item, "You belong in Gryffindor, where dwell the brave at heart. Their daring, nerve, and chivalry set Gryffindors apart.")
	elif rand_item == 'Ravenclaw':
		print (rand_item , "You belong in wise old Ravenclaw, if you've a ready mind, where those of wit and learning will always find their kind.")
	else rand_item == 'Slytherin':
		print (rand_item , "You belong in Slytherin, where you'll make your real friends. Those cunning folks use any means to achieve their ends.")

	#Can also be if roll == num1:
			#print("{r} Critical fail".format(r=roll))
# do the dot format like this, instead of commas or pluses "{name} is {age} and is from 
#{place}".format(name=name, age=age, place=place)
