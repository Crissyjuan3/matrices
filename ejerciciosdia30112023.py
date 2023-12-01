matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(f"el total de filas es de: {len(matriz)}")

print(matriz[0][1])
list = [1,2,3]
for elementos in list:
    print(elementos)
print()
print()
print()
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#
# for i in range(len(matriz)):
#     for j in matriz[i]:
#         print(j)
#
for i in range(len(matriz)):
    print(matriz[i][2], end=" ")
print()
print()
print()
#recorrer diagonal principal
for i in range(len(matriz)):
    print(matriz[i][i], end=" ")
print()
print()
print()

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j]*2, end=" ")
print()
print()
print()

for i in range(len(matriz)): #inicializa el recorrido de la filas
    for j in range(len(matriz)): #inicializa el recorrido de las columnas
        print(matriz[j][i], end=' ')
print()
print()
print()

print(f"el total de filas es de: {len(matriz)}")
print(f"el total de columnas es de: {len(matriz[0])}")
print(f"el total de elementos es de: {len(matriz)*len(matriz[0])}")

#puede pedir extremos de una matriz
#libreria numpi
#imprimame la diagonal secundario 3,5,7
#imprimame la segunda, segunda columna, diagonal principal inversa
#sumar la primera columna con la segunda columna
#lambda





