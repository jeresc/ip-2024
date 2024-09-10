-- 1)
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

-- 2)
parteEntera :: Float -> Integer
parteEntera n | 0 <= n && n < 1 = 0
              | n >= 1 = 1 + parteEntera (n-1)
              | otherwise = -1 + parteEntera (n+1)

-- 3)
esDivisible :: Integer -> Integer -> Bool
esDivisible x y = x == 0 || (x >= y && esDivisible (x - y) y)

{-
esDivisible x y | x == 0 = True
                | x < y = False
                | otherwise = esDivisible (x-y) y
-}

-- 4)
sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = (n*2 - 1) + sumaImpares (n-1)

-- 5)
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

-- 6)
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n = n < 10 || (ultimoDigito n == ultimoDigito (sinUltimoDigito n) && todosDigitosIguales (sinUltimoDigito n))

ultimoDigito:: Integer -> Integer
ultimoDigito n = mod n 10

sinUltimoDigito:: Integer -> Integer
sinUltimoDigito n = div n 10

-- 7)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito n
                 | otherwise = iesimoDigito (sinUltimoDigito n) i

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

-- 8)
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

-- 9)
esCapicua :: Integer -> Bool
esCapicua n = n == invertirNumero n 0

invertirNumero :: Integer -> Integer -> Integer
invertirNumero 0 invertido = invertido
invertirNumero n invertido = invertirNumero (n `div` 10) (invertido * 10 + n `mod` 10)

-- 10.a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n + f1 (n-1)

-- 10.b)
f2 :: Integer -> Integer -> Integer
f2 1 q = q
f2 n q = q^n + f2 (n - 1) q

-- 10.c)
f3 :: Integer -> Integer -> Integer
f3 n 1 = 2 * n
f3 1 q = f2 2 q
f3 n q = f2 (2 * n) q

-- 10.d)
f4 :: Integer -> Integer -> Integer
f4 n q = f3 n q - f2 (n - 1) q

-- 11.a)
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = 1 / fromIntegral (factorial n) + eAprox (n-1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

-- 11.b)
e :: Float
e = eAprox 10

-- 12)
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = 1 + 1 / raizDe2AproxAux (n - 1)

raizDe2AproxAux :: Integer -> Float
raizDe2AproxAux 1 = 2
raizDe2AproxAux n = 2 + 1 / raizDe2AproxAux (n - 1)

-- 13)
sumaDoble :: Integer -> Integer -> Integer
sumaDoble 0 m = 0
sumaDoble n m = sumaInterior n m + sumaDoble (n - 1) m

sumaInterior :: Integer -> Integer -> Integer
sumaInterior n 0 = 0
sumaInterior n m = n ^ m + sumaInterior n (m - 1)

-- 14)
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = potencias q n * potencias q m

potencias :: Integer -> Integer -> Integer
potencias q 1 = q
potencias q n = potencias q (n - 1) * (q ^ n)

