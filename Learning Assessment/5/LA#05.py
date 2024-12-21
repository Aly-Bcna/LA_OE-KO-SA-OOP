LA#05

class Mlhero():
   def __init__(self, name, role):
   self.name = name
   self.role = role

   def describe(self):
     print(f"{self.name} is a/an {self.role} hero.")
     
support = Mlhero("Angela", "support")
marksman = Mlhero("Miya", "Marksman:)

support.describe()
marksman.describe()
