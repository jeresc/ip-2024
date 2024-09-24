{-
Simulacro 2023 2do Cuatrimestre

problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar el orden)}
}

problema personas (relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en cualquiera de las dos posiciones, sin repetir}
}

problema amigosDe (persona: String, relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las
  componentes es persona}
}

problema personaConMasAmigos (relaciones: seq⟨String × String⟩) : String {
  requiere: {relaciones no vacía}
  requiere: {relacionesValidas(relaciones)}
  asegura: {resu es el Strings que aparece m´as veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}

-}

type Relaciones = [(String, String)]

-- Funciones Auxiliares :s

tieneRepetidos :: Eq a => [a] -> Bool
tieneRepetidos [] = False
tieneRepetidos (x:xs)
  | x `elem` xs = True
  | otherwise   = tieneRepetidos xs

aplanarDuplas :: [(t,t)] -> [t]
aplanarDuplas [] = []
aplanarDuplas ((x,y):xs) = x : y : aplanarDuplas xs

eliminarRepetidos :: Eq a => [a] -> [a]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)
  | x `elem` xs = eliminarRepetidos xs
  | otherwise   = x : eliminarRepetidos xs

-- Ejercicio 1
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas ((x,y):xs) = not (tieneRepetidos relaciones) && x /= y && relacionesValidas xs
  where relaciones = (x,y):xs

-- Ejercicio 2
personas :: [(String,String)] -> [String]
personas relaciones = eliminarRepetidos ( aplanarDuplas relaciones)

-- Ejercicio 3
amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a,b):xs)
  | persona == a = b : amigosDe persona xs
  | persona == b = a : amigosDe persona xs
  | otherwise = amigosDe persona xs

-- Ejercicio 4
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos relaciones = buscarPersonaConMasAmigos relaciones (personas relaciones)

cantidadDeAmigos :: String -> [(String,String)] -> Int
cantidadDeAmigos persona relaciones = length (amigosDe persona relaciones)

buscarPersonaConMasAmigos :: [(String,String)] -> [String] -> String
buscarPersonaConMasAmigos _ [a] = a
buscarPersonaConMasAmigos relaciones (a:b:ps)
  | cantidadDeAmigos a relaciones >= cantidadDeAmigos b relaciones = buscarPersonaConMasAmigos relaciones (a:ps)
  | otherwise = buscarPersonaConMasAmigos relaciones (b:ps)
