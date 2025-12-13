#Class attributes
class character:
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
        self.position = (0, 0)
        self.is_defending = False


#==========METHODS SECTION==========

    def run(self):
        if self.state_of_life == "Dead":
            print(f"{self.name} cannot run because it's dead!")
        elif self.stamina >= 15:
            self.stamina -= 15
            print(f"{self.name} is running! \n{self.name} stamina left: {self.stamina}")
        else:
            print(f"{self.name} is too tired to run!")
    
    def talk(self, message):
        if self.state_of_life == "Dead":
            print(f"{self.name} cannot talk because it's dead!")
        else:
            print(f"{self.name} says: {message}")
    
    def defend(self):
        if self.state_of_life == "Dead":
            print(f"{self.name} cannot defend because it's dead!")
        elif self.stamina >= 5:
            self.stamina -= 5
            self.is_defending = True
            print(f"{self.name} is defending! \n{self.name} stamina left: {self.stamina}")
        else:
            print(f"{self.name} is too tired to defend!")

    def attack(self, damage):
        if self.stamina >= 10:
            self.stamina -= 10
            print(f"{self.name} attacks and deals {damage} damage! \n{self.name} stamina left: {self.stamina}")
        elif self.state_of_life == "Dead":
            print(f"{self.name} cannot attack because it's dead!")
        else:
            print(f"{self.name} is too tired to attack!")

#Here are defined the attributes of each character
if __name__ == "__main__":
    guts = character("Guts", 24, "Dragonslayer", "Band of the Hawk", 100, 80, 50)
    griffith = character("Griffith", 22, "Sabre", "Band of the Hawk", 100, 70, 35)
    casca = character("Casca", 20, "Short Sword", "Band of the Hawk", 90, 70, 20)

#Example of method calls
casca.run()
guts.attack(guts.damage)
griffith.talk("For the glory of the Band of the Hawk!")