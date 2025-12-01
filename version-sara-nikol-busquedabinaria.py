def busqueda_binaria_validada(lista, objetivo):
    if not lista:
        return -1

    if lista != sorted(lista):
        raise ValueError("La lista debe estar ordenada antes de realizar la búsqueda binaria.")

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 15]
    objetivo = 7

    resultado = busqueda_binaria_validada(lista, objetivo)
    print("Resultado de la búsqueda:", resultado)



