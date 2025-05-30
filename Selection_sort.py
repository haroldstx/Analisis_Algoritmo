# Selection Sort
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encuentra el índice del elemento mínimo en el subarreglo arr[i..n-1]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo con el primer elemento del subarreglo
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    # Solicitar el número de elementos
    n = int(input("Enter number of elements: "))
    
    # Generar una lista de n elementos aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    print("Random elements:", arr)
    
    # Ordenar la lista usando Selection Sort
    selection_sort(arr)
    
    # Mostrar el arreglo ordenado
    print("Sorted array:", arr)

    # Medir el tiempo de ejecución
    import time
    inicio = time.time()
    selection_sort(arr)
    fin = time.time()
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
if __name__ == "__main__":
    main()