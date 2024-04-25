# Definir la primera matriz
fila1 = [1, 2]
fila2 = [4, 5]

# Definir la segunda matriz
fila3 = [3, 9, 12]
fila4 = [0, 7, 14]

# Organizar las matrices siguiendo el procedimiento para hallar el producto de estas

# Operar la primera fila de la primera matriz con la primera, segunda y tercera columna de las segunda matriz
fila11 = [fila1[0]*fila3[0] + fila1[1]*fila4[0]]
fila12 = [fila1[0]*fila3[1] + fila1[1]*fila4[1]]
fila13 = [fila1[0]*fila3[2] + fila1[0]*fila4[2]]

# Operar la segunda fila de la primera matriz con la primera, segunda y tercera columna de las segunda matriz
fila21 = [fila2[0]*fila3[0] + fila2[1]*fila4[0]]
fila22 = [fila2[0]*fila3[1] + fila2[1]*fila4[1]]
fila23 = [fila2[0]*fila3[2] + fila2[1]*fila4[2]]

A = fila11, fila12, fila13
B = fila21, fila22, fila23

# Mostrar la matriz final de 2x3
print(A)
print(B)


