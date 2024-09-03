#Desarrollar un programa que sume los elementos de una fila dada de una matriz.
fila_1 = [1, 4, 7,9]
fila_2 = [2, 5, 8,10]
fila_3 = [3, 6, 9,11]

A = [fila_1, fila_2,fila_3]

def sumador_filas(A,a):
    suma=0
    for b in range(len(A[0])):
        suma+=A[a][b]
    return suma

if __name__=="__main__":
    entrada=int(input("introduzca el número de fila de la matriz del cual quiere saber la suma de sus partes:"))
    a=entrada-1
    if -1<a< len(A):
        suma=sumador_filas(A,a)
        print("la suma de los elementos de la fila ",entrada,"es:",suma)
    else:
        print("introduzca un número de fila que esté dentro de la matriz")