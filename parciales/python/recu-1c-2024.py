from queue import Queue

"""
1) Billetera Virtual [2 puntos]
Las billeteras virtuales son sistemas financieros (pero no necesariamente bancarios) en los cuales los
usuarios pueden cargar dinero y utilizarlo "virtualmente", realizando pagos y recargas de forma sencilla.
Éstas transacciones quedan registradas en el sistema de la billetera virtual. Por ejemplo, el Sistema Único
de Boleto Electrónico (SUBE) es un sistema de billetera virtual.

En el presente ejercicio verificaremos el histórico de transacciones (el historial) de una billetera virtual.
En esta billetera sólo se puede: recargar saldo (r), pagar un viaje (v), ver el balance actual (s), y salir (x).

Cada transacción queda grabada con su correspondiente caracter en una lista que representa el historial.
En historial tendremos una secuencia de caracteres donde:

v: Realiza un viaje (todos los viajes son de $56)
r: Recarga saldo (todas las recargas son de $350)
s: Visualiza el saldo actual (no modifica el saldo)
x: El usuario decide terminar el programa

Implementar la función verificar_transacciones() que dada una secuencia de caracteres s, devuelve el
saldo de la billetera al momento de terminar el programa. La finalización del programa está determinada
por: (1) aparición de una x, (2) el usuario está intentando hacer un pago sin saldo suficiente (en esta
billetera virtual no se permite saldo negativo), (3) no hay más transacciones en la lista.

problema verificar_transacciones (in s: String) : Z {
  requiere: {|s|>0}
  requiere: {s sólo puede contener los caracteres "r", "x", "v" o "s"}
  segura: {res >= 0}
  asegura: {res = ($350 * #ap_antes_corte("r", s)) - ($56 * #ap_antes_corte("v", s))}
}

problema #ap_antes_corte(in c: char, in s: String): Z {
  requiere: {True}
  asegura: {res = cantidad de veces que aparece c desde el inicio hasta que: aparece una x, o que el
cálculo del saldo se hace negativo}
}
"""


def verificar_transacciones(s: str) -> int:
    return 350 * apariciones_antes_corte("r", s) - 56 * apariciones_antes_corte("v", s)


def apariciones_antes_corte(c: str, s: str) -> int:
    count: int = 0
    balance: int = 0

    for char in s:
        if char == "v":
            balance -= 56
        elif char == "r":
            balance += 350

        if char == "x" or balance < 0:
            return count
        elif char == c:
            count += 1


print("[verificar_transacciones 714]", verificar_transacciones("ssrvvrrvvsvvsxrvvv"))
print("[verificar_transacciones 14]", verificar_transacciones("ssrvvvvsvvsvvv"))


"""
2) Hace calor [2 puntos]
El cambio climático es innegable. En las últimas décadas hemos registrado aumentos en las
temperaturas medias del planeta, lo que está generando una gran cantidad de efecto en la climatología
de todo el mundo: lluvias más caudalosas, temperaturas más extremas, etc. Las ciencias de la atmósfera
vienen estudiando estos cambios hace muchos años, y la conclusión con amplio consenso científico es
que este cambio es producto de la actividad humana: lo que se llama "cambio climático antropogénico".
Un grupo de estudiantes de la Licenciatura en Ciencias de la Atmósfera (carrera que se estudia en esta
Facultad) cuenta con una lista de tuplas de las temperaturas mínimas y máximas diarias de los últimos
años en la Ciudad de Buenos Aires. Implementar la función valor_minimo() que dado este listado de
tuplas devuelva el valor mínimo, entre las mínimas alcanzadas.

problema valor_minimo (in s: seq<(R,R)>): R {
  requiere: {|s| > 0}
  requiere: {En cada tupla de s el primero valor es menor que el segundo}
  asegura: {res pertenece a alguna tupla de s, en la primera posición}
  asegura: {No existe ningún valor en las primeras posiciones de las tuplas de s que sea menor que res}
}
"""


def valor_minimo(s: list[tuple[float, float]]) -> float:
    min: float = float("inf")

    for elem in s:
        if elem[0] <= min:
            min = elem[0]

    return min


s = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]
print("[valor_minimo -3.1]", valor_minimo(s))


"""
3) El MERVAL [3 puntos]
En la bolsa de valores de Argentina (denominada MERVAL) operan un gran número de empresas. Las
empresas cuyas acciones cotizan en la bolsa tienen un nombre identificador. Por ejemplo, "YPF Sociedad
Anónima" en la bolsa es: YPF; "Banco Galicia" es GGAL; Aluminio Argentino (Aluar, la empresa
siderúrgica) es ALUA; Loma Negra Compañía industrial de Cemento es LOMA. Durante una jornada los
precios de las acciones de estas empresas se ven modificados.
En el presente ejercicio vamos a trabajar con un diccionario (valores_diarios) que registrará el precio de
las acciones de diferentes empresas en diferentes momentos de un determinado mes. El diccionario
tendrá como clave los nombres de las empresas y como valores, listas de tuplas, donde cada tupla
(dupla) codifica el día (como entero) y el valor de la acción (como real). Es posible que exista más de un
registro por día.

Implementar la función valores_extremos() que dado un diccionario valores_diarios devuelva un nuevo
diccionario, con las mismas claves, pero que los valores sean tuplas que indiquen el mínimo y el máximo
alcanzado durante el periodo registrado.

problema valores_extremos(in cotizaciones_diarias: dict⟨String,seq⟨(Z x R)⟩⟩): dict⟨String,(R x R)⟩ {
  requiere: {Cada valor de cotizaciones_diarias es una secuencia de tuplas, donde los primeros elementos de dichas tuplas son enteros del 1 al 31}
  requiere: {Cada valor de cotizaciones_diarias es una secuencia de tuplas, de longitud mayor estricto que 0}
  asegura: {res tiene como claves exactamente las mismas claves que cotizaciones_diarias}
  asegura: {Cada valor de res es una tupla de (mínimo, máximo), donde mínimo y máximo son los valores extremos alcanzados por las cotizaciones de cada empresa}
}

cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
resultado_esperado es: {"YPF" : (3,100), "ALUA" : (0,50)}
"""


def valores_extremos(
    cotizaciones_diarias: dict[str, list[tuple[int, float]]]
) -> dict[str, tuple[float, float]]:
    res: dict[str, tuple[float, float]] = {}
    for key in cotizaciones_diarias.keys():
        min: int = float("inf")
        # anotacion para manu
        # float("inf") -> infinito (num mas grande que puede poner python)
        max: int = 0

        for day in cotizaciones_diarias[key]:
            if day[1] <= min:
                min = day[1]

            if day[1] >= max:
                max = day[1]

        res[key] = (min, max)

    return res


cotizaciones_diarias = {
    "YPF": [(1, 10), (15, 3), (31, 100)],
    "ALUA": [(1, 0), (20, 50), (31, 30)],
}
print("[valores_extremos]", valores_extremos(cotizaciones_diarias))


"""
4) Sudoku [3 puntos]
El sudoku es un juego moderno, inventado en el Siglo XX, que consiste en una grilla de 9x9 celdas. Para resolverlo es necesario completar las grillas con los dígitos del 1 al 9 haciendo que cada dígito aparezca
exactamente una vez en cada fila, columna y grilla 3x3 en la que se encuentren.
Implementar la función es_sudoku_valido() que dado un tablero de
sudoku (de 9x9) semi-completo devuelve True si en cada una de sus filas no hay números del 1 al 9
repetidos, y en cada una de sus columnas no hay números de 1 al 9 repetidos. Las celdas vacías se
marcarán con valor 0.

problema es_sudoku_valido(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
  requiere: {todos los elementos de m tienen longitud 9}
  requiere: {|m| = 9}
  requiere: {todos los elementos en todas las secuencias de m son números del 0 al 9}
  asegura: {(res = true) <=> en cada fila de m no se repiten números del 1 al 9}
  asegura: {(res = true) <=> en cada columna de m no se repiten números del 1 al 9}
}

"""

sudoku_valido_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku_valido_2 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 3, 5, 0, 0, 0],
    [0, 0, 0, 4, 0, 6, 7, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [0, 1, 0, 0, 9, 0, 0, 8, 0],
    [5, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 1, 6, 0, 8, 0, 0, 0],
    [0, 0, 0, 3, 5, 0, 0, 0, 0],
    [2, 7, 0, 0, 0, 0, 0, 0, 0],
]

sudoku_invalido_1 = [
    [5, 5, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku_invalido_2 = [
    [5, 0, 0, 0, 7, 0, 0, 0, 0],
    [6, 5, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def es_sudoku_valido(m: list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {}
    cols: dict[int, list[int]] = {}
    grid: dict[str, list[int]] = {}

    for r in range(9):
        for c in range(9):
            current_val: int = m[r][c]

            if current_val == 0:
                continue

            grid_index = (r // 3, c // 3)

            if not r in rows.keys():
                rows[r] = []
            if not c in cols.keys():
                cols[c] = []
            if not grid_index in grid.keys():
                grid[grid_index] = []

            if (
                current_val in rows[r]
                or current_val in cols[c]
                or current_val in grid[grid_index]
            ):
                return False

            cols[c].append(current_val)
            rows[r].append(current_val)
            grid[grid_index].append(current_val)

    return True


print("[es_sudoku_valido True]", es_sudoku_valido(sudoku_valido_1))
print("[es_sudoku_valido True]", es_sudoku_valido(sudoku_valido_2))
print("[es_sudoku_valido False]", es_sudoku_valido(sudoku_invalido_1))
print("[es_sudoku_valido False]", es_sudoku_valido(sudoku_invalido_2))
