import numpy as np


# function to find pivor column
def pivoColum(matrix, lines, columns):

    for line in range(0, lines):
        for column in range(0, columns):
            if matrix[line][column] < menorCP:
                colunaPivo = matrix[:, column]
                colunaPivo = np.reshape(colunaPivo, (3, 1))
    return colunaPivo

def pivoLine(matrix, lines, columns, colunaPivo):

    ladoDireito = rightSide(matrix)
    colunaPivo = colunaPivo

    



def rightSide(matrix):

    ladoDireito = matrix[:, 6]
    ladoDireito = np.reshape(ladoDireito, (3, 1))
    return ladoDireito


if __name__ == '__main__':

    menorCP = 0
    colunaPivo = []
    linhaPivo = []
    elementoPivo = 0

    matrix = np.array([[-7, -7, -6, -9, 0, 0, 0],
                       [4, 5, 3, 5, 1, 0, 30000],
                       [2, 1.5, 3, 3, 0, 1, 20000]]);


    lines = matrix.shape[0]
    columns = matrix.shape[1]

    matrix.astype(float)

    colunaPivo = pivoColum(matrix, lines, columns)
    linhaPivo = pivoLine(matrix, lines, columns, colunaPivo)
