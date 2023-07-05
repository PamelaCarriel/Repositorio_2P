#Universidad de la Fuerzas Armadas-ESPE
#Autor:Pamela Jesabel Carriel Mier 
"""Modifica la función buscar_valor en Python para que reciba un árbol binario y un valor como
parámetros, y devuelva True si el valor se encuentra en el árbol, y False en caso contrario."""
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

"""arbol = insertar(arbol, 10)
arbol = insertar(arbol, 13)
arbol = insertar(arbol, 16)
arbol = insertar(arbol, 19)"""

def buscar_valor(arbol, valor):
    if arbol is None:
        return False
    elif arbol.valor == valor:
        return True
    elif valor < arbol.valor:
        return buscar_valor(arbol.izquierda, valor)
    else:
        return buscar_valor(arbol.derecha, valor)

print(buscar_valor(arbol , 1))