LA#12

class Toy:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def describeToy(self):
    print(f"{self.name} is {self.price} pesos.")
    
class Car(Toy):
  def __init__(self, name, price):
    super().init(name, price)

lamborghini = Car("Lamborghini", 1200)
lamborghini.describeToy()
