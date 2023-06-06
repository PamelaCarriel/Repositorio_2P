#UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
#Autor:Pamela Jesabel Carriel Mier 
#Ordenacion Distribución en python
#Fecha : 05 de junio del 2023
def countingSort(arr):
    # Encontrar el rango de valores en el arreglo
    max_value = max(arr)
    min_value = min(arr)
    range_value = max_value - min_value + 1

    # Inicializar el arreglo de conteo y el arreglo de salida
    count = [0] * range_value
    output = [0] * len(arr)

    # Contar la frecuencia de cada elemento en el arreglo
    for num in arr:
        count[num - min_value] += 1

    # Calcular las posiciones finales de los elementos en el arreglo ordenado
    for i in range(1, range_value):
        count[i] += count[i - 1]

    # Colocar los elementos en el arreglo de salida en orden
    for num in reversed(arr):
        output[count[num - min_value] - 1] = num
        count[num - min_value] -= 1

    return output

# Ejemplo de uso
arr = [5, 2, 8, 12, 1, 6]
print("Array original:", arr)
arr_ordenado = countingSort(arr)
print("Array ordenado:", arr_ordenado)
