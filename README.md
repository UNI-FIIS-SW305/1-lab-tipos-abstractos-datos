# Primer Laboratorio

Implemente los siguientes problemas en el archivo [`laboratorio.py`](laboratorio.py).
**No edite el resto de archivos de este repositorio.**

## Primer Problema

Implemente en Python una clase para representar las tarjetas de credito que emiten los bancos.
La clase `TarjetaDeCredito` debe tener los siguientes atributos.

* `nombre`: donde almacenamos el nombre del cliente.
* `numero_tarjeta`: el identificador de la tarjeta.
* `limite`: el limite de la tarjeta. Es la maxima deuda que un cliente puede tener.
* `balance`: El balance de la tarjeta. Es la deuda total del cliente.

Asimismo, la clase `TarjetaDeCredito` tiene los siguientes metodos:

* `comprar(monto)`, para realizar una compra con la tarjeta por un valor de `monto`, incrementando el valor de `balance`. En caso el nuevo balance exceda el valor de `limite`, la operacion no debe ser permitida y debe generar una excepcion `ValueError`.
* `depositar(monto)`, para pagar la deuda por una valor de `monto`, disminuyendo el valor de `balance`. En caso el valor de `monto` exceda el valor de `balance`, la operacion no debe permitirse y debe generar una excepcion `ValueError`.
* `reportar()` genera una cadena de caracteres con el siguiente formato: *"El cliente NOMBRE-CLIENTE con tarjeta NUMERO-TARJETA tiene un balance de BALANCE y un limite de LIMITE"*.