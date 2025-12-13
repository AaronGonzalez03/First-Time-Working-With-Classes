#First, the template for our character class (these are the CLASS ATTRIBUTES)
class character:
    name = "Default"
    age = 18
    weapon = "Sword"
    affiliation = "Band of the Hawk" 

#Now, we create INSTANCE ATTRIBUTES using the __init__ method
    def __init__(self, name, age, weapon, affiliation):
        self.name = name
        self.age = age
        self.weapon = weapon
        self.affiliation = affiliation

#Here are defined the attributes of each character
guts_attributes = character("guts_attributes", 24, "Dragonslayer", "Band of the Hawk")
griffith_attributes = character("griffith_attributes", 22, "Sabre", "Band of the Hawk")
casca_attributes = character("casca_attributes", 20, "Short Sword", "Band of the Hawk")

#Showing and displaying character attributes
print(f"Character Attributes: Name: {guts_attributes.name}, Age: {guts_attributes.age}, Weapon: {guts_attributes.weapon}, Affiliation: {guts_attributes.affiliation}")
print(f"Character Attributes: Name: {griffith_attributes.name}, Age: {griffith_attributes.age}, Weapon: {griffith_attributes.weapon}, Affiliation: {griffith_attributes.affiliation}")
print(f"Character Attributes: Name: {casca_attributes.name}, Age: {casca_attributes.age}, Weapon: {casca_attributes.weapon}, Affiliation: {casca_attributes.affiliation}")