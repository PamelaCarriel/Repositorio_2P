# Búsqueda Lineal 
def busqueda_lineal(lista, objetivo): 
    for i, num in enumerate(lista): 
        if num == objetivo: 
            return i 
    return -1 
# Búsqueda Binaria
def busqueda_binaria(lista, objetivo): 
    izquierda, derecha = 0, len(lista) - 1 
    while izquierda <= derecha: 
        medio = (izquierda + derecha) // 2 
        if lista[medio] == objetivo: 
            return medio 
        elif lista[medio] < objetivo: 
            izquierda = medio + 1 
        else: 
            derecha = medio - 1 
    return -1 
lista_ordenada = list(range(1, 1001)) 
objetivo = 750
indice_lineal = busqueda_lineal(lista_ordenada, objetivo)
indice_binaria = busqueda_binaria(lista_ordenada, objetivo) 
print("Búsqueda Lineal:") 
print(f"El número {objetivo} se encuentra en el índice {indice_lineal}") 
print("Búsqueda Binaria:") 
print(f"El número {objetivo} se encuentra en el índice {indice_binaria}")
