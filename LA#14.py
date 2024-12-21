LA#14

class Spiderman:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def describeSpiderman(self):
    print(f"{self.name} is {self.age} years old.")
    
class Tobey(Spiderman):
  def __init__(self, name, age, movietitle):
    super().init(name, age)
    self.movietitle = movietitle
    
class Andrew(Spiderman):
  def __init__(self, name, age, movietitle):
    super().init(name, age)
    self.movietitle = movietitle
    
class Tom(Spiderman):
  def __init__(self, name, age, movietitle):
    super().init(name, age)
    self.movietitle = movietitle

tobey = Tobey("Tobey", 39, "The Spider Man")

andrew = Andrew("Andrew", 55, "The Spider Man 2")

tom = Tom("Tom", 28, "The Spider Man 3")

print(tobey.name.upper(), tobey.movietitle)
print(andrew.name.upper(), andrew.movietitle)
print(tom.name.upper(), tom.movietitle)
