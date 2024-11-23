"""
Ejercicio 1

 problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
   requiere: {e pertenece a s }
   asegura: {res es la posición de la última aparición de e en s}
 }

Por ejemplo, dados
  s = [-1,4,0,4,100,0,100,0,-1,-1]
  e = 0
se debería devolver res=7
"""


def ultima_aparicion(s: list[int], e: int) -> int:
    pass


"""
Ejercicio 2

 problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
   requiere: -
   asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
   asegura: {res no tiene elementos repetidos }
 }

Por ejemplo, dados
  s = [-1,4,0,4,3,0,100,0,-1,-1]
  t = [0,100,5,0,100,-1,5]
se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
ó res = [5,3,4] ó res = [5,4,3]
"""


def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    pass


"""
Ejercicio 3

Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
palabras que tienen la misma traducción en inglés y en alemán.

 problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
   requiere: -
   asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
 }

 Por ejemplo, dados los diccionarios
   aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
   inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
 se debería devolver res=2
"""


def contar_traducciones_iguales(ing: dict[str, str], ale: dict[str, str]) -> int:
    pass


"""
Ejercicio 4

Un grupo de autos se encuentra a distintas distancias de la milla inicial 0, viajando hacia un punto de destino en una milla objetivo.

Cada auto tiene una posición inicial y una velocidad (en millas por hora), representadas en dos listas: `posición` y `velocidad`, ambas de longitud n.
La posición `posición[i]` indica la milla inicial del i-ésimo auto, y `velocidad[i]` indica su velocidad.

Un auto no puede adelantar a otro, pero puede alcanzarlo y viajar junto a él a la velocidad del auto más lento.

Se define una *flota de autos* como uno o más autos que viajan juntos a la misma velocidad.
La velocidad de una flota es la velocidad mínima entre los autos que la forman.

Si un auto alcanza una flota en el punto de destino, también se considera parte de esa flota.

Escribir una función que, dado un destino `objetivo`, las posiciones iniciales y las velocidades de los autos, devuelva la cantidad de flotas que llegarán al destino.

problema numero_de_flotas (in objetivo: Z, in posición: seq⟨Z⟩, in velocidad: seq⟨Z⟩): Z {  
    requiere: {n > 0, n es igual a la longitud de posición y velocidad}  
    requiere: {1 <= n <= 10⁵}  
    requiere: {0 < objetivo <= 10⁶}  
    requiere: {0 <= posición[i] < objetivo, para todo i}  
    requiere: {posición contiene valores únicos}  
    requiere: {0 < velocidad[i] <= 10⁶, para todo i}  
    asegura: {res es la cantidad de flotas de autos que llegarán al destino considerando que cada auto se une a una flota si alcanza a otro antes o al llegar al destino.}  
}

"""


def numero_de_flotas(objetivo: int, posicion: list[int], velocidad: list[int]) -> int:
    pass
