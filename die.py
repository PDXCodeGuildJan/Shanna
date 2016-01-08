
from random import randint #import python function random-you have to tell it #to do this. Randint takes two variables and #picks one randomly. 

#Make a die function that returns a random number
def die (): #defines function die
	roll=randint (1,6)
	print(roll) 

#Make a function called custom_die that takes a range and prints a random #number in that range

def custom_die(num1, num2): #num1 and num2 are the buckets you hold your variables in
	roll=randint(num1, num2) #this tells computer to pick anything between
	
#determine if max or min 

	if roll == num1: #num1 is min in range
		print(num1, "Critical fail!") #feeding print statement multiple arguments
	elif roll == num2:  #num2 is max in range
		print(num2, "Critical hit!")
	else: #if neither, print only the number.
		print(roll)

def main(): 
	print("Welcome to Die Roller. Enter q to exit.")

	entree = "" #empty string, must make it not equal q.
	
	while entree != "q":

		entree = input("How many dice do you want to roll?")
		if entree == "q":
			#exit the program. can avoid repeat in line 34 with a function.
			exit()

		#Convert input string to integer. Called casting.
		#it's not q, it has to be total rolls, assign to total_rolls
		total_rolls= int(entree)

		#How big are the dice? Can nest int and input, to convert from string.
		entree = input("How many sides on the dice?")

		if entree == "q":
			#exit the program
			exit()
		#already checked to see entree wasn't q, now turn that entree into an int
		max_num= int(entree)
		

		#Roll that many dice. You'll need a FOR LOOP here.
		for something in range(0,total_rolls): 
			custom_die(1, max_num) #this prints the number
			
	
main()


