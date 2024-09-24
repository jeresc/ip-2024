import Test.Hspec
import Funciones

main :: IO ()
main = hspec $ do
  describe "parcialF" $ do
    it "devuelve 8 para la entrada 1" $ do
      parcialF 1 `shouldBe` 8
    it "devuelve 131 para la entrada 4" $ do
      parcialF 4 `shouldBe` 131
    it "devuelve 16 para la entrada 16" $ do
      parcialF 16 `shouldBe` 16

  describe "parcialG" $ do
    it "devuelve 16 para la entrada 8" $ do
      parcialG 8 `shouldBe` 16
    it "devuelve 4 para la entrada 16" $ do
      parcialG 16 `shouldBe` 4
    it "devuelve 1 para la entrada 131" $ do
      parcialG 131 `shouldBe` 1

  describe "parcialH" $ do
    it "compone correctamente parcialF y parcialG" $ do
      parcialH 8 `shouldBe` parcialF (parcialG 8)
      parcialH 16 `shouldBe` parcialF (parcialG 16)
      parcialH 131 `shouldBe` parcialF (parcialG 131)

  describe "parcialK" $ do
    it "compone correctamente parcialG y parcialF" $ do
      parcialK 1 `shouldBe` parcialG (parcialF 1)
      parcialK 4 `shouldBe` parcialG (parcialF 4)
      parcialK 16 `shouldBe` parcialG (parcialF 16)

  describe "absoluto" $ do
    it "devuelve el número mismo si es positivo" $ do
      absoluto 5 `shouldBe` 5
    it "devuelve el equivalente positivo si el número es negativo" $ do
      absoluto (-3) `shouldBe` 3

  describe "maximoAbsoluto" $ do
    it "devuelve el valor absoluto máximo" $ do
      maximoAbsoluto 5 (-3) `shouldBe` 5
      maximoAbsoluto (-7) 7 `shouldBe` 7

  describe "maximo3" $ do
    it "devuelve el máximo de tres números" $ do
      maximo3 1 2 3 `shouldBe` 3
      maximo3 3 2 1 `shouldBe` 3
      maximo3 2 3 1 `shouldBe` 3

  describe "algunoEs0" $ do
    it "devuelve True si alguno de los números es 0" $ do
      algunoEs0 0 1 `shouldBe` True
      algunoEs0 1 0 `shouldBe` True
      algunoEs0 1 2 `shouldBe` False

  describe "algunoEs02" $ do
    it "devuelve True si alguno de los números es 0" $ do
      algunoEs02 0 1 `shouldBe` True
      algunoEs02 1 0 `shouldBe` True
      algunoEs02 1 2 `shouldBe` False

  describe "mismoIntervalo" $ do
    it "devuelve True si ambos números están en el mismo intervalo" $ do
      mismoIntervalo 2 1 `shouldBe` True
      mismoIntervalo 5 6 `shouldBe` True
      mismoIntervalo 8 9 `shouldBe` True
      mismoIntervalo 2 5 `shouldBe` False

  describe "sumaDistintos" $ do
    it "suma correctamente los enteros distintos" $ do
      sumaDistintos 1 1 1 `shouldBe` 1
      sumaDistintos 1 1 2 `shouldBe` 3
      sumaDistintos 1 2 2 `shouldBe` 3
      sumaDistintos 1 2 3 `shouldBe` 6

  describe "esMultiploDe" $ do
    it "devuelve True si x es múltiplo de y" $ do
      esMultiploDe 10 5 `shouldBe` True
      esMultiploDe 10 3 `shouldBe` False

  describe "digitoUnidades" $ do
    it "devuelve el dígito de las unidades de un número" $ do
      digitoUnidades 123 `shouldBe` 3
      digitoUnidades 456 `shouldBe` 6

  describe "digitoDecenas" $ do
    it "devuelve los últimos dos dígitos de un número" $ do
      digitoDecenas 123 `shouldBe` 23
      digitoDecenas 456 `shouldBe` 56

  describe "estanRelacionados" $ do
    it "devuelve True si a^2 es divisible por a*b" $ do
      estanRelacionados 8 2 `shouldBe` True
      estanRelacionados 7 3 `shouldBe` False

  describe "prodInt" $ do
    it "devuelve el producto punto de dos puntos 2D" $ do
      prodInt (1, 2) (3, 4) `shouldBe` 11
      prodInt (2, 3) (4, 5) `shouldBe` 23

  describe "todoMenor" $ do
    it "devuelve True si todas las coordenadas del primer punto son menores que las del segundo" $ do
      todoMenor (1, 2) (3, 4) `shouldBe` True
      todoMenor (2, 3) (1, 4) `shouldBe` False

  describe "distanciaPuntos" $ do
    it "calcula la distancia entre dos puntos 2D" $ do
      distanciaPuntos (1, 1) (4, 5) `shouldBe` 5.0
      distanciaPuntos (0, 0) (3, 4) `shouldBe` 5.0

  describe "sumaTerna" $ do
    it "devuelve la suma de una terna de enteros" $ do
      sumaTerna (1, 2, 3) `shouldBe` 6
      sumaTerna (4, 5, 6) `shouldBe` 15

  describe "sumarSoloMultiplos" $ do
    it "suma solo los múltiplos de n en una terna" $ do
      sumarSoloMultiplos (2, 4, 6) 2 `shouldBe` 12
      sumarSoloMultiplos (2, 5, 7) 2 `shouldBe` 2

  describe "posPrimerPar" $ do
    it "devuelve la posición del primer número par" $ do
      posPrimerPar (2, 3, 4) `shouldBe` 0
      posPrimerPar (1, 4, 5) `shouldBe` 1
      posPrimerPar (1, 3, 4) `shouldBe` 2
      posPrimerPar (1, 3, 5) `shouldBe` 4

  describe "crearPar" $ do
    it "crea un par a partir de dos elementos" $ do
      crearPar 1 "a" `shouldBe` (1, "a")
      crearPar "x" 2 `shouldBe` ("x", 2)

  describe "invertir" $ do
    it "invierte un par" $ do
      invertir (1, "a") `shouldBe` ("a", 1)
      invertir ("x", 2) `shouldBe` (2, "x")


  describe "todosMenores" $ do
    it "devuelve True cuando todos los elementos cumplen la condición f x > g x" $ do
      todosMenores (8, 8, 8) `shouldBe` True

    it "devuelve False cuando al menos un elemento no cumple la condición" $ do
      todosMenores (1, 8, 3) `shouldBe` False


    it "devuelve False cuando el resultado de f no es mayor que el de g para alguno de los elementos" $ do
      todosMenores (4, 5, 1) `shouldBe` False

  describe "bisiesto" $ do
    it "verifica si un año es bisiesto" $ do
      bisiesto 2024 `shouldBe` True
      bisiesto 2023 `shouldBe` False

  describe "distanciaManhattan" $ do
    it "calcula la distancia de Manhattan entre dos coordenadas 3D" $ do
      distanciaManhattan (1, 2, 3) (4, 5, 6) `shouldBe` 9.0
      distanciaManhattan (0, 0, 0) (1, 1, 1) `shouldBe` 3.0

  describe "comparar" $ do
    it "compara dos enteros basándose en la suma de sus dos últimos dígitos" $ do
      comparar 45 312 `shouldBe` -1
      comparar 2312 7 `shouldBe` 1
      comparar 45 172 `shouldBe` 0

  describe "sumaUltimosDosDigitos" $ do
    it "suma los dos últimos dígitos de un entero" $ do
      sumaUltimosDosDigitos 123 `shouldBe` 5
      sumaUltimosDosDigitos 456 `shouldBe` 11
