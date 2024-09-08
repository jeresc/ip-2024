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
{- esDivisible x y | x == 0 = True
                | x < y = False
                | otherwise = esDivisible (x-y) y -}

esDivisible x y = x == 0 || (x >= y && esDivisible (x - y) y)

-- 4)
sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = (n*2 - 1) + sumaImpares (n-1)

-- 5)
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

