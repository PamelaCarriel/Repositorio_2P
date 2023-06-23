#Mediante busqueda binaria
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Lista de números ordenados
numbers = [2, 5, 8, 12, 15, 18, 20, 25]
target = 12

# Llamada a la función de búsqueda binaria
index = binary_search(numbers, target)

if index != -1:
    print("El número", target, "se encuentra en el índice", index)
else:
    print("El número", target, "no se encontró en la lista")