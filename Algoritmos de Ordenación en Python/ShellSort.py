#UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
#Autor:Pamela Jesabel Carriel Mier 
#Ordenacion Shellsort en python
#Fecha : 05 de junio del 2023
def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

# Ejemplo de uso
arr = [5, 2, 8, 12, 1, 6]
print("Array original:", arr)
shellSort(arr)
print("Array ordenado:", arr)
