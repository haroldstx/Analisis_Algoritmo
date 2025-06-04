# Quick Sort
import random
import time

def quick_sort(arr):
    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a random pivot for better performance
    pivot = random.choice(arr)
    
    # Partition the array into three subarrays
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    # Recursively sort the subarrays and combine them
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

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