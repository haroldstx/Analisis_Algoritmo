# Quick Sort
import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Elegir el pivote (en este caso, el último elemento)
        pivot = arr[-1]
        # Dividir el arreglo en dos subarreglos: menores y mayores al pivote
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        # Ordenar recursivamente y combinar
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def main():
    # Solicitar el número de elementos
    n = int(input("Enter number of elements: "))
    
    # Generar una lista de n elementos aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    print("Random elements:", arr)
    
    # Medir el tiempo de ejecución del Quick Sort
    inicio = time.time()
    sorted_arr = quick_sort(arr)
    fin = time.time()
    
    # Mostrar el arreglo ordenado
    print("Sorted array:", sorted_arr)
    
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()