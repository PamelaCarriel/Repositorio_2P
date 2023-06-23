#Universidad de la Fuerzas Armadas-ESPE
#Autor:Pamela Jesabel Carriel Mier 
"""Implementa la función eliminar_valor en Python que reciba un árbol binario
y un valor como parámetros, y elimine el nodo con ese valor del árbol."""
#Fecha : 23 de junio del 2023
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __repr__(self):
        return f'Nodo({self.valor})'

def crear_arbol():
    return None

arbol = crear_arbol()

def insertar(arbol, valor):
    if arbol is None:
        return Nodo(valor)
    else:
        if valor < arbol.valor:
            arbol.izquierda = insertar(arbol.izquierda, valor)
        else:
            arbol.derecha = insertar(arbol.derecha, valor)
        return arbol

arbol = insertar(arbol, 10)
arbol = insertar(arbol, 13)
arbol = insertar(arbol, 16)
arbol = insertar(arbol, 19)

def contar_nodos(arbol):
    if arbol is None:
        return 0
    else:
        return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)

print(contar_nodos(arbol))

def encontrar_minimo(arbol):
    if arbol is None:
        return None
    while arbol.izquierda is not None:
        arbol = arbol.izquierda
    return arbol

def eliminar(arbol, valor):
    if arbol is None:
        return arbol
    if valor < arbol.valor:
        arbol.izquierda = eliminar(arbol.izquierda, valor)
    elif valor > arbol.valor:
        arbol.derecha = eliminar(arbol.derecha, valor)
    else:
        if arbol.izquierda is None:
            return arbol.derecha
        elif arbol.derecha is None:
            return arbol.izquierda
        else:
            sucesor = encontrar_minimo(arbol.derecha)
            arbol.valor = sucesor.valor
            arbol.derecha = eliminar(arbol.derecha, sucesor.valor)
    return arbol

arbol = eliminar(arbol, 10)
print(arbol)
