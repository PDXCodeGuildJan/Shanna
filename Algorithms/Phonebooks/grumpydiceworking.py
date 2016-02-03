from random import randint


def start():
   """This is our welcome wagon, and prints a string with rules, and a prompt 
   for the user name."""

   print("Welcome to Grumpy Dice, the grumpiest game in the known universe.\n") 
   player = input("What is your name?")
   print ("Time to get your grump on, " + player + ".")


start()



pass
class Die:
   """Grumpy dice requires two of these objects."""

   def __init__(self):
      """This defines the dice object, to be used with the Game and Stage objects.
      The die instances contain values (ints) for current roll, boolean values
      indicating frozen/unfrozen state, and a list that describes appearance of 
      current die face."""

      self.curr_roll = 
      self.frozen = F
      self.die_face = 


   def roll_die(self):
      """When each die is rolled, a random int between 1 and 6 will be generated."""
      self.curr_roll1 = randint(1, 6)
      self.curr_roll2 = randint(1,6)
      

   def __str__(self):
      """This method overrides Python's built-in object memory address printing,
      instead printing a formatted die."""

"""
+-------+         +-------+       +-------+       +-------+       +-------+       +-------+
| o   o |         |       |       | o     |       | \   / |       | o   o |       | o   o |
|       |         |   o   |       |       |       | ^   ^ |       |   o   |       | o   o |
| o   o |         |       |       |     o |       | ----- |       | o   o |       | o   o |
+-------+"""      +-------+       +-------+       +-------+       +-------+       +-------+


class Stage:
   """Grumpy dice requires one of these objects."""

   def __init__(self):
      """This defines the Stage object, to be used with the Die and Game objects. 
      The Stage object contains integer values for current stage, a dictionary 
      containing stage goals (both level number and target numbers to match). In order
      to enable evaluation of freezable numbers at each stage, the Stage object also 
      contains a dictionary of values that can be frozen at every level.  The stage
      lockables are the same as the goals, except for level three, as rules of 
      the game do not permit freezing the int 6 on the third level."""

      self.curr_stage = 
      self.stage_goals = {1: 1,2, 2:3,4, 3:5,6}
      self.stage_freezables = {1:1,2, 2:3,4, 3:5}

  
   def update_stage(self, die_1, die_2):
      """When Game evaluates two die to be validly frozen, the stage is updated. 
      The stage is also updated whenever two grumpy faces are rolled.  Update 
      stage changes the current stage attributes: current stage, stage goals,   
      and stage freezables."""

   def check_freezable(self, die_1, die_2):
      """This method checks the values currently locked on the dice against the 
      stage freezable values.  If two valid freezes, update stage is activated."""
      

   def double_grump(self, die_1, die_2):
      """The int 3 is a grumpy number.  If both die rolls are currently 3, this
      is a double_grump situation (indicated by a Boolean). In this situation,
      update_stage resets to the initial values"""

class Game:
   """This class contains the playing information and methods for the game Grumpy Dice."""

   def __init__(self)
   """This defines the Game object for Grumpy Dice.  The Game object contains both 
   dice, and the stage object."""
   
   
   
   def roll_dice():
      """This method generates a random int between 1 and 6 for each rolled die object."""

   def prompt_for_lock():
      """This method takes a list, from somewhere, probably. The list is full of (ok, possibly full of?)
      information you need.  But since you don't know what it is or where it's coming from, good luck
      with this miserable function. Is this a list of the die-display-side?"""

   def validate_and_lock():
      """This method tries to lock the die at the roll specified by the player.  
      This method calls check_freezable in Stage."""

   def win():
     """This prints an ASCII cake, if that exists.  Because you won."""
      print "You've done it, you Crabby Appleton.  You're the grouchiest of all. Here's cake!\n"
           
         (.)
         .|.
         l8J
         | |
     _.--| |--._
  .-';  ;`-'& ; `&.
 & &  ;  &   ; ;   \
 \      ;    &   &_/
  F"""---...---"""J
  | | | | | | | | |
  J | | | | | | | F
   `---.|.|.|.---'



   
  
      
   

 
