"""This creates our hero class, which inherits from creature."""
from creature import Creature


class Hero(Creature):
    
   def __init__(self):

      super(Hero, self).__init__()
      self.level = 1
       
      
