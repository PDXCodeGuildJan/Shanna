"""This creates the class of MonsterHero, which is under the parent class of 
   Creature, and inherits from the subclasses Monster and Hero."""

from creature import Creature
from monster import Monster
from hero import Hero

class MonsterHero(Monster, Hero):

   def __init__(self):
      #passing the memory reference of self and calling monster initiation
      Monster.__init__(self)
      #passing the memory ref of self and calling hero initiation 
      Hero.__init__(self)
      
