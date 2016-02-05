#this imports our creature properties and methods from creatures.py
from creature import Creature

"""Defines the Monster class, which inherits from Creature class in our game."""

class Monster(Creature):

   AGRO = "aggressive"
   DEFENSE = "defensive"
   
   def __init__(self):
      #super is a builtin python variable that represents the parent class of
      #this object (parent class = Creature here). This makes a monster inside  
      #the parent class of creature, with all the properties of creature. 

      super(Monster, self).__init__()
      
      self.personality = Monster.AGRO
   
  
