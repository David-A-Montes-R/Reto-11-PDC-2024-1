# Reto 11 PDC 2024-1

## punto 1

Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
fila_1 = [1, 8, 3]
fila_2 = [10,5, 6]
fila_3 = [7, 8, 9]

A = [fila_1, fila_2, fila_3]
# 2 matrices conocidas de prueba
fila_1B=[1, 2, 3]
fila_2B=[4, 5, 6]
fila_3B=[7, 9, 11]

B=[fila_1B,fila_2B,fila_3B]
def verificar(A,B):
    verificadores=[]
    #aquí se verifica si las matrices tienen la misma cantidad de filas
    for a in range(len(A)):
            for b in range(len(A[a])):
                if len(A)==len(B) and ( len(A[a])==len(B[a])):
                    verificadores.append(1) #en el reto anterior no sé por qué me falló el .append ¿?
                else:
                    verificadores.append(0)
    if 0 in verificadores:
        verificación=False
    else:
        verificación=True
    return verificación
def suma_matrices(A,B): #aquí se suman las matrices, transforma a A en la suma de A y B
    for a in range(len(A)):
        for b in range(len(A[a])):
            A[a][b]+=B[a][b]
    return A
if __name__=="__main__":
    verificación=verificar(A,B)
    if verificación==True:
        suma=suma_matrices(A,B)
        print("la suma de las matrices es: ",suma)
    else:
        print("error, las matrices dadas no cumplen las condiciones para ser sumadas ")
```

## punto 2

Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
fila_1 = [1,8, 3]
fila_2 = [10,5, 6]
fila_3 = [7, 8,9]

A = [fila_1, fila_2, fila_3]
# 2 matrices conocidas de prueba
fila_1B=[1,2,3]
fila_2B=[4,5,6]
fila_3B=[7,8,11]

B=[fila_1B,fila_2B,fila_3B]
def verificar(A,B):
    verificadores=[]
    #aquí se verifica si las matrices tienen la misma cantidad de filas
    for a in range(len(A)):
            for b in range(len(A[a])):
                if (len(A)==len(B[a]) and (len(A[a])==len(B))):
                    verificadores.append(1)
                else:
                    verificadores.append(0)
    if 0 in verificadores:
        verificación=False
    else:
        verificación=True
    return verificación
def multiplicador(A,B):
    for a in range(len(A)):
        for b in range(len(A[a])):
             A[a][b]*=B[b][a]
    return A

if __name__=="__main__":
    verificación=verificar(A,B)
    if verificación==True:
        multiplicación=multiplicador(A,B)
        print("el resultado de la multiplicación de matrices es: ",multiplicación)
    else:
        print("las matrices no cumplen las condiciones requeridas para multiplicarse")
```

## punto 3

Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#hallar la transpuesta de una matriz
fila_1 = [1, 4, 7]
fila_2 = [2, 5, 8]
fila_3 = [3, 6, 9]
A = [fila_1, fila_2,fila_3]
#Se usa una matriz de testeo conocida

transpuesta=[]
def verificar(A):
    verificadores=[]
    for a in range(len(A[0])):
        if len(A[a])== len(A[0]):
            verificadores.append(1)
        else:
            verificadores.append(0)
    if 0 in verificadores:
        verificación=False
    else:
        verificación=True
    return verificación
def transposición(A):
    for a in range(len(A[0])):
        filas_transpuesta=[A[b][a] for b in range(len(A))]
        transpuesta.append(filas_transpuesta)
    return transpuesta
if __name__=="__main__":
    verificador=verificar(A)
    if verificador==True:
        transpuesta=transposición(A)
        print("esta es la transpuesta de la matriz original:",transpuesta)
    else:
        print("no se ha ingresado una matriz válida")

#este programa funciona correctamente
```

## punto 4

Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python

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
```
## punto 5

Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
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
```