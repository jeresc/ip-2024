
-- 1.a)
parcialF :: Integer -> Integer
parcialF 1 = 8
parcialF 4 = 131
parcialF 16 = 16

-- b)
parcialG :: Integer -> Integer
parcialG n | n == 8 = 16
           | n == 16 = 4
           | n == 131 = 1

-- c)
parcialH :: Integer -> Integer
parcialH = parcialF . parcialG

parcialK :: Integer -> Integer
parcialK = parcialG . parcialF

-- 2.a)

absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | otherwise = -n

-- b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | abs x > abs y = abs x
                   | otherwise = abs y

-- c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x > y && x > z = x
              | y > z = y
              | otherwise = z

-- d) Sin pattern matching
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y = x == 0 || y == 0

-- Con pattern matching
algunoEs02 :: Float -> Float -> Bool
algunoEs02 _ 0 = True
algunoEs02 0 _ = True
algunoEs02 _ _ = False

-- f) (-Inf, 3), (3, 7], (7, Inf)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y = (x <= 3 && y <= 3) || (x > 7 && y > 7) || (x <= 7 && y <= 7 && x > 3 && y > 3)

-- g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x == y && x == z = x
                    | x == y && x /= z = x + z
                    | x == z && x /= y = x + y
                    | y == z && y /= x = y + x
                    | otherwise = x + y + z

-- h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = x `mod` y == 0

-- i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = x `mod` 10

-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = x `mod` 100

-- 3)
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = (a ^ 2) `mod` (a * b) == 0

-- 4.a)
type Punto2D = (Float, Float)
prodInt :: Punto2D -> Punto2D -> Float
prodInt (x1, y1) (x2, y2) = x1 * x2 + y1 * y2

-- b)
todoMenor :: Punto2D -> Punto2D -> Bool
todoMenor (x1, y1) (x2, y2) = x1 < x2 && y1 < y2

-- c)
distanciaPuntos :: Punto2D -> Punto2D -> Float
distanciaPuntos (x1, y1) (x2, y2) = sqrt ((x1 - x2) ^ 2 + (y1 - y2) ^ 2)

-- d)
type Terna = (Integer, Integer, Integer)
sumaTerna :: Terna -> Integer
sumaTerna (x,y,z) = x + y + z

-- e)
sumarSoloMultiplos :: Terna -> Integer -> Integer
sumarSoloMultiplos (x,y,z) n | x `mod` n == 0 && y `mod` n == 0 && z `mod` n == 0 = x + y + z
                             | x `mod` n == 0 && y `mod` n == 0 = x + y
                             | x `mod` n == 0 && z `mod` n == 0 = x + z
                             | y `mod` n == 0 && z `mod` n == 0 = y + z
                             | otherwise = 0

-- f)
posPrimerPar :: Terna -> Integer
-- even o bien n `mod` 2 == 0
posPrimerPar (x,y,z) | even x = 0
                     | even y = 1
                     | even z = 2
                     | otherwise = 4

-- g)
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)

-- h)
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

-- 5)
todosMenores :: Terna -> Bool
todosMenores (x,y,z) = (f x > g x) && (f y > g y) && (f z > g z)

f :: Integer -> Integer
f n | n <= 7 = n ^ 2
    | otherwise = (2 * n) - 1

g :: Integer -> Integer
g n | even n = div n 2
    | otherwise = (3*n) + 1

-- 6)
type Año = Integer
type EsBisiesto = Bool

bisiesto :: Año -> EsBisiesto
bisiesto año = not ( mod año 4 /= 0 || (mod año 100 == 0 && mod año 400 /= 0) )
