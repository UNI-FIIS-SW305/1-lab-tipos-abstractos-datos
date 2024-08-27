# SW 305: Primer Laboratorio

Implemente los siguientes problemas completando las clases del módulo [`laboratorio.py`](laboratorio.py).
Incluya en cada método implementado un [DocString](https://www.datacamp.com/es/tutorial/docstrings-python) describiendo su solución, así como pruebas de que la funcionalidad está implementada correctamente.


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

## Tercer Problema

Un polinomio es una expresión algebraica,Q(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + ... + a<sub>n</sub>x<sup>n</sup> formada por un monomio o por la suma de varios monomios. Un monomio es una expresión algebraica formada por un coeficiente, una variable (por lo general x) y un exponente. Por ejemplo 5x<sup>3</sup>.

Implemente la clase `Polinomio` para representar polinomios. Esta clase debe tener los siguientes atributos:

* Un campo `coeficientes` que contenga una lista con los coeficientes del polinomio. El valor de esta lista es un parámetro del constructor. En la lista, el elemento de índice 0 contiene el coeficiente del término grado 0 del polinomio (el término constante). El elemento de índice 1 de la lista contiene el coeficiente del término de grado 1, y así sucesivamente.
* Un método `obtener_grado`, que devuelve el [grado del polinomio](https://es.wikipedia.org/wiki/Grado_(polinomio)). Por ejemplo, Q(x) = 5 es un polinomio de grado 0,y Q(x) = 5 + x<sup>2</sup> es un polinomio de grado 2.
* Un método `obtener_coeficiente(exponente)` que devuelva el coeficiente del término elevado al valor de `exponente`. Por ejemplo, en el polinomio Q(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> +  a<sub>3</sub>x<sup>3</sup> +... + a<sub>n</sub>x<sup>n</sup> el valor de `obtener_coeficiente(3)` tiene el valor de a<sub>3</sub>. En caso el valor de `exponente` sea inválido, generar una excepción `ValueError`.
* Un método `modificar_coeficiente(exponente, coeficiente)` que modifique el coeficiente del término de exponente `exponente` por un nuevo valor `coeficiente`. Por ejemplo, si invocamos al método `modificar_coeficiente(3, b)` en el polinomio Q(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup>  + a<sub>3</sub>x<sup>3</sup> +... + a<sub>n</sub>x<sup>n</sup>, el polinomio resultado sería  Q(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup>  + bx<sup>3</sup> +... + a<sub>n</sub>x<sup>n</sup>. En caso el valor de `exponente` sea inválido, generar una excepción `ValueError`.
* Un método `evaluar(valor)`, que reciba un entero `valor` y devuelva el valor del polinomio para ese valor. Por ejemplo, si invocamos `evaluar(1)` en el polinomio Q(x) = 5 + 4x + 3x<sup>2</sup> deberíamos obtener 12.
* Un método `suma(otro_polinomio)`, que reciba un objeto de tipo `Polinomio`, y devuelva un nuevo objeto `Polinomio` que sea el resultado de [sumar](https://www.superprof.es/apuntes/escolar/matematicas/algebra/polinomios/suma-de-polinomios.html#tema_suma-de-polinomios) nuestro objeto con el polinomio `otro_polinomio`. Por ejemplo, si sumamos los polinomios Q(x) = 5 +4x + 3x<sup>2</sup> y P(x) = -3 -2x +4x<sup>2</sup> + x<sup>3</sup> obtenemos R(x) = 2 + 2x + 7x<sup>2</sup> + x<sup>3</sup>.

## Cuarto Problema

Python incluye una función `range`, que genera secuencias de enteros. 
Vamos a replicar su funcionalidad en la clase `Rango`, generando una secuencia de enteros **sin almacenarlos en campos**. La clase `Rango` contiene los siguientes campos:

* Un campo `inicio`, que contiene el valor inicial de la secuencia.
* Un campo `limite`, que contiene el límite superior de la secuencia. `limite` **no pertenece a la secuencia.**
* Un campo `distancia`, que contiene la distancia entre números de la secuencia.
Su valor por defecto es 1. En caso el usuario asigne un valor de 0, lanzar una excepción `ValueError`.

Por ejemplo el rango `mi_rango = Rango(inicio=2, limite=10, distancia=2)`, generará los valores: 2, 4, 6, 8.

Los métodos de la clase `Rango` son:
 * El método `numero_elementos()`, que devuelve el número de elementos en el rango. Para `mi_rango()` en el ejemplo, genera el valor de 4.
 * El método `obtener_elemento(indice)`, que recibe un valor entero `indice` y devuelve el elemento de índice `indice` en el rango. Para `mi_rango` en el ejemplo, `obtener_elemento(0) == 2`, `obtener_elemento(1) == 4`, `obtener_elemento(2) == 6` y `obtener_elemento(3) == 8`. En caso el valor de índice sea inválido, lanzar una excepción `ValueError`.
 * El método `representar()` genera una cadena de caracteres que contenga la secuencia de elementos del rango. Para `mi_rango` en el ejemplo, el resultado es `2,4,6,8` (sin espacios).
 * El método `sumar()` que devuelve la suma de todos los elementos de la secuencia. Para `mi_rango` en el ejemplo, el resultado es 2 +4 +6 + 8 = 20.
