# Tarea en clase semana 11

# Ordenación de Arreglo Multidimensional algoritmo de ordenación QuickSort

def quicksort(arr):

    # Función que implementa el algoritmo QuickSort para ordenar una lista.

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def ordenar_fila(matriz, fila):

    # Ordena una fila específica de una matriz bidimensional utilizando QuickSort.

    # Verifica si el número de fila es válido
    if fila < 0 or fila >= len(matriz):
        print("Número de fila fuera de rango.")
        return
    # Ordena la fila especificada
    matriz[fila] = quicksort(matriz[fila])

def imprimir_matriz(matriz):

    for fila in matriz:
        print(fila)

# Definimos la matriz
matriz = [[21, 4, 121],[95, 48, 62],[12, 84, 58]]

# El programa imprime la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Declaramos la fila a ordenar
ordenar_fila(matriz, 1)

print("\nMatriz con la fila 1 ordenada:")
imprimir_matriz(matriz)

# Fin del programa