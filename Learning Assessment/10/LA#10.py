LA#10

class Vehicle:
  def __init__(self, brand, model, fuel_type):
  self.brand = brand
  self.model = model
  self.fuel_type = fuel_type

  def describeVehicle(self):
    print(f"{self.brand} is a {self.model} with a {self.fuel_type} fuel type")
    
class Car(Vehicle):
pass
bmw = Car("BMW", "ghgh", "Premium")
bmw.describeVehicle()
class Motorcycle(Vehicle):
pass
yamaha = Motorcycle("Yamaha", "XSR", "Premium")
yamaha.describeVehicle()
