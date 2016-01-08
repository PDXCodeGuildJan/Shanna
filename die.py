
from random import randint #import python function random-you have to tell it #to do this. Randint takes two variables and #picks one randomly. 

#Make a die function that returns a random number
def die (): #defines function die
	roll=randint (1,6)
	print(roll) #this print function always available

#Make a function called custom_die that takes a range and prints a random #number in that range
def custom_die(x, y): #x and y are the buckets you hold your variables in
	roll=randint(x, y) #this tells computer to pick anything between x and y
	print(roll)


def main(): 
	#Ask the user how many dice to roll
	total_rolls = input("How many dice do you want to roll?")

	#Convert input string to integer. Called casting.
	total_rolls= int(total_rolls)



	#How big are the dice? Can nest int and input, to convert from string.
	max_num = int(input("How many sides on the dice?"))
	

	#Roll that many dice. You'll need a FOR LOOP here.
	for something in range(0, total_rolls): 
		custom_die(1, max_num)

main()






