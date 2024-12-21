LA#21

class Sinigang:
    def __init__(self, pork, beans, sampaloc, tomato):
        self.__pork = pork
        self.__beans = beans
        self.__sampaloc = sampaloc
        self.__tomato = tomato
    def __str__(self):
        return f"My favorite food Sinigang has {self.__pork}, {self.__beans}, {self.__sampaloc}, and {self.__tomato}"
    def may_beans_ba(self):
       return self.__beans
    def i_set_to(self, bago):
        self.__beans = bago

sinigang = Sinigang("Pork", "Beans", "Sampaloc", "Tomato")
sinigang.i_set_to("Unti lang")
print(sinigang.may_beans_ba())
