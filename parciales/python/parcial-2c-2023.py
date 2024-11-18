from queue import LifoQueue as Stack, Queue
import random  # xd

# from queue import LifoQueue as Pila, Queue as Cola

# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
s = [-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]
e = 0
# se debería devolver res=7


def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s) - 1, -1, -1):
        if s[i] == e:
            return i


print("[ultima_aparicion 7]", ultima_aparicion(s, e))
print("[ultima_aparicion 0]", ultima_aparicion([0, 1, 2, 3, 4, 5], 0))

# l = [2,3,4] -> len = 3
#             -> ultima posicion = 2
# l[3] no existe

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }


# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3]
# ó res = [5,3,4] ó res = [5,4,3]
def pertenece(l: list, n: int) -> bool:
    for elem in l:
        if elem == n:
            return True

    return False


def elementos_exclusivos(s: list, t: list) -> list:
    elementos: list[int] = s + t
    res: list[int] = []

    for elem in elementos:
        if (pertenece(s, elem) and not pertenece(t, elem)) or (
            pertenece(t, elem) and not (pertenece(s, elem))
        ):
            if not pertenece(res, elem):
                res.append(elem)

    return res


s: list[int] = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
t: list[int] = [0, 100, 5, 0, 100, -1, 5]

print("[elementos_exclusivos]", elementos_exclusivos(s, t))

# Resumen diccionarios
paises: dict[str, int] = {
    "argentina": 49,
    "colombia": 52,
    "chile": 19,
}

paises_detallado: dict[str, dict[str, int]] = {
    "argentina": {"poblacion": 49, "mundiales": 3},
}

paises_detallado["argentina"]["mundiales"]  # -> mundiales B)

paises["argentina"]  # -> 49
paises["alemania"] = 84  # agrego alemania a paises
paises["alemania"] = 43  # hubo una purga en alemania :(
paises.keys()  # -> ["argentina", "colombia", "chile"]
pertenece(paises.keys(), "argentina")
paises.values()  # -> [49, 52, 19]
paises.items()  # -> [("argentina", 49), ("colombia", 52), ("chile", 19)]


# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dict⟨String,String⟩, ale: dict⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2


def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    # anotacion para manu
    # pass -> no hacer nada
    iguales: int = 0
    for clave in ingles.keys():
        if pertenece(aleman.keys(), clave):
            if ingles[clave] == aleman[clave]:
                iguales += 1

    return iguales


aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print("[contar_traducciones_iguales] 2", contar_traducciones_iguales(aleman, ingles))

aleman = {"Mano": "Hand", "Pie": "Fuss", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print("[contar_traducciones_iguales] 1", contar_traducciones_iguales(aleman, ingles))


# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s,
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO


def convertir_a_diccionario(lista: list) -> dict:
    res: dict[int, int] = {}

    for num in lista:
        if pertenece(res.keys(), num):
            res[num] += 1
        else:
            res[num] = 1

    return res


lista: list[int] = [-1, 0, 4, 100, 100, -1, -1]
print("[convertir_a_diccionario]", convertir_a_diccionario(lista))
