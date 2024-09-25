{-
2024 TN Primer Cuatrimestre

La Unidad de Tecnologías de la Información (UTI) de nuestra Facultad nos ha encargado que desarrollemos un nuevo sistema para el registro de alumnos. En este sistema se guarda la información de cada alumno, que está representada como una tupla de dos elementos: el primero es el nombre completo del alumno y el segundo una lista con las notas de los finales que rindió.

Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
Ejercicio 1 (2 puntos)

problema aproboMasDeNMaterias (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, alumno:seq⟨Char⟩, n: Z) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {n > 0}
  requiere: {El alumno se encuentra en el registro }
  asegura: {res = true <=> el alumno tiene más de n notas de finales mayores o iguales a 4 en el registro}
}
Ejercicio 2 (2 puntos)

problema buenosAlumnos (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨seq⟨Char⟩⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  asegura: {res es la lista de los nombres de los alumnos que están en registro cuyo promedio de notas es mayor o igual a 8 y no tiene aplazos (notas menores que 4)}
}
Para resolver el promedio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve su equivalente de tipo Float.
Ejercicio 3 (2 puntos)

problema mejorPromedio (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨Char⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {|registro| > 0 }
  asegura: {res es el nombre del alumno cuyo promedio de notas es el más alto; si hay más de un alumno con el mismo promedio de notas, devuelve el nombre de alumno que aparece primero en registro}
}
Ejercicio 4 (3 puntos)

problema seGraduoConHonores (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, cantidadDeMateriasDeLaCarrera: Z, alumno: seq⟨Char⟩ ) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {cantidadDeMateriasDeLaCarrera > 0}
  requiere: {El alumno se encuentra en el registro }
  requiere: {|buenosAlumnos(registro)| > 0}
  asegura: {res <=> true si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera -1) = true y alumno pertenece al conjunto de buenosAlumnos(registro) y el promedio de notas de finales de alumno está a menos (estrictamente) de 1 punto del mejorPromedio(registro)}
}

Ejercicio 5 (1 punto)

Conteste marcando la opción correcta. El Testing es una técnica de verificación que sirve para:
- [ ] Demostrar que un programa es correcto.
- [ ] Probar propiedades de un programa.
- [X] Encontrar fallas en un programa.

TEMA 2
-}

-- Funciones Auxiliares :p

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

promedio :: [Int] -> Float
promedio nums = fromIntegral (sumatoria nums) / fromIntegral (length nums)

pertenece :: Eq a => a -> [a] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys

absoluto :: Float -> Float
absoluto x
  | x < 0 = -x
  | otherwise = x

-- Ejercicio 1
aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias registro alumno n = contarAprobadas (notasDeAlumno registro alumno) > n

notasDeAlumno :: [(String, [Int])] -> String -> [Int]
notasDeAlumno [] _ = []
notasDeAlumno ((nombre, notas):xs) alumno
  | nombre == alumno = notas
  | otherwise = notasDeAlumno xs alumno

contarAprobadas :: [Int] -> Int
contarAprobadas [] = 0
contarAprobadas (x:xs)
  | x >= 4 = 1 + contarAprobadas xs
  | otherwise = contarAprobadas xs

-- Ejercicio 2
buenosAlumnos:: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((nombre, notas):xs)
  | promedio notas >= 8 && not (tieneAplazos notas) = nombre : buenosAlumnos xs
  | otherwise = buenosAlumnos xs

tieneAplazos :: [Int] -> Bool
tieneAplazos [] = False
tieneAplazos (nota:notas) = nota < 4 || tieneAplazos notas

-- Ejercicio 3
mejorPromedio:: [(String, [Int])] -> String
mejorPromedio [(nombre, notas)] = nombre
mejorPromedio ((nombre, notas): (nombre2, notas2) :xs)
  | promedio notas >= promedio notas2 = mejorPromedio ((nombre, notas):xs)
  | otherwise = mejorPromedio ((nombre2, notas2):xs)

-- Ejercicio 4
seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores registro cantidadDeMateriasDeLaCarrera alumno = aproboMasDeNMaterias registro alumno (cantidadDeMateriasDeLaCarrera - 1) && pertenece alumno (buenosAlumnos registro) && diferencia < 1
  where promedioAlumno = promedio (notasDeAlumno registro alumno)
        promedioMasAlto = notasDeAlumno registro (mejorPromedio registro)
        diferencia = absoluto (promedioAlumno - promedio promedioMasAlto)
