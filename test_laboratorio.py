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

    assert factor.distancia_coseno(otro_factor) == pytest.approx(0.486, rel=1e-2)
