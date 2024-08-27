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

    def similitud_coseno(self, otro_vector):
        numerador = self.producto_escalar(otro_vector)
        denominador = math.sqrt(self.producto_escalar(self)) * math.sqrt(
            otro_vector.producto_escalar(otro_vector)
        )

        return numerador / denominador


class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def obtener_grado(self):
        return len(self.coeficientes) - 1

    def obtener_coeficiente(self, exponente):
        if exponente < 0 or exponente > self.obtener_grado():
            raise ValueError("Coeficiente inválido")

        return self.coeficientes[exponente]

    def modificar_coeficiente(self, exponente, coeficiente):

        if exponente < 0 or exponente > self.obtener_grado():
            raise ValueError("Coeficiente inválido")

        self.coeficientes[exponente] = coeficiente

    def evaluar(self, valor):
        resultado = 0

        for exponente, coeficiente in enumerate(self.coeficientes):
            resultado = resultado + coeficiente * (valor**exponente)

        return resultado

    def sumar(self, otro_polinomio):

        mis_coeficientes = self.coeficientes
        otros_coeficientes = otro_polinomio.coeficientes

        if self.obtener_grado() < otro_polinomio.obtener_grado():
            mis_coeficientes = mis_coeficientes + [0] * (
                otro_polinomio.obtener_grado() - self.obtener_grado()
            )
        elif self.obtener_grado() > otro_polinomio.obtener_grado():
            otros_coeficientes = otros_coeficientes + [0] * (
                self.obtener_grado() - otro_polinomio.obtener_grado()
            )

        coeficientes = [
            coeficiente + otro_coeficiente
            for coeficiente, otro_coeficiente in zip(
                mis_coeficientes, otros_coeficientes
            )
        ]

        return Polinomio(coeficientes=coeficientes)


class Rango:

    def __init__(self, inicio, limite, distancia=1) -> None:
        if distancia == 0:
            raise ValueError("La distancia no puede ser cero.")

        self.inicio = inicio
        self.limite = limite
        self.distancia = distancia

    def numero_elementos(self):
        rango_a_recorrer = self.limite - self.inicio
        return rango_a_recorrer // self.distancia

    def obtener_elemento(self, indice):
        if indice < 0 or indice >= self.numero_elementos():
            raise ValueError("Indice invalido")

        return self.inicio + self.distancia * indice

    def representar(self):
        elementos = []
        indice = 0
        while len(elementos) < self.numero_elementos():
            elementos.append(str(self.obtener_elemento(indice)))
            indice = indice + 1

        return ",".join(elementos)

    def sumar(self):
        resultado = 0
        indice = 0
        while indice < self.numero_elementos():
            resultado = resultado + self.obtener_elemento(indice)
            indice = indice + 1

        return resultado
