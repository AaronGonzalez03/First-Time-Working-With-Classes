#Before nothing, aclear that this version of the code is with to many errors. 
#I let them because I want to see my progress and intentions.


#Class attributes
class character_attributes:
    universe = "Berserk"
    species = "Human"

#Now, we create INSTANCE ATTRIBUTES using the __init__ method
    def __init__(self, name, age, weapon, affiliation):
        self.name = name
        self.age = age
        self.weapon = weapon
        self.affiliation = affiliation

#Here are defined the attributes of each character
guts_attributes = character_attributes("Guts", 24, "Dragonslayer", "Band of the Hawk")
griffith_attributes = character_attributes("Griffith", 22, "Sabre", "Band of the Hawk")
casca_attributes = character_attributes("Casca", 20, "Short Sword", "Band of the Hawk")


#Class methods 
class character_methods:
    attack = "Slash"
    talk = "Speak"
    defend = "Block"
    walk = "Move"

#Here we are creating the instance methods
    def __init__(self, attack, talk, defend, damage, health, state_of_life, stamina):
        self.attack = attack
        self.talk = talk
        self.defend = defend
        self.damage = damage
        self.health = health
        self.state_of_life = state_of_life
        self.stamina = stamina

#Here are defined the methods of each character
guts_methods = character_methods("Heavy Slash", "Rough Speak", "Strong Block", 90, 100, "Alive", 80)
griffith_methods = character_methods("Quick Slash", "Persuasive Speak", "Agile Block", 70, 90, "Alive", 90)
casca_methods = character_methods("Swift Strike", "Calm Speak", "Defensive Block", 60, 80, "Alive", 85) 

#It's time to create the final result of the characters
guts = guts_attributes + guts_methods             
griffith = griffith_attributes + griffith_methods 
casca = casca_attributes + casca_methods          