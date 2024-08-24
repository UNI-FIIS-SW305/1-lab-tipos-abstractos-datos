class TarjetaDeCredito:
    
    def __init__(self,nombre, numero_tarjeta, limite, balance ):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta
        self.limite = limite
        self.balance = balance

    def comprar(self, monto):

        if (self.balance + monto) <= self.limite:
            self.balance = self.balance + monto 
        else:
            raise ValueError(f"No es posible gastar {monto} con un balance de {self.balance}")
        
    def depositar(self, monto):
        if monto > self.balance:
            raise ValueError(f"El monto {monto} excede el balance {self.balance}")
        else:
            self.balance = self.balance - monto

    def reporte(self):
        return (f"El cliente {self.nombre} con tarjeta {self.numero_tarjeta} tiene un balance de {self.balance} "
                f"y un limite de {self.limite}")
