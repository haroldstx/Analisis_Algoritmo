import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover elementos del arreglo que son mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Solicita al usuario la cantidad de elementos
n = int(input("Ingrese el número de elementos: "))

# Genera una lista aleatoria con n elementos entre 1 y 1000
lista = [random.randint(1, 100000) for _ in range(n)]
print("Lista original:", lista)

# Mide el tiempo de ejecución
inicio = time.time()
insertion_sort(lista)
fin = time.time()

# Muestra los resultados
print("Lista ordenada:", lista)
# Muestra el tiempo de ejecución
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
