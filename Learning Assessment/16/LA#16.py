LA#16

class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
    def operate(self):
        print("Operating!")
    def info(self):
        print("Brand: {self.brand} Model: {self.model}")
       
class WashingMachine(Appliance):
    def operate(self):
        print("Washing Clothes")
class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold")    
class Microwave(Appliance):
    def operate(self):
        print("Heating food")
       
washingmachine = WashingMachine("Toshiba", "VH")
refrigerator = Refrigerator("LG", "hshs")
microwave = Microwave("Sharp", "dsds")


for Appliance in [WashingMachine, Refrigerator, Microwave]:
    Appliance.operate()
    Appliance.info()
