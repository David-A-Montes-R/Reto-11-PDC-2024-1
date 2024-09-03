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
