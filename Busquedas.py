import random
import time

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
def ordenacion_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

def medir_tiempo_ms(algoritmo, lista, elemento=None):
    inicio = time.time()
    if elemento is None:
        algoritmo(lista)
    else:
        algoritmo(lista, elemento)
    fin = time.time()
    return (fin - inicio) * 1000  
n = 1000

lista_lineal = generar_lista_aleatoria(n)
lista_binaria = sorted(generar_lista_aleatoria(n))  
lista_burbuja = generar_lista_aleatoria(n)

elemento_a_buscar = random.randint(1, 1000)

tiempo_lineal = medir_tiempo_ms(busqueda_lineal, lista_lineal, elemento_a_buscar)
tiempo_binaria = medir_tiempo_ms(busqueda_binaria, lista_binaria, elemento_a_buscar)
tiempo_burbuja = medir_tiempo_ms(ordenacion_burbuja, lista_burbuja)

# Imprimir los resultados en milisegundos
print(f"Tiempo de búsqueda lineal: {tiempo_lineal} milisegundos")
print(f"Tiempo de búsqueda binaria: {tiempo_binaria} milisegundos")
print(f"Tiempo de ordenación burbuja: {tiempo_burbuja} milisegundos")
