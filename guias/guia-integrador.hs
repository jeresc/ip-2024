-- SISTEMA DE STOCK
-- EJERCICIO 1
generarStock :: [String] -> [(String,Int)]
generarStock [] = []
generarStock (p:ps) = añadirProducto p (generarStock ps)

añadirProducto :: String -> [(String,Int)] -> [(String,Int)]
añadirProducto p [] = [(p,1)]
añadirProducto p ((n,c):ss)
  | p == n = (n,c+1) : ss
  | otherwise = (n,c) : añadirProducto p ss

-- EJERCICIO 3
stockDeProducto :: [(String,Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((n,c):ss) p
  | p == n = c
  | otherwise = stockDeProducto ss p

-- EJERCICIO 3
dineroEnStock :: [(String,Int)] -> [(String,Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((n,c):ss) ps = precioProducto ps n * fromIntegral c + dineroEnStock ss ps

precioProducto :: [(String,Float)] -> String -> Float
precioProducto ((n,v):ps) p
  | p == n = v
  | otherwise = precioProducto ps p

-- EJERCICIO 4
aplicarOferta :: [(String,Int)] -> [(String,Float)] -> [(String,Float)]
aplicarOferta _ [] = []
aplicarOferta ss ((n,v):ps)
  | stockDeProducto ss n > 10 = (n,v * 0.80) : aplicarOferta ss ps
  | otherwise = (n,v) : aplicarOferta ss ps

-- SOPA DE NUMEROS
type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int,Int)
type Camino = [Posicion]

-- EJERCICIO 5
maximo :: Tablero -> Int
maximo [f] = maximoEnFila f
maximo (f:fs)
  | maximoEnFila f > maximo fs = maximoEnFila f
  | otherwise = maximo fs

maximoEnFila :: Fila -> Int
maximoEnFila [f] = f
maximoEnFila (f:fs)
  | f > maximoEnFila fs = f
  | otherwise = maximoEnFila fs

