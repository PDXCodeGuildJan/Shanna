

Monster
#the constant variable never changes
personality: str(const)

Hero
level: int

Creature

name: str
state: str(const)
health: int
attack_points: int
weapon: Weapon
special_abil: {Special.Ability}
stats: {}
max_health: int

attack(): int
heal(int): int
defend(int):
take_damage(int):
change_weapon(weapon)L Weapon
change_state(const): Bool
