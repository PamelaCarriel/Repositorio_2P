#Universidad de la Fuerzas Armadas-ESPE
#Autor:Pamela Jesabel Carriel Mier 
"""Implementa la función contar_nodos en Python que reciba como parámetro un árbol binario 
y devuelva la cantidad total de nodos en el árbol."""
#Fecha : 23 de junio del 2023

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

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
