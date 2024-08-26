import math


class TarjetaDeCredito:

    def __init__(self, nombre, numero_tarjeta, limite, balance):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta
        self.limite = limite
        self.balance = balance

    def comprar(self, monto):

        if (self.balance + monto) <= self.limite:
            self.balance = self.balance + monto
        else:
            raise ValueError(
                f"No es posible gastar {monto} con un balance de {self.balance}"
            )

    def depositar(self, monto):
        if monto > self.balance:
            raise ValueError(f"El monto {monto} excede el balance {self.balance}")
        else:
            self.balance = self.balance - monto

    def reporte(self):
        return (
            f"El cliente {self.nombre} con tarjeta {self.numero_tarjeta}"
            f" tiene un balance de {self.balance} "
            f"y un limite de {self.limite}"
        )


class Vector:

    def __init__(self, dimension) -> None:
        self.dimension = dimension
        self.datos = [0 for _ in range(dimension)]

    def representar(self):
        return "(" + ",".join([str(dato) for dato in self.datos]) + ")"

    def obtener_elemento(self, indice):
        return self.datos[indice]

    def asignar_elemento(self, indice, valor):
        if indice < 0 or indice >= self.dimension:
            raise ValueError("Indice incorrecto!")
        self.datos[indice] = valor

    def sumar(self, otro_vector):
        if self.dimension != otro_vector.dimension:
            raise ValueError("Las dimensiones son diferentes")

        resultado = Vector(self.dimension)

        for indice in range(self.dimension):
            resultado.asignar_elemento(
                indice,
                self.obtener_elemento(indice) + otro_vector.obtener_elemento(indice),
            )

        return resultado

    def es_igual(self, otro_vector):
        if self.dimension != otro_vector.dimension:
            return False

        for indice in range(self.dimension):
            if self.obtener_elemento(indice) != otro_vector.obtener_elemento(indice):
                return False
        return True

    def producto_escalar(self, otro_vector):
        if self.dimension != otro_vector.dimension:
            raise ValueError("Las dimensiones son diferentes!")

        resultado = 0
        for indice in range(self.dimension):
            resultado = resultado + self.obtener_elemento(
                indice
            ) * otro_vector.obtener_elemento(indice)

        return resultado

    def distancia_coseno(self, otro_vector):
        numerador = self.producto_escalar(otro_vector)
        denominador = math.sqrt(self.producto_escalar(self)) * math.sqrt(
            otro_vector.producto_escalar(otro_vector)
        )

        return numerador / denominador
