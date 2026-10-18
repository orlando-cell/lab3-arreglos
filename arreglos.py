# Archivo principal del sistema

# ============================================================
# INSTRUCCIONES PARA LOS INTEGRANTES:
# Cada uno debe pegar SU código en el lugar que le corresponde.
# NO pegar código en otro lugar. Respetar el orden.
# ============================================================

# ------------------------------------------------------------
# ETAPA 1: LISTAS UNIDIMENSIONALES
# Autor: Cristian Omar Huamán Rojas
# ------------------------------------------------------------

def declarar_lista():
    return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def recorrer_lista(lista):
    print("\nElementos de la lista:")
    for i, num in enumerate(lista):
        print(f"  [{i}] = {num}")


def modificar_elemento(lista):
    nuevo = int(input("Ingrese nuevo valor para el tercer elemento: "))
    lista[2] = nuevo
    print(f"Elemento modificado. Lista actual: {lista}")


def buscar_elemento(lista):
    num = int(input("Ingrese número a buscar: "))
    if num in lista:
        print(f"El número {num} SÍ existe en la lista.")
    else:
        print(f"El número {num} NO existe en la lista.")



# ------------------------------------------------------------
# ETAPA 2: MATRIZ 3x3
# Autor: Álvaro Leandro Gutiérrez Carranza
# ------------------------------------------------------------
def llenar_matriz():
    matriz = []
    print("\n  Ingrese los valores de la matriz 3x3:")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"    Posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("\n  Matriz 3x3:")
    for fila in matriz:
        print("   ", fila)

def sumar_matriz(matriz):
    suma = 0
    for fila in matriz:
        for valor in fila:
            suma += valor
    print(f"\n  Suma total de los elementos: {suma}")
    return suma



# ------------------------------------------------------------
# ETAPA 3: OPERACIONES SOBRE LISTAS
# Autor: Zinedine Michael Callirgos Cabanillas
# ------------------------------------------------------------

def insertar_elemento(lista):
    valor = int(input("  Ingrese valor a insertar: "))
    lista.append(valor)
    print(f"Elemento insertado. Lista actual: {lista}")

def eliminar_elemento(lista):
    pos = int(input("  Ingrese posición a eliminar: "))
    if 0 <= pos < len(lista):
        eliminado = lista.pop(pos)
        print(f"Elemento '{eliminado}' eliminado. Lista actual: {lista}")
    else:
        print("Posición inválida.")

def buscar_valor(lista):
    valor = int(input("  Ingrese valor a buscar: "))
    if valor in lista:
        print(f" El valor {valor} está en la posición {lista.index(valor)}.")
    else:
        print(f"El valor {valor} no se encuentra en la lista.")

def mostrar_lista(lista):
    print(f"\n  Lista actual: {lista}")

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
#------------------------------------------------------------
def mostrar_menu():
    print("\n" + "=" * 45)
    print("   LABORATORIO N° 3 - ARREGLOS Y LISTAS")
    print("=" * 45)
    print("1. Etapa 1: Listas unidimensionales")
    print("2. Etapa 2: Matriz 3x3")
    print("3. Etapa 3: Operaciones sobre listas")
    print("4. Etapa 4: Algoritmos de ordenamiento")
    print("5. Salir")
    print("=" * 45)

def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            lista = declarar_lista()
            recorrer_lista(lista)
            modificar_elemento(lista)
            buscar_elemento(lista)
        elif opcion == "2":
            matriz = llenar_matriz()
            mostrar_matriz(matriz)
            sumar_matriz(matriz)
        elif opcion == "3":
            lista = [10, 20, 30]
            insertar_elemento(lista)
            eliminar_elemento(lista)
            buscar_valor(lista)
            mostrar_lista(lista)
        elif opcion == "4":
            probar_ordenamiento()
        elif opcion == "5":
            print("\nSaliendo del sistema.")
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    main()
# ------------------------------------------------------------


