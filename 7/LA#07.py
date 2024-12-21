LA#07

class Car:
  def __init__(self, brand, color):
  self.brand = brand
  self.color = color

kotse = Car("Vios", "Red")
kotse2 = Car("Jimmy", "Black")

print(kotse.brand, kotse2.color)
kotse.color = "Yellow"
print(kotse2.brand, kotse.color)

print(kotse.brand, kotse2.color)
print(kotse2.brand, kotse.color)
