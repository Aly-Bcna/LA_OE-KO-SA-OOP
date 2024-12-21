LA#06

class Laptop:
  def init(self, brand, model):
  pass
  def laptop_info(self):
  pass

lenovo = laptop("Lenovo", "ideapad")

print(lenovo.laptop_info())

class course:
  def init(self, name):
  self.name = name

it = course("Information Technology")
cs = course("Computer Science")

print(it.name)
it.name = "BSIT"
print(it.name)
