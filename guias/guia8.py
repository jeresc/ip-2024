from queue import LifoQueue as Stack, Queue
from random import randint, sample


# Stack / Pila
# Ejercicio 1
def generar_nros_al_azar(n: int, min: int, max: int) -> Stack[int]:
    stack: Stack[int] = Stack()

    for _ in range(n):
        stack.put(randint(min, max))

    return stack


stack: Stack[int] = generar_nros_al_azar(10, 1, 100)
print(stack.queue)


# Ejercicio 2
def cantidad_de_elementos(stack: Stack[int]) -> int:
    quantity: int = 0
    aux_stack: Stack[int] = Stack()

    while not stack.empty():
        quantity += 1
        aux_stack.put(stack.get())

    while not aux_stack.empty():
        stack.put(aux_stack.get())

    return quantity


print(cantidad_de_elementos(stack))
print(stack.queue)


# Ejercicio 3
def buscar_el_maximo(stack: Stack[int]) -> int:
    max_element: int = 0
    # float('-inf')
    aux_stack: Stack[int] = Stack()

    while not stack.empty():
        element = stack.get()
        if element >= max_element:
            max_element = element
        aux_stack.put(element)

    while not aux_stack.empty():
        stack.put(aux_stack.get())

    return max_element


print(buscar_el_maximo(stack))


# Ejercicio 4
def buscar_nota_maxima(stack: Stack[tuple[str, int]]) -> tuple[str, int]:
    max_element: tuple[str, int] = ("", 0)
    aux_stack: Stack[tuple[str, int]] = Stack()

    while not stack.empty():
        element = stack.get()
        if element[1] >= max_element[1]:
            max_element = element
        aux_stack.put(element)

    while not aux_stack.empty():
        stack.put(aux_stack.get())

    return max_element


students_stack: Stack[tuple[str, int]] = Stack()

students_stack.put(("a", 10))
students_stack.put(("b", 5))
students_stack.put(("c", 8))

print(buscar_nota_maxima(students_stack))


# Ejercicio 5
def esta_bien_balanceada(s: str) -> bool:
    stack: Stack[str] = Stack()
    keys: dict[str, str] = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # reemplazar in por pertenece :p
        if char in keys.values():
            stack.put(char)
        elif char in keys.keys():
            if stack.empty() or keys[char] != stack.get():
                return False

    return stack.empty()


balanced: str = "({[()]})"
unbalanced: str = "({[()])}"

print(esta_bien_balanceada(balanced))
print(esta_bien_balanceada(unbalanced))


# Ejercicio 6
def evaluar_expresion_postfija(s: str) -> int:
    stack: Stack[int] = Stack()

    for char in s:
        # reemplazar in por pertenece :p
        if char in "0123456789":
            stack.put(int(char))
        elif char in "+-*/":
            b = stack.get()
            a = stack.get()
            if char == "+":
                stack.put(a + b)
            elif char == "-":
                stack.put(a - b)
            elif char == "*":
                stack.put(a * b)
            elif char == "/":
                stack.put(a / b)

    return stack.get()


postfix: str = "3 4 + 5 * 2 -"
print(evaluar_expresion_postfija(postfix))


# Ejercicio 7
def invertir(stack: Stack[int]) -> Stack[int]:
    inverted_stack: Stack[int] = Stack()
    aux_stack: Stack[int] = Stack()

    while not stack.empty():
        element = stack.get()
        inverted_stack.put(element)
        aux_stack.put(element)

    while not aux_stack.empty():
        stack.put(aux_stack.get())

    return inverted_stack


def intercalar(stack1: Stack[int], stack2: Stack[int]) -> Stack[int]:
    if cantidad_de_elementos(stack1) != cantidad_de_elementos(stack2):
        return None

    merged_stack: Stack[int] = Stack()
    inverted_stack1: Stack[int] = invertir(stack1)
    inverted_stack2: Stack[int] = invertir(stack2)

    while not inverted_stack1.empty():
        merged_stack.put(inverted_stack1.get())
        merged_stack.put(inverted_stack2.get())

    return invertir(merged_stack)


s1: Stack[int] = generar_nros_al_azar(5, 1, 10)
s2: Stack[int] = generar_nros_al_azar(5, 1, 10)

print(s1.queue)
print(s2.queue)
print(intercalar(s1, s2).queue)
print(invertir(intercalar(s1, s2)).queue)


# Queue / Cola
# Ejercicio 8
def generar_nros_al_azar(n: int, min: int, max: int) -> Queue[int]:
    queue: Queue[int] = Queue()

    for _ in range(n):
        queue.put(randint(min, max))

    return queue


queue: Queue = generar_nros_al_azar(10, 1, 100)
print(queue.queue)

# Ejercicios 9, 10, 11 y 12 son iguales a los ejercicios 2, 3, 4 y 5 pero con Queue en vez de Stack


# Ejercicio 13.1
def armar_secuencia_de_bingo() -> Queue[int]:
    sequence: Queue[int] = Queue()
    numbers: list[int] = list(range(100))

    for _ in range(100):
        sequence.put(numbers.pop(randint(0, len(numbers) - 1)))

    return sequence


# Ejercicio 13.2
def jugar_carton_de_bingo(card: list[int], sequence: Queue[int]) -> int:
    plays: int = 0
    card: list[int] = card.copy()

    while len(card) != 0:
        plays += 1
        current_number = sequence.get()
        if current_number in card:
            card.remove(current_number)

    return plays


card: list[int] = sample(range(100), 12)
sequence: Queue[int] = armar_secuencia_de_bingo()

print(card)
print(sequence.queue)
print(jugar_carton_de_bingo(card, sequence))


# Ejercicio 14
def n_paciantes_urgentes(patients: Queue[tuple[int, str, str]]) -> int:
    urgent_patients: int = 0
    aux_queue: Queue[tuple[int, str, str]] = Queue()

    while not patients.empty():
        patient = patients.get()
        if 1 <= patient[0] <= 3:
            urgent_patients += 1
        aux_queue.put(patient)

    while not aux_queue.empty():
        patients.put(aux_queue.get())

    return urgent_patients


patients: Queue[tuple[int, str, str]] = Queue()

patients.put((1, "a", "b"))
patients.put((2, "c", "d"))
patients.put((3, "e", "f"))
patients.put((4, "g", "h"))

print(n_paciantes_urgentes(patients))


def merge_queues(*queues: Queue[int]) -> Queue[int]:
    merged_queue: Queue[int] = Queue()

    for queue in queues:
        while not queue.empty():
            merged_queue.put(queue.get())

    return merged_queue


# Ejercicio 15.1 Dar una especificacion para el problema planteado 🙄
# Ejercicio 15.2
# e.g. [("Juan", 43214132, False (preferencial), True (embarazado))]
def atencion_a_clientes(clients: Queue[tuple[str, int, bool, bool]]):
    priority_queue: Queue[str] = Queue()
    preferential_queue: Queue[str] = Queue()
    low_priority_queue: Queue[str] = Queue()
    aux_queue: Queue[tuple[str, int, bool, bool]] = Queue()

    while not clients.empty():
        client = clients.get()
        aux_queue.put(client)
        if client[3]:
            priority_queue.put(client)
        elif client[2]:
            preferential_queue.put(client)
        else:
            low_priority_queue.put(client)

    while not aux_queue.empty():
        clients.put(aux_queue.get())

    return merge_queues(priority_queue, preferential_queue, low_priority_queue)


clients: Queue[tuple[str, int, bool, bool]] = Queue()

clients.put(("Primero", 1, False, True))
clients.put(("Cuarto", 4, False, False))
clients.put(("Quinto", 5, False, False))
clients.put(("Sexto", 6, False, False))
clients.put(("Segundo", 2, True, False))
clients.put(("Tercero", 3, True, False))

print(atencion_a_clientes(clients).queue)

# Dictionaries / Diccionarios
