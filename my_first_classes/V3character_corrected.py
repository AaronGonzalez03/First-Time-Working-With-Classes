#Class attributes
class character_attributes:
    total_characters = 0
    universe = "Berserk"
    species = "Human"

#Now, we create INSTANCE ATTRIBUTES using the __init__ method
    def __init__(self, name, age, weapon, affiliation, health, stamina, damage):
        self.name = name
        self.age = age
        self.weapon = weapon
        self.affiliation = affiliation
        self.health = health
        self.stamina = stamina
        self.damage = damage
        if self.health > 0:
            self.state_of_life = "Alive"
        else:
            self.state_of_life = "Dead"
        self.position = 0
        self.is_defending = False

        character_attributes.total_characters += 1

#==========METHODS SECTION==========

    def walk(self):
        print(f"{self.name} is walking")
    
    def run(self):
        print(f"{self.name} is running")
    
    def talk(self, message):
        print(f"{self.name} says: {message}")
    
    def attack(self):
        print(f"{self.name} attacks with {self.weapon}")
    
    def defend(self):
        print(f"{self.name} defends with {self.weapon}")

    def attack(self, damage):
        if self.stamina >= 10:
            self.stamina -= 10
            print(f"{self.name} attacks and deals {damage} damage!")
        elif self.state_of_life == "Dead":
            print(f"{self.name} cannot attack because it's dead!")
        else:
            print(f"{self.name} is too tired to attack!")

#Here are defined the attributes of each character
guts_attributes = character_attributes("Guts", 24, "Dragonslayer", "Band of the Hawk", 100, 80, 50)
griffith_attributes = character_attributes("Griffith", 22, "Sabre", "Band of the Hawk", 100, 70, 35)
casca_attributes = character_attributes("Casca", 20, "Short Sword", "Band of the Hawk", 90, 70, 20)