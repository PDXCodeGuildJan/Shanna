"""This is a game of grumpy dice.  Roll the dice, choose which numbers to freeze,
    and try to match the numbers needed for the level. If you match and freeze your 
   dice at those numbers, you advance.  But careful! If you roll two grumpy dice,
   it's back to the beginning for you."""

__author__= "Shanna Louise"
from random import randint

def main():
   """This is our welcome wagon, and prints a string with rules, and a prompt 
   for the user name."""
   #this is the code version of the flow chart.  Call each function in order.
   
   # Make a new instance of the game
   new_game = Game()
   # Start up our new game
   new_game.start()


class Game:
   """This class contains the playing information and methods for the game Grumpy Dice."""

   def __init__(self):
      """This defines the Game object for Grumpy Dice.  The Game object contains both 
      dice, and the stage object."""
      #names and creates Dice for the game
      self.die_1 = Die()
      self.die_2 = Die()
      #names and creates Stage for the game
      self.stage = Stage()
      # have the player's name
      self.player = ""

   def start(self):
      """This begins a new game."""
      print("Welcome to Grumpy Dice, the grumpiest game in the known universe.\n") 
      self.player = input("What is your name, O Grouchy One?")
      print ("Time to get your grump on, " + self.player + ".")

      self.play_game()

   def play_game(self):
      """Play the game Angry Dice, until they win."""

      # This is where we implement our beautiful flow chart

      won = False
      print("The while loop should start right now.")
      while not won:

         # Roll Dice
         print("This should roll the dice.")
         self.roll_dice()
         
         # Evaluate the rolled values of the dice
         print("This should evaluate for doublegrump.")
         angry = self.stage.double_grump(self.die_1, self.die_2)

         # If the user isn't angry, see if they passed the round
         print("If the dice aren't angry, this checks to see if they passed the round.")
         if not angry:
            # See if they advance to the next stage
            new_stage = self.stage.update_stage(self.die_1, self.die_2)
         
         # If they haven't advanced, prompt them to freeze dice
         print("If not new stage, ask what dice to freeze")
         print(new_stage)

         if not new_stage:
            # Ask them what they want to hold
            self.prompt_freeze()
         # See if the new stage they are on means they won!      
         else: 
            if self.stage.curr_stage == 4:
               # THEY'VE WON!!!
               self.win()
               won = True


   ###### FEB 2 IS THIS REDUNDANT?
  #see if you can work this into a part of the die class, so that the die knows not to roll itself if it's frozen .
  #check down in roll and see if you can eliminate the redundancy in the die attributes      
   def roll_dice(self):
      """This method generates a random int between 1 and 6 for each rolled die object."""
      #If die_1 isn't locked, roll
      if self.die_1.frozen == False:
         #This updates the stored value for curr_roll back up in dice object's method roll
         self.die_1.roll()
      #if die_2 isn't locked, roll
      if self.die_2.frozen == False:
         self.die_2.roll()
      #display both dice
      print (self.die_1)
      print(self.die_2)

   def prompt_freeze(self):
      """This method displays a menu of play options, and allows the player to 
         freeze dice, if desired."""
      option = ""

      # Thaws all the dice before we ask what they want to freeze
      self.die_1.frozen, self.die_2.frozen = False, False

      #menu of player choices
      while option != "e":
         option = input("(e)xit\n(r)oll\n1 to freeze die 1\n2 to freeze die 2\n(f)reeze both\n").lower()
         #press r to roll again
         if option == "r":
            self.roll_dice()
         #player press 1 to lock die_1
         elif option == "1":
            self.freeze([self.die_1])
         #press 2 to lock die_2
         elif option == "2":
            self.freeze([self.die_2])
         #press b to freeze both
         elif option == "f":
            self.freeze([self.die_1, self.die_2])
         #press e to exit
         elif option == "e":
            exit()
         else:
            print("press e to exit, r to roll, 1 to freeze die 1, 2 to freeze die 2\n")
      
   def freeze(self, frozen_dice):
      """This method freezes the die at the roll specified by the player, and then 
         checks the dictionary of stage values in Stage to see if the lock is valid."""

      for die in frozen_dice:
      #if the die's current roll value appears in the dict of valid freezables
         if die.curr_roll in self.stage.stage_freezables[self.stage.curr_stage]:
            die.frozen = True
         
      #in an if statement, you don't need the =True, it's assumed
         if self.die_1.frozen and self.die_2.frozen and self.stage.curr_stage < 3:
            print("Ahh! You accidentally froze everything when you shouldn't have!! Let me help..")
            print("Unfreezing Die 1 for you.")
            self.die_1.frozen = False

####  HONEY, THERE'S A BUG HERE AND IT ALWAYS PRINTS THIS AND YOU'LL FIGURE IT OUT SOON
         else: 
            print("NOPE. Press r to roll again.")
      
   def win(self):
      """This prints an ASCII cake, if that exists.  Because you won."""
      
      
           
      cake = """
         (.)
         .|.
         l8J
         | |
     _.--| |--._
  .-';  ;`-'& ; `&.
 & &  ;  &   ; ;   \\
 \\      ;    &   &_/
  F'''---...---'''J
  | | | | | | | | |
  J | | | | | | | F
   `---.|.|.|.---"""

      print(cake + "\nYou're the grumpiest of all, you Crabby Appleton". self.player," here's a cake.  The cake is not a lie")



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

      self.curr_stage = 1
      self.stage_goals = {1:[1,2], 2:[3,4], 3:[5,6]}
      self.stage_freezables = {1:[1,2], 2:[3,4], 3:[5]}
   
  
   def update_stage(self, die_1, die_2):
      """When both dice display the target numbers for the level, the stage is updated. 
      Update stage evaluates two dice, and changes the current stage if
      they've completed it."""

      # see if the dice are what they should be for the current stage
######can that be written if self.die_1.curr_roll, self.die_2.curr_roll in self.stage_freeables[self.stage.curr_round]??
      if die_1.curr_roll in self.stage_freezables[self.curr_stage] and die_2.curr_roll in self.stage_freezables[self.curr_stage]:
      # if they are, update the stage to the next one and return True
            self.curr_stage += self.curr_stage
            print("I'm updating the stage.") 
      # Otherwise, return False
      else:
         return False

    
   def double_grump(self, die_1, die_2):
      """The int 3 is a grumpy number.  If both die rolls are currently 3, this
      is a double_grump situation (indicated by a Boolean). In this situation,
      update_stage resets to the initial values"""
      #is die value the grumpy one? 
      if die_1.curr_roll == 3 and die_2.curr_roll == 3:
      #print a sorry-you message 
         oscar = """
                ____ 
    ___________//__\\__________
   /___________________________\\
   I___I___I___I___I___I___I___I
         < ,wWWWWwwWWWWw, >
        <  WW( 0 )( 0 )WW  >
       <      '-'  '-'      >
      <    ,._.--""--._.,    >
      <   ' \   .--.   / `   >
       <     './__\\_\\.'   >
     ___<.-.____________.-.>___
    (___/   \\_________/   \\___)
     |  \,_,/          \,_,/  |
   .-|/^\\ /^\\ /^\\ /^\\ /^\\|-.
  / (|\\| | | | | | | | | | /\\|)\\
  '.___/| | | | | | | | | | \___.'
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     || | | | | | | | | | | | |
     `''''''''''''''''''''''''`"""
         print(oscar + "\nTake your double grump and get outta here!")
         #reset game values to initial state
         self.curr_stage = 1
         return True
      else:
         return False
   
   
class Die:
   """Grumpy dice requires two of these objects."""

   def __init__(self):
      """This defines the dice object, to be used with the Game and Stage objects.
      The die instances contain values (ints) for current roll, boolean values
      indicating frozen/unfrozen state, and a list that describes appearance of 
      current die face."""

      self.curr_roll = 1
      self.frozen = False
      self.die_faces = {
1: """
+-------+
|       |
|   o   |
|       |
+-------+""",
2: """
+-------+
|     o |
|       |
| o     |
+-------+""",
3: """
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",
4: """
+-------+
| o   o |
|       |
| o   o |
+-------+""",
5: """
+-------+
| o   o |
|   o   |
| o   o |
+-------+""",
6: """
+-------+
| o   o |
| o   o |
| o   o |
+-------+"""

}


   def roll(self):
      """When die is rolled, a random int between 1 and 6 will be generated."""
      if not self.frozen:         
         self.curr_roll = randint(1, 6)

   #have it check itself to see if it's locked.  if it is, it won't roll. if it's not, it will roll.

   def __str__(self):
      """This method overrides Python's built-in object memory address printing,
      instead printing a formatted die."""

      return self.die_faces[self.curr_roll]
  
if __name__ == "__main__":
   main()
   

 
