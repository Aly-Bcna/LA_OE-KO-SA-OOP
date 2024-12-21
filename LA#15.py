LA#15

class Dog:
    def __init__(self, name):
        self.name = name
       
    def speak(self):
         print(f"{self.name} bark")
       
class Cat:
    def __init__(self, name):
        self.name = name
       
    def speak(self):
         print(f"{self.name} meow")
       
class Bird:
    def __init__(self, name):
        self.name = name
       
    def speak(self):
        print(f"{self.name} chirp")
       

dog = Dog("aso")  
cat = Cat("pusa")
bird = Bird("ibon")

def animal_sound(animal):
    print(animal.speak())
   
animal_sound(dog)
animal_sound(cat)
animal_sound(bird)

for animal in [dog, cat, bird]:
    print(animal.speak()) 
