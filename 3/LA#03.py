LA#03

class Mlhero():
   def __init__(self, name, role):
   self.name = name
   self.role = role
  
   def describe(self):
    return f"{self.name} is a/an {self.role} hero."
     
support = Mlhero("Angela", "Support")
marksman = Mlhero("Miya", "Marksman")

print(support.name)
print(support.role)
print(support.describe())
print(marksman.name)
print(marksman.role)
print(marksman.describe())
