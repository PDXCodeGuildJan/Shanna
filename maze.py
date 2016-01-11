import sys

#create a text based maze with five rooms, including the start and finish, and handle incorrect inputs gracefully. For extra coolness, handle inputs without case-sensitivity, add a trap, output the path taken at the finish.

#Dear Shanna, you need a way to quit the game and also a way to store/give back the path taken

1#Greet
def main():

    print ("Welcome! You are a traveler searching for the Eternal Cake, rumored to be deep in the recesses of a cursed castle.  After hacking through the vines at the castle's entrance, you find yourself facing a single door. You push it open and proceed cautiously.")
    invalidentry = True
    while invalidentry == True:
        direction=input ("Press e to enter. ")
        direction=direction.lower()
        if direction == "e":
            vines()
        elif direction =="q":
            exit()
        else:
            print ("I don't understand. Please try again.")
      

#create a function for each room
#validation boolean-this makes sure that if we get the answers north/east/west, it moves on, but anything else, will loop back and give us the chance to try again.

def vines():
     invalidentry = True
     while invalidentry == True:
          print("You are in a room covered in vines and mysterious flora. The vines begin to twine around your ankles-you've got to get outta here! There are doors to the north, west, and east.")
          direction = input("Which way do you go? ")
          direction=direction.lower()
          if direction == "north":
               invalidentry = False
               pterodactyls()
          elif direction == "east":
               invalidentry=False
               leavecastle()
          elif direction == "west":
               invalidentry = False
               rainbow()
          elif direction =="q":
               invalidentry = False
               exit()
          else: 
               print("I don't understand. Please try again.")

# choices-north, west, east
#if east, you leave the castle
#if west, there is a room of rainbows
#if north, you get eaten by pterodactyls
#anything else print "I don't understand. Please try again."

def leavecastle():
     print("You walked back out the front door.  No cake for you. Press q to quit.")
     exit ()

def dungeon():
     invalidentry = True
     while invalidentry == True:
          print("This must be the dungeon.  It is full of ghosts and sharks. There is a door to the south and one to the north.")
          direction=input("Which do you take? ")
          direction=direction.lower()
          if direction == "north":
               invalidentry = False
               rainbow()
          elif direction == "south":
               invalidentry = False
               eternalcake()
          elif direction == "q":
               invalidentry = False
               exit()
          else:
               print("I don't understand. Please try again.")
#if choice north, def(rainbow)
#eternal cake only activated if "south" is chosen in dungeon.

def eternalcake(): 
     print("You have discovered the Cake of Eternity without getting eaten by pterodactlys or melted.  Congratulations, human-made-of-dust! The cake is not a lie. Eat it and be happy, or use it to rule the world. This is the end.  Press q to quit. ")
     exit()

def rainbow():
     invalidentry = True
     while invalidentry == True:
          print("This room is made of rainbows, and it's hard to find your way. The floor is covered in clown noses and balloon weasels. There are doors to the north, south, and east.")
          direction=input("Which way do you go? ")
          direction=direction.lower()
          if direction == "north":
               invalidentry = False
               volcano()
          elif direction == "south":
               invalidentry = False
               dungeon()
          elif direction == "east":
               invalidentry = False
               vines()
          elif direction == "q":
               invalidentry= False
               exit()
          else:
               print ("I don't understand. Please try again. ")
          
# if choice north, portal to jupiter
#if choice south, rainbow room
#if choice east, vines

def jupiter(): 
     print ("You've discovered a portal to Jupiter.  Unfortunately, you have not discovered the cake.  But hey, it's eternal, right?  That means it's still going to be around when you make it back from the outer galaxy.  Or, you could press q to quit. ")
     exit()

def volcano():
     invalidentry = True
     while invalidentry == True: 
          print("A chain of volcanoes lines the walls. The smoke makes it hard to see, and the floor appears to be lava.  Do not panic, mortal!  Instead, choose a door.  There are doors to the north, south, and west.")
          direction = input ("Which way do you go? ")
          direction=direction.lower ()
          if direction == "south":
               invalidentry= False
               rainbow()
          elif direction == "north":
               invalidentry = False
               jupiter()
          elif direction == "west":
               print ("There aren't stairs.  You fall into the moat, where an alligator will probably eat you. No cake, but q for quit.")
          elif direction == "q":
               invalidentry = False
               exit()
          else: 
               print ("I don't understand. Please try again. ")

#if choice west, "There aren't stairs.  You fall into the moat, where an alligator will probably eat you."
#if choice south, rainbow.
#if choice north, volcano.


def pterodactyls():
     print ("You get eaten by pterodactyls on the castle roof. Too bad. Press q to quit. ")
        

def exit():
    print("Thanks for playing. Please come find the Cake of Eternity again. ")
    sys.exit(0)

main()


