LA#13

class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def describeAnimal(self):
    print(f"{self.name} is a {self.type} that can swim")
    
class Fish(Animal):
  def __init__(self, name, type):
    super().init(name, type)
    self.can_swim = True

mackerel = Fish("Tilapia", "Garfish")
print(mackerel.can_swim)
