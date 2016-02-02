from random import randint


def main():
   """This is our welcome wagon, and prints a string with rules, and a prompt 
   for the user name."""

   print("Welcome to Grumpy Dice, the grumpiest game in the known universe.\n") 
   player = input("What is your name, O Grouchy One?")
   print ("Time to get your grump on, " + player + ".")


   # Test  AREA!!
   new_game = Game()
   new_game.start()
   new_game.doublegrump()
   
   
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
      if self.frozen == False:         
         self.curr_roll = randint(1, 6)

#have it check itself to see if it's locked.  if it is, it won't roll. if it's not, it will roll.

   def __str__(self):
      """This method overrides Python's built-in object memory address printing,
      instead printing a formatted die."""

      return self.die_faces[self.curr_roll]



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
      """When Game evaluates two die to be validly frozen, the stage is updated. 
      Update stage changes the current stage attributes: current stage, stage goals,   
      and stage freezables."""

    
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

   def start(self):
      """This begins a new game."""
      self.roll_dice()
      self.stage.double_grump(self.die_1, self.die_2)
      self.prompt_freeze()
      
  #see if you can work this into a part of the die class, so that the die knows not to roll itself if it's frozen       
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
      option = input
      #menu of player choices
      while option != "e":
         option = input("(e)xit\n(r)oll\n1 to freeze die 1\n2 to freeze die 2\n(f)reeze both\n(t)haw both  \n").lower()
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
         elif option == "t":
            die.frozen = False
         else:
            print("press e to exit, r to roll, 1 to freeze die 1, 2 to freeze die 2\n")
      
   def freeze(self, frozen_dice):
      """This method freezes the die at the roll specified by the player, and then 
         checks the dictionary of stage values in Stage to see if the lock is valid."""
      for die in frozen_dice:
      #if the die's current roll value appears in the dict of valid freezables
         if die.curr_roll in self.stage.stage_freezables :
            die.frozen = True
      #in an if statement, you don't need the =True, it's assumed
      if self.die_1.frozen and self.die_2.frozen and self.stage.curr_stage < 3:
            update_stage()
           
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

      print(cake + "\nYou're the grumpiest of all, Crabby Appleton. Here's a cake.")


   
  
if __name__ == "__main__":
   main()
   

 
