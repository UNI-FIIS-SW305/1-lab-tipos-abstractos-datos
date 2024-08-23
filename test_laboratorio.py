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
    assert tarjeta.balance == 0

    with pytest.raises(ValueError):
        tarjeta.comprar(1)




