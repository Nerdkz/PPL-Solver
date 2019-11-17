import numpy as np


# function to find pivor column
def findPivoColum(matrix, columns):

    menorCP = 0

    for column in range(0, columns):
        if matrix[0][column] < menorCP:
            indiceCP = column
            colunaPivo = matrix[:, column]
            colunaPivo = np.reshape(colunaPivo, (3, 1))

    return colunaPivo, indiceCP


#function to find pivor line and pivor element
def findPivoLine(matrix, indexCP, lines, columns):

    minValue = float(99999.0)

    for line in range(0, lines):

        if matrix[line][indexCP] > 0 and matrix[line][columns - 1] > 0 :

            if (matrix[line][columns - 1] / matrix[line][indexCP]) < minValue:
                indiceLP = line
                linhaPivo = matrix[line, :]
                minValue = (matrix[line][columns - 1] / matrix[line][indexCP])

    return linhaPivo, indiceLP



def generateMatrix(matrix, lines, columns, columnPivor, linePivor, indexCP, indexLP):

    elementPivor = matrix[indexLP][indexCP]
    lineRef = linePivor / elementPivor

    for line in range(0, lines):
        for column in range(0, columns):

            if line != indexLP:
                newline = matrix[line, :] + (((- 1) * columnPivor[line][0]) * lineRef)
                matrix[line][:] = np.around(newline, 2)

            else:
                matrix[line][:] = lineRef

    #print("{}\n\n\n".format(matrix))



def multMatrix(a, b):
    result = [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]
    return result


# Main Function
if __name__ == '__main__':

    np.set_printoptions(precision= 3, suppress = True)

    colunaPivo = None
    linhaPivo = None

    matriz = np.array([[-5, -7, -8, 0, 0, 0],
                       [1, 1, 2, 1, 0, 1190],
                       [3, 4.5, 1, 0, 1, 4000]]);


    matriz.astype(float)

    linhasMatriz = matriz.shape[0]
    colunasMatriz = matriz.shape[1]

    while min(matriz[0, :]) < 0:
        colunaPivo, indiceCP = findPivoColum(matriz, colunasMatriz)
        linhaPivo, indiceLP = findPivoLine(matriz, indiceCP, linhasMatriz, colunasMatriz)
        generateMatrix(matriz, linhasMatriz, colunasMatriz, colunaPivo, linhaPivo, indiceCP, indiceLP)


    print("{}\n\n\n".format(matriz))
