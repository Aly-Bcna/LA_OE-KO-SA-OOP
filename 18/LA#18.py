LA#18

class Sinigang:
    def __init__(self, pork, beans, sampaloc, tomato):
        self.__pork = pork
        self.__beans = beans
        self.__sampaloc = sampaloc
        self.__tomato = tomato
    def __str__(self):
        return f"My favorite food Sinigang has {self.__pork}, {self.__beans}, {self.__sampaloc}, and {self.__tomato}"
   
sinigang = Sinigang("Pork", "Beans", "Sampaloc", "Tomato")

print(sinigang)
