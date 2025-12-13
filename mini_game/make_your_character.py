class your_character:
    
    def __init__(self, name, age, type_of_warrior, weapon, affiliation, health, stamina, damage):
        self.name = name
        self.age = age
        self.type_of_warrior = type_of_warrior
        self.weapon = weapon
        self.affiliation = affiliation
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

character = your_character(input("Enter your character's name: "), int(input("Enter your character's age: ")), input(f"Enter your type of warrior: \nType of warriors available: \n{types_of_warriors}"),
                           if self.type_of_warrior == "Swordsman": 
                            input(f"Choose your weapon: \nAvailable weapons: \n{swordsman_weapons}"),
                           elif self.type_of_warrior == "Archer": 
                            input(f"Choose your weapon: \nAvailable weapons: \n{archer_weapons}"),
                           elif self.type_of_warrior == "Mage": 
                            input(f"Choose your weapon: \nAvailable weapons: \n{mage_weapons}"),
                           else:
                             print("Select a valid character"), 100, 100, 10)

#I was investing bout the errors and I found why this doesn't work, to see the correction and upgrade, go to "make_your_charecter_V2.py"
#I like to learn with my mistakes :) Thatas why I leave this version right here