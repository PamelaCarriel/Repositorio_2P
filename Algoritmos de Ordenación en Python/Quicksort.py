#UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
#Autor:Pamela Jesabel Carriel Mier 
#Ordenacion Quicksort en python
#Fecha : 05 de junio del 2023
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Ejemplo de uso
arr = [5, 2, 8, 12, 1, 6]
print("Array original:", arr)
quickSort(arr, 0, len(arr) - 1)
print("Array ordenado:", arr)
