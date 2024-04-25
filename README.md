# Reto-once

### Punto numero 1

- Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```Python
# PARA LA SUMA

# Definir la primera matriz
fila1 = [1, 2, 3]
fila2 = [4, 5, 6]

# Definir la segunda matriz
fila3 = [3, 9, 12]
fila4 = [0, 7, 14]

# Organizar la primera matriz en un arreglo para realizar la suma
filaA = [fila1[0]+fila2[0], fila1[1]+fila2[1], fila1[2]+fila2[2]]
print(filaA)

# Organizar la segunda matriz en un arreglo para realizar la suma
filaB = [fila3[0]+fila4[0], fila3[1]+fila4[1], fila3[2]+fila4[2]]
print(filaB)


# PARA LA RESTA (mismas matrices)

# Definir la primera matriz
fila1 = [1, 2, 3]
fila2 = [4, 5, 6]

# Definir la segunda matriz
fila3 = [3, 9, 12]
fila4 = [0, 7, 14]

# Organizar la primera matriz en un arreglo para realizar la resta
filaA = [fila1[0]-fila2[0], fila1[1]-fila2[1], fila1[2]-fila2[2]]
print(filaA)

# Organizar la segunda matriz en un arreglo para realizar la resta
filaB = [fila3[0]-fila4[0], fila3[1]-fila4[1], fila3[2]-fila4[2]]
print(filaB)
```

### Punto numero 2

- Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```Python
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
```

### Punto numero 3

- Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```Python
# Definir una matriz predeterminada para hayar la transpuesta de esta
fila1 = [[1, 12], [4, 16], [8, 20]]

# Mostrar la matriz transpuesta con las siguientes condiciones
print(fila1[0][0], fila1[1][0], fila1[2][0])
print(fila1[0][1], fila1[1][1], fila1[2][1])
```


### Punto numero 4

- Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```Python
# Definir una matriz predeterminada para sumar los elementos de una columna (en este caso la 2)
fila1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Recorrer cada matriz y elegir los elementos en la segunda columan
A = (fila1[2][2])
B = (fila1[0][2])
C = (fila1[1][2])

# Mostrar la suma de estos elementos
print(A+B+C)
```

### Punto numero 5

- Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```Python
# Definir una matriz predeterminada para sumar los elementos de una fila (en este caso la tercera)
fila1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Recorrer la matriz y elegir los elementos en la tercera fila
A = (fila1[2][0])
B = (fila1[2][1])
C = (fila1[2][2])

# Mostrar la suma de estos elementos
print(A+B+C)
```
