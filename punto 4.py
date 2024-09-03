#Desarrollar un programa que sume los elementos de una columna dada de una matriz
fila_1 = [1, 4]
fila_2 = [2, 5]
fila_3 = [3, 6]
A = [fila_1, fila_2, fila_3]
#una matriz de testeo conocida
def sumador_columnas(A,a):
    suma=0
    for b in range(len(A)):
        suma+=A[b][a]
    return suma

if __name__=="__main__":
    entrada=int(input("introduzca el número de columna de la matriz del cual quiere saber la suma de sus partes:"))
    a=entrada-1
    if -1<a< len(A[0]):
        suma=sumador_columnas(A,a)
        print("la suma de los elementos de la columna ",entrada,"es:",suma)
    else:
        print("introduzca un número de columna que esté dentro de la matriz")