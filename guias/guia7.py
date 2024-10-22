import numpy as np


# Ejercicio 1.6
def ordenados(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


input = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]


# Ejercicio 6.1
def es_matriz(matrix):
    if not matrix:
        return False
    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            return False
    return True


# Ejercicio 6.2
def filas_ordenadas(matrix):
    for row in matrix:
        if not ordenados(row):
            return False
    return True


# Ejercicio 6.3
def columna(matrix, i):
    return [row[i] for row in matrix]


# Ejercicio 6.4
def columnas_ordenadas(matrix):
    for i in range(len(matrix[0])):
        if not ordenados(columna(matrix, i)):
            return False
    return True


# Ejercicio 6.5
def transpuesta(matrix):
    transposed_matrix = []

    for i in range(len(matrix[0])):
        transposed_matrix.append(columna(matrix, i))

    return transposed_matrix
    # return [columna(matrix, i) for i in range(len(matrix[0]))]


print(np.matrix(input), "\n")
print(np.matrix(transpuesta(input)))

board_1 = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", "O", "X"],
]

board_2 = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", "O", "O"],
]


# Ejercicio 6.6
def quien_gana_tateti(board):
    # if X wins return 1
    # if O wins return 0
    # if no one wins return 2
    map = {
        "X": 1,
        "O": 0,
    }

    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return map[row[0]]

    # check column
    for column in transpuesta(board):
        if column[0] == column[1] == column[2] and column[0] != " ":
            return map[column[0]]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return map[board[0][0]]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return map[board[0][2]]

    return 2


print(quien_gana_tateti(board_1))
print(quien_gana_tateti(board_2))
