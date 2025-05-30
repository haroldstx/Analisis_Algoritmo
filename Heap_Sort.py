# Heap Sort
import random
import time

def heapify(arr, n, i):
    # Encuentra el nodo más grande entre el nodo actual y sus hijos
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo más grande no es el nodo actual, intercambia y aplica heapify recursivamente
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover la raíz al final
        heapify(arr, i, 0)

def main():
    # Solicitar el número de elementos
    n = int(input("Enter number of elements: "))
    
    # Generar una lista de n elementos aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    print("Random elements:", arr)
    
    # Medir el tiempo de ejecución del Heap Sort
    inicio = time.time()
    heap_sort(arr)
    fin = time.time()
    
    # Mostrar el arreglo ordenado
    print("Sorted array:", arr)
    
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()