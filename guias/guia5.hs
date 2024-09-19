-- 1.1)
longitud :: [t] -> Integer
longitud [] = 0
longitud ts = 1 + longitud (tail ts)

-- 1.2)
ultimo :: [t] -> t
ultimo [t] = t 
ultimo (t:ts) | longitud ts == 0 = t
              | otherwise = ultimo ts

-- 1.3)
principio :: [t] -> [t]
principio [t] = []
principio (t:ts) = t : principio ts

-- 1.4)
reverso :: [t] -> [t]
reverso [] = []
reverso [t] = [t]
reverso (x:xs) = reverso xs ++ [x]

-- 2.1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
-- pertenece x (t:ts) | x == t = True
--                    | otherwise = pertenece x ts
pertenece x (t:ts) = x == t || pertenece x ts

-- 2.2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [t] = True
todosIguales (t:ts) = t == head ts && todosIguales ts

-- 2.3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [t] = True
todosDistintos (t:ts) = not (pertenece t ts) && todosDistintos ts

-- 2.4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos l = not (todosDistintos l)

-- 2.5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (t:ts) | x == t = ts
                | otherwise = t : quitar x ts

-- 2.6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (t:ts) | x == t = quitarTodos x ts
                     | otherwise = t : quitarTodos x ts

-- 2.7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (t:ts) = t : eliminarRepetidos (quitarTodos t ts)

-- 2.8)
contiene :: (Eq t) => [t] -> [t] -> Bool
contiene [] ys = True
contiene (x:xs) ys = pertenece x ys && contiene xs ys

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] _ = False
mismosElementos _ [] = False
mismosElementos xs ys = contiene xs ys && contiene ys xs

-- 2.9)
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua ts = ts == reverso ts

-- 3.1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 3.2)
productoria :: [Integer] -> Integer
productoria [] = 0
productoria [t] = t
productoria (x:xs) = x * productoria xs

-- 3.3)
maximo :: [Integer] -> Integer
maximo [t] = t
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs

-- 3.4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x + n) : sumarN n xs

-- 3.5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo ts = sumarN (ultimo ts) ts

-- 3.7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)
  | mod x 2 == 0 = x : pares xs
  | otherwise = pares xs

-- 3.8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)
  | mod x n == 0 = x : multiplosDeN n xs
  | otherwise = multiplosDeN n xs

-- 3.9) Merge Sort
ordenar :: [Integer] -> [Integer]
ordenar []  = []
ordenar [x] = [x]
ordernar xs = maximo xs : ordenar (quitar (maximo xs) xs)

{-
ordenar xs  = juntar (ordenar ys) (ordenar zs)
  where
  (ys,zs)     = partirALaMitad xs

partirALaMitad :: [Integer] -> ([Integer],[Integer])
partirALaMitad l = splitAt (div (longitud l) 2) l

juntar :: [Integer] -> [Integer] -> [Integer]
juntar xs [] = xs
juntar [] ys = ys
juntar (x:xs) (y:ys)
  | x <= y = x : juntar xs (y:ys)
  | otherwise = y : juntar (x:xs) ys
-}

-- 4.a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs)
  | x == ' ' && head xs == ' ' = sacarBlancosRepetidos xs
  | otherwise = x : sacarBlancosRepetidos xs
