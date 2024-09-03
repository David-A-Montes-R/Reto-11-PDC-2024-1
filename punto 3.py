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