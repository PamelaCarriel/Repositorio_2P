def busqueda_hash(lista, objetivo):
    # Creamos un diccionario (hash table) para mapear elementos a índices
    hash_table = {}

    # Llenamos la tabla de hash con los elementos de la lista
    for i, elemento in enumerate(lista):
        hash_table[elemento] = i

    # Buscamos el objetivo en el diccionario
    if objetivo in hash_table:
        return hash_table[objetivo]  # Devolvemos el índice si se encuentra
    else:
        return -1  # El objetivo no está en la lista
