#UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
#Autor:Pamela Jesabel Carriel Mier 
#Ordenacion Burbuja en python
#Fecha : 05 de junio del 2023
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [6, 4, 8, 14, 12, 3]
print("Lista original:", arr)
bubble_sort(arr)
print("Lista ordenada:", arr)
