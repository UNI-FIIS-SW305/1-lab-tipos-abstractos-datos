# Primer Laboratorio

Implemente los siguientes problemas en el archivo [`laboratorio.py`](laboratorio.py).
**No edite el resto de archivos de este repositorio.**

## Primer Problema

Implemente en Python una clase para representar las tarjetas de crédito que emiten los bancos.
La clase `TarjetaDeCredito` debe tener los siguientes campos.

* `nombre`: donde almacenamos el nombre del cliente.
* `numero_tarjeta`: el identificador de la tarjeta.
* `limite`: el limite de la tarjeta. Es la maxima deuda que un cliente puede tener.
* `balance`: El balance de la tarjeta. Es la deuda total del cliente.

Asimismo, la clase `TarjetaDeCredito` tiene los siguientes métodos:

* `comprar(monto)`, para realizar una compra con la tarjeta por un valor de `monto`, incrementando el valor de `balance`. En caso el nuevo balance exceda el valor de `limite`, la operación no debe ser permitida y debe generar una excepción `ValueError`.
* `depositar(monto)`, para pagar la deuda por una valor de `monto`, disminuyendo el valor de `balance`. En caso el valor de `monto` exceda el valor de `balance`, la operación no debe permitirse y debe generar una excepción `ValueError`.
* `reportar()` genera una cadena de caracteres con el siguiente formato: *"El cliente NOMBRE-CLIENTE con tarjeta NUMERO-TARJETA tiene un balance de BALANCE y un limite de LIMITE"*.

## Segundo Problema

Implemente la clase `Vector` para representar [espacios multi-dimensionales](https://es.wikipedia.org/wiki/Vector). Por ejemplo, en un espacio de 3 dimensiones, podríamos representar un vector con las coordenadas: 5, -2, 3. Esta clase debe contener los siguientes atributos:

* El campo `dimension`, que devuelve la dimensión del vector.
* El método `representar()`, que devuelve una cadena de caracteres que representa al vector. Por ejemplo, para un vector de coordenadas 3, 5, 0 este método devolvería la cadena `"(3,5,0)"` (sin espacios).
* El método `obtener_elemento(indice)` que devuelve la coordenada del vector con índice `indice`. 
Considerar que la primera coordenada del vector tiene índice `0`.
* El método `asignar_elememto(indice, valor)`, modifica la coordenada de índice `indice`, y le asigna el valor `valor`. En caso el índice no sea válido, lanzar una excepción `ValueError`.
* El método `sumar(otro_vector)`, que devuelve un nuevo vector que es [la suma](https://www.educaplus.org/movi/1_4sumavector.html) del vector original con el parámetro `otro_vector`. En caso las dimensiones de los vectores sean diferentes, lanzar una excepción `ValueError`.
* El método `es_igual(otro_vector)` devuelve `True` si ambos vectores son iguales, y `False` en caso contrario.
* El método `producto_escalar(otro_vector)` devuelve el producto escalar de [dos vectores](https://www.superprof.es/apuntes/escolar/matematicas/analitica/vectores/producto-escalar-2.html).  En caso las dimensiones de los vectores sean diferentes, lanzar una excepción `ValueError`.
* El método `similitud_coseno(otro_vector)` devuelve la [similitud coseno entre los dos vectores](https://www.learndatasci.com/glossary/cosine-similarity/).