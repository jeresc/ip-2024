from queue import Queue

"""
1) Gestión de notas de estudiantes [2 puntos]
 
En una escuela llamada "Academia Futura", se desea desarrollar un programa para gestionar las notas de los estudiantes por materia. El programa debe procesar una lista de tuplas donde cada tupla contiene el nombre de un estudiante, el nombre de una materia y la nota final obtenida por el estudiante en esa materia.
 
Se pide implementar una función en python, que respete la siguiente especificación:
 
problema gestion_notas (in notas_estudiante_materia: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
  requiere: { Las primeras componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las segundas componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las terceras componentes de notas_estudiante_materia están entre 1 y 10, ambos inclusive }
  requiere: { No hay 2 tuplas en notas_estudiante_materia que tengan la primera y segunda componente iguales (mismo estudiante y misma materia) }
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de notas_estudiante_materia (o sea, un estudiante)}
  asegura: {El valor en res de un estudiante es una lista de tuplas donde cada tupla contiene como primera componente el nombre de la materia y como segunda componente la nota obtenida por el estudiante en esa materia según notas_estudiante_materia}
  asegura: { Para toda clave (estudiante) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (materia) }
}
"""


def gestion_notas(
    students: list[tuple[str, str, int]]
) -> dict[str, list[tuple[str, int]]]:
    notes_by_student: dict[str, list[tuple[str, int]]] = {}
    for student in students:
        name: str = student[0]
        if not name in notes_by_student.keys():
            notes_by_student[name] = [(student[1], student[2])]
        else:
            notes_by_student[name].append((student[1], student[2]))

    return notes_by_student


students = [("jere", "algebra", 7), ("juan", "ip", 2), ("jere", "ip", 2)]
print("[gestion_notas]", gestion_notas(students))


"""
2) Cantidad dígitos pares [2 puntos]
 
Se pide implementar una función en Python llamada cantidad_digitos_pares que respete la siguiente especificación:
 
problema cantidad_digitos_pares (in numeros: seq⟨Z⟩) : Z {
  requiere:{Todos los elementos de numeros son mayores iguales a 0}
  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
}

Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8).
"""


def cantidad_digitos_pares(nums: list[int]) -> int:
    count: int = 0
    for num in nums:
        num_string: str = str(num)
        for c in num_string:
            if int(c) % 2 == 0:
                count += 1

    return count


print("[cantidad_digitos_pares 4]", cantidad_digitos_pares([12, 213, 321, 78, 99, 11]))
print("[cantidad_digitos_pares 7]", cantidad_digitos_pares([32, 99, 33, 44, 22, 22]))


"""
3) Priorizar cola de paquetes [2 puntos]
 
En una empresa de logística, se manejan paquetes que llegan a una bodega y deben ser procesados para su posterior distribución. Cada paquete está representado por una tupla (id_paquete, peso), donde id_paquete es un identificador único del paquete y peso representa el peso del paquete en kilogramos.
 
Se pide implementar una función en Python llamada reordenar_cola_primero_pesados que respete la siguiente especificación:
 
problema reordenar_cola_primero_pesados(in paquetes: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
  requiere: {no hay repetidos en las primeras componentes (Ids) de paquetes}
  requiere: {todos las segundas componentes (pesos) de paquetes son mayores estricto a cero}
  requiere: {umbral es mayor o igual a cero}
  asegura: {los elementos de res son exactamente los mismos que los elementos de paquetes}
  asegura: {|res| = |paquetes|}
  asegura: {no hay un elemento en res, cuyo peso sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo peso sea mayor que el umbral)}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son menores o iguales que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces p1 aparece primero que p2 en res}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son mayores que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces p1 aparece primero que p2 en res}
}
"""


def reordenar_cola_primero_pesados(
    packages: Queue[tuple[str, int]], threshold: int
) -> Queue[tuple[str, int]]:
    packages_copy: Queue[tuple[str, int]] = Queue()

    ordered_packages: Queue[tuple[str, int]] = Queue()
    light_packages: Queue[tuple[str, int]] = Queue()

    while not packages.empty():
        package: tuple[str, int] = packages.get()
        packages_copy.put(package)

        if package[1] <= threshold:
            light_packages.put(package)
        else:
            ordered_packages.put(package)

    while not light_packages.empty():
        ordered_packages.put(light_packages.get())

    while not packages_copy.empty():
        packages.put(packages_copy.get())

    return ordered_packages


packages: Queue[tuple[str, int]] = Queue()
packages.put(("1", 1))
packages.put(("2", 2))
packages.put(("3", 3))
packages.put(("4", 4))
packages.put(("5", 5))
packages.put(("6", 6))
packages.put(("7", 7))

print(
    "[reordenar_cola_primero_pesados]",
    reordenar_cola_primero_pesados(packages, 4).queue,
)


"""
4) Matriz pseudo ordenada [2 puntos]
 
Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente
 
Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:
 
matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
}
"""


def min(l: list[int]) -> int:
    res: int = l[0]
    for num in l:
        if num <= res:
            res = num

    return res


def column(matrix, i):
    col: list[int] = []
    for row in matrix:
        col.append(row[i])
    return col


def transposed(matrix):
    transposed_matrix: list[list[int]] = []

    for i in range(len(matrix[0])):
        transposed_matrix.append(column(matrix, i))

    return transposed_matrix


"""
[0,1,2]
[3,4,5]
[6,7,8]
 
transposed ->
 
[0,3,6]
[1,4,7]
[2,4,8]
"""


def matriz_pseudo_ordenada(matrix: list[list[int]]) -> bool:
    last_min: int = min(matrix[0]) - 1
    for row in transposed(matrix):
        min_row = min(row)
        if not min_row > last_min:
            return False
        last_min = min_row

    return True


ordered = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]
unordered = [[0, 1, 2, 0], [1, 2, 3, 1], [2, 3, 4, 2]]

print("[matriz_pseudo_ordenada True]", matriz_pseudo_ordenada(ordered))
print("[matriz_pseudo_ordenada False]", matriz_pseudo_ordenada(unordered))
