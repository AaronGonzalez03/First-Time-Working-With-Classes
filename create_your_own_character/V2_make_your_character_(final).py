print("=======================================")
print("Welcome to the Character Creation Menu")
print("=======================================")

class character:
    
    def __init__(self, name, age, type_of_warrior, weapon, health, stamina, damage):
        self.name = name
        self.age = age
        self.type_of_warrior = type_of_warrior
        self.weapon = weapon
        self.health = health
        self.stamina = stamina
        self.damage = damage
        if self.health > 0:
            self.state_of_life = "Alive"
        else:
            self.state_of_life = "Dead"
        self.position = (0, 0)
        self.is_defending = False
        

types_of_warriors = ["Swordsman", "Archer", "Mage", "Real Fighter"]
    
swordsman_weapons = ["Sword", "Longsword", "Katana"]
archer_weapons = ["Bow", "Crossbow", "Longbow"]
mage_weapons = ["Staff", "Wand", "Orb"]

character_name = input("Enter your character's name: ").title()
character_age = int(input("Enter your character's age: "))


while True:
    character_type_of_warrior = input(f"Choose your warrior type: \nAvaible warriors: {types_of_warriors}: ").title()
    if character_type_of_warrior in types_of_warriors:
        break
    else:
        print("Invalid warrior type. Please try again.")

character_weapon = ""
if character_type_of_warrior == "Swordsman":
    while True:
        character_weapon = input(f"Choose your weapon: \n{swordsman_weapons}: ").title()
        if character_weapon in swordsman_weapons:
            break
        else:
            print("Invalid weapon. Please try again.")
elif character_type_of_warrior == "Archer":
    while True:
        character_weapon = input(f"Choose your weapon: \n{archer_weapons}: ").title()
        if character_weapon in archer_weapons:
            break
        else:
            print("Invalid weapon. Please try again.")
elif character_type_of_warrior == "Mage":
    while True:
        character_weapon = input(f"Choose your weapon: \n{mage_weapons}: ").title()
        if character_weapon in mage_weapons:
            break
        else:
            print("Invalid weapon. Please try again.")
else:
    character_weapon = "Hands"

character_health = 100
character_stamina = 100
character_damage = 10

user_character = character(character_name, character_age, character_type_of_warrior, character_weapon, character_health,
                           character_stamina, character_damage)

print(f"Character Created! \n{character_name}, now you can start your adventure as a {character_type_of_warrior}")
while True:
    see_stats = input("Do you want to see your character's stats? (Yes/No): ").title()
    if see_stats == "Yes":
        print(f"Name: {user_character.name}\nAge: {user_character.age}\nType of Warrior: {user_character.type_of_warrior}\n"
            f"Weapon: {user_character.weapon}\nHealth: {user_character.health}\nStamina: {user_character.stamina}\n"
            f"Damage: {user_character.damage}\nState of Life: {user_character.state_of_life}")
        break
    elif see_stats == "No":
        print("Good luck on your adventure!")
        break
    else:
        print("Invalid input. Please enter Yes or No.")