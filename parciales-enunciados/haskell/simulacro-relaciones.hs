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

-- Ejercicio 1
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas _ = True

-- Ejercicio 2
personas :: [(String,String)] -> [String]
personas _ = [""]

-- Ejercicio 3
amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ _ = [""]

-- Ejercicio 4
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos _ = ""
