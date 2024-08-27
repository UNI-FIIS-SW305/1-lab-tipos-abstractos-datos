import laboratorio
import pytest


def tarjeta_de_prueba() -> laboratorio.TarjetaDeCredito:
    return laboratorio.TarjetaDeCredito(
        nombre="Lolo Fernandez", numero_tarjeta="123456", limite=100, balance=20
    )


def test_crear_tarjeta():
    tarjeta: laboratorio.TarjetaDeCredito = tarjeta_de_prueba()

    assert tarjeta.nombre == "Lolo Fernandez"
    assert tarjeta.numero_tarjeta == "123456"
    assert tarjeta.limite == 100
    assert tarjeta.balance == 20


def test_comprar_con_tarjeta():
    tarjeta: laboratorio.TarjetaDeCredito = tarjeta_de_prueba()

    tarjeta.comprar(30)
    assert tarjeta.balance == 50

    tarjeta.comprar(50)
    assert tarjeta.balance == 100

    with pytest.raises(ValueError):
        tarjeta.comprar(1)

    with pytest.raises(ValueError):
        tarjeta.depositar(101)

    tarjeta.depositar(10)
    assert tarjeta.balance == 90

    tarjeta.depositar(90)
    assert tarjeta.balance == 0

    assert tarjeta.reporte() == (
        "El cliente Lolo Fernandez con tarjeta 123456"
        " tiene un balance de 0 y un limite de 100"
    )


def test_crear_vector() -> None:
    vector: laboratorio.Vector = laboratorio.Vector(3)

    assert vector.dimension == 3
    assert vector.representar() == "(0,0,0)"
    assert vector.obtener_elemento(2) == 0

    vector.asignar_elemento(2, 2)
    assert vector.obtener_elemento(2) == 2

    otro_vector: laboratorio.Vector = laboratorio.Vector(3)
    otro_vector.asignar_elemento(0, 1)
    otro_vector.asignar_elemento(1, 2)
    otro_vector.asignar_elemento(2, 3)

    with pytest.raises(ValueError):
        otro_vector.asignar_elemento(-1, -1)

    with pytest.raises(ValueError):
        otro_vector.asignar_elemento(3, 4)

    with pytest.raises(ValueError):
        vector.sumar(laboratorio.Vector(2))

    assert not vector.es_igual(laboratorio.Vector(1))

    resultado: laboratorio.Vector = vector.sumar(otro_vector)
    assert resultado.obtener_elemento(0) == 1
    assert resultado.obtener_elemento(1) == 2
    assert resultado.obtener_elemento(2) == 5

    assert not resultado.es_igual(otro_vector)

    vector_copia = laboratorio.Vector(3)
    vector_copia.asignar_elemento(0, 0)
    vector_copia.asignar_elemento(1, 0)
    vector_copia.asignar_elemento(2, 2)

    assert vector_copia.es_igual(vector)

    factor = laboratorio.Vector(2)
    factor.asignar_elemento(0, 3)
    factor.asignar_elemento(1, 0)

    otro_factor = laboratorio.Vector(2)
    otro_factor.asignar_elemento(0, 5)
    otro_factor.asignar_elemento(1, 5)

    assert factor.producto_escalar(otro_factor) == 15

    with pytest.raises(ValueError):
        factor.producto_escalar(vector_copia)

    factor = laboratorio.Vector(4)
    factor.asignar_elemento(0, 3)
    factor.asignar_elemento(1, 2)
    factor.asignar_elemento(2, 0)
    factor.asignar_elemento(3, 5)

    otro_factor = laboratorio.Vector(4)
    otro_factor.asignar_elemento(0, 1)
    otro_factor.asignar_elemento(1, 0)
    otro_factor.asignar_elemento(2, 0)
    otro_factor.asignar_elemento(3, 0)

    assert factor.similitud_coseno(otro_factor) == pytest.approx(0.486, rel=1e-2)


def test_polinomio() -> None:
    polinomio: laboratorio.Polinomio = laboratorio.Polinomio(coeficientes=[0, 0, 0, 5])

    assert polinomio.coeficientes == [0, 0, 0, 5]

    polinomio = laboratorio.Polinomio([5])
    assert polinomio.obtener_grado() == 0

    polinomio = laboratorio.Polinomio([5, 0, 1])
    assert polinomio.obtener_grado() == 2

    polinomio = laboratorio.Polinomio([0, 1, 2, 3, 4])
    assert polinomio.obtener_coeficiente(3) == 3

    with pytest.raises(ValueError):
        polinomio.obtener_coeficiente(5)

    polinomio.modificar_coeficiente(3, 6)
    assert polinomio.obtener_coeficiente(3) == 6

    with pytest.raises(ValueError):
        polinomio.modificar_coeficiente(-1, 0)

    polinomio = laboratorio.Polinomio([5, 4, 3])
    assert polinomio.evaluar(1) == 12

    polinomio = laboratorio.Polinomio([5, 4, 3])
    otro_polinomio: laboratorio.Polinomio = laboratorio.Polinomio([-3, -2, 4, 1])

    polinomio_suma: laboratorio.Polinomio = polinomio.sumar(otro_polinomio)

    assert polinomio_suma.obtener_coeficiente(0) == 2
    assert polinomio_suma.obtener_coeficiente(1) == 2
    assert polinomio_suma.obtener_coeficiente(2) == 7
    assert polinomio_suma.obtener_coeficiente(3) == 1


def test_rango() -> None:
    rango: laboratorio.Rango = laboratorio.Rango(inicio=2, limite=10, distancia=2)

    assert rango.inicio == 2
    assert rango.limite == 10
    assert rango.distancia == 2

    assert rango.numero_elementos() == 4

    assert rango.obtener_elemento(0) == 2
    assert rango.obtener_elemento(1) == 4
    assert rango.obtener_elemento(2) == 6
    assert rango.obtener_elemento(3) == 8

    with pytest.raises(ValueError):
        rango.obtener_elemento(4)

    assert rango.representar() == "2,4,6,8"
    assert rango.sumar() == 20

    rango: laboratorio.Rango = laboratorio.Rango(inicio=2, limite=10)
    assert rango.inicio == 2
    assert rango.limite == 10
    assert rango.distancia == 1

    with pytest.raises(ValueError):
        laboratorio.Rango(1, 1, 0)

    rango: laboratorio.Rango = laboratorio.Rango(inicio=0, limite=5, distancia=1)
    assert rango.numero_elementos() == 5

    rango: laboratorio.Rango = laboratorio.Rango(inicio=0, limite=2, distancia=1)
    assert rango.numero_elementos() == 2
