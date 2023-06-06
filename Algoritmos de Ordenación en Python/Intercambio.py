#UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
#Autor:Pamela Jesabel Carriel Mier 
#Ordenacion por intercambio en python
#Fecha : 05 de junio del 2023
def bubble_sort(lista):
    n = len(lista)
    #Se utiliza el bucle for para iterar sobre la lista, y dentro de este bucle
    for i in range(n - 1):
        #e utiliza una variable intercambio para verificar si se ha realizado algún intercambio en cada iteración del bucle interno.
        intercambio = False
        #para comparar y realizar intercambios entre elementos adyacentes. 
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista

lista = [5, 2, 7, 10, 1, 0]
print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)
