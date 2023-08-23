def busqueda_binaria(lista, objetivo):
    # Suponemos que la lista está ordenada
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        elemento_medio = lista[medio]

        if elemento_medio == objetivo:
            return medio  # Encontramos el objetivo, devolvemos su índice
        elif elemento_medio < objetivo:
            izquierda = medio + 1  # El objetivo está en la mitad derecha
        else:
            derecha = medio - 1  # El objetivo está en la mitad izquierda

    return -1  # El objetivo no está en la lista
