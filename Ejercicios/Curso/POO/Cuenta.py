class Cuenta():

    def __init__(self, pro,sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Metodos getters
    def get_Saldo(self):
        return self.__saldo
    
    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda
    
    # Metodos setters
    def set_Saldo(self, saldo):
        self.__saldo = saldo
    
    def set_Propietario(self, propie):
        self.__propietario = propie

    def set_Moneda(self, moneda):
        self.__moneda = moneda

    


cuenta1 = Cuenta("Samuel Maldonado", 1000000, "Dolar")

print(cuenta1.get_Moneda())
print(cuenta1.get_Saldo())

cuenta1.set_Moneda("Peso Colombiano")
print(cuenta1.get_Moneda())