✅ 3. Versión 3 — “busqueda_binaria_validada.py”
Descripción:

Versión con validaciones adicionales:

Verifica si la lista está ordenada

Maneja lista vacía

Maneja datos incorrectos

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

    return -1*