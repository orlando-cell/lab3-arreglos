# Archivo principal del sistema

# ============================================================
# INSTRUCCIONES PARA LOS INTEGRANTES:
# Cada uno debe pegar SU código en el lugar que le corresponde.
# NO pegar código en otro lugar. Respetar el orden.
# ============================================================

# ------------------------------------------------------------
# ETAPA 1: LISTAS UNIDIMENSIONALES
# Autor: Cristian Omar Huamán Rojas
# PEGA AQUÍ TU CÓDIGO (declarar, recorrer, modificar, buscar)
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 2: MATRIZ 3x3
# Autor: Álvaro Leandro Gutiérrez Carranza
# PEGA AQUÍ TU CÓDIGO (llenar, mostrar, sumar matriz)
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 3: OPERACIONES SOBRE LISTAS
# Autor: Zinedine Michael Callirgos Cabanillas
# PEGA AQUÍ TU CÓDIGO (insertar, eliminar, buscar, mostrar)
# ------------------------------------------------------------



# ============================================================
# Etapa 4: Algoritmos de Ordenamiento
# Autor: Juan Orlando Correa Flores
# ============================================================

def burbuja(lista):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def seleccion(lista):
    """Ordena una lista usando el algoritmo Selection Sort."""
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


def probar_ordenamiento():
    """Prueba ambos algoritmos con una lista desordenada."""
    lista_original = [64, 25, 12, 22, 11]
    print("\n" + "=" * 45)
    print("   PRUEBA DE ALGORITMOS DE ORDENAMIENTO")
    print("=" * 45)
    print(f"  Lista original: {lista_original}")

    lista_burbuja = lista_original.copy()
    burbuja(lista_burbuja)
    print(f"  Burbuja       : {lista_burbuja}")

    lista_seleccion = lista_original.copy()
    seleccion(lista_seleccion)
    print(f"  Selección     : {lista_seleccion}")
    print("=" * 45)



# ------------------------------------------------------------
# MENÚ PRINCIPAL Y PRUEBAS
# Autor: Anthony Rene Terraz Terrones
# PEGA AQUÍ TU CÓDIGO (main, menú, pruebas)
# ------------------------------------------------------------


