






die_1: die
die_2: die
curr_stage: int
stage.goals: {}

def start_game():
   """This function welcomes player and displays the rules for play."""
   print welcome
   
   take and remember name of player
      

__init__ make dice thing
    """This initializes the two six-sided dice needed for the game."""
   use class to make two dice

def update_stage():
   """This function thaws frozen die, and is passed an int representative of game stage
      and calls the roll die methods"""
   unfreeze die (reset lock to = false)
   update curr_stage variable 


def roll_dice():
   """This function evaluates dice for frozen/unfrozen attributes and produces a
   random number between 1 and 6 for each die roll. Roll is a method in die class."""
    dice frozen? no?
      roll die 1 
      roll die 2
   one locked?
      return (die_1, die_2) #these will be instances of class die, wrapped in a tuple
                            #that contains the current roll, locked/unlocked status
                            #and these dice will persist for the duration of the program
      roll unlocked die
  
   #curr_roll is the numerical value btwn 1-6, generated randomly for each die roll.
   #This return is incorrect, because this information is contained inside the die objs.
   return curr_roll_1
          curr_roll_2
    
def double_grump():
   """This function evaluates die rolls for double-grump status.  Double-grumps
   restart the game at the initial state."""
   curr_roll_1 and curr_roll_2 == 3?
      if True
      initial state()
   curr_rolls != 3?

def prompt_for_lock(die_1, die_2):
   """This function allows the player to lock either die, which is actually a method 
   built into the die class, so I'm not sure what it looks like. This function evaluates
   the validity of locked dice, and controls the flow of the game accordingly.  Dice 
   must be locked in order to win."""
   press 1 to lock die_1
   press 2 to lock die_2
 


def validate_lock():
   """This function accesses the global stage variable and compares it against
the locked curr_roll/s.  If lock state is valid, the unlocked die may be rerolled.
If two valid locks, the function increments the update_stage variable, unless it
is stage 3, and then two valid locks indicates a number."""
  press spacebar to roll again
      if locked?

      lock valid?
         one valid
         die_1.roll_die() #this is calling die's built-in method
         two valid?
            if stage 1-2:  
               update_stage()
            if stage 3:
               you_win()



   return 
         
   
   
   
   
  
   
