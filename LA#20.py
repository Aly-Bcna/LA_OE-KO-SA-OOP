LA#20

class Sinigang:
    def __init__(self, pork, beans, sampaloc, tomato):
        self.__pork = pork
        self.__beans = beans
        self.__sampaloc = sampaloc
        self.__tomato = tomato
    def __str__(self):
        return f"My favorite food Sinigang has {self.__pork}, {self.__beans}, {self.__sampaloc}, and {self.__tomato}"
    def may_beans_ba(self, age):
        if age >= 12:
            return self.__beans
        else:
            return "Secret"
    def i_set_to(self, bago, nanay_ka_ba):
        if nanay_ka_ba == "oo":
            self.__beans = bago
        else:
            print("Bawal")

sinigang = Sinigang("Pork", "Beans", "Sampaloc", "Tomato")
sinigang.i_set_to("Buong Beans", "oo")
print(sinigang.may_beans_ba(31))
