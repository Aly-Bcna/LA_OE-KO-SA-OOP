LA#22

class My_bday:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food
    def __foods(self):
        print(f"Theme of the party is {self.theme}")
        print(f"The Special Dish is {self.food}")
    def party(self):
        print("Our Foods: Kaldereta, Letchon, Lumpia")
        self.__foods()
       
theme = My_bday("Enchanted", "Spaghetti")
theme.party()
print("____________________________________")
theme = My_bday("Holloween","Chocolate Cake")
theme.party()
print("___________________________________")
theme = My_bday("Carnival", "Menudo")
theme.party()
#LA23
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def wrapper_mthd(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper_mthd
       
character = AnimeCharacter("Yuji Itadori", "Megumi Fushiguro")

@character.introduce
def character_intro(name, ability):
    print(f"I am {name} and I can use {ability}.")
   
character_intro("Gojo Saturo","Cursed Technique")
