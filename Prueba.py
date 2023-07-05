#Universidad de la Fuerzas Armadas-ESPE
#Autor:Pamela Jesabel Carriel Mier 
"""Aplicar el algoritmo de ordenación de selección a la siguiente lista de números: [9, 2, 5, 1, 7]"""
#Fecha : 05 de julio del 2023
def Ordenacion_Seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
lista = [9, 2, 5, 1, 7]
resultado = Ordenacion_Seleccion(lista)
print(resultado)
