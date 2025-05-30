# Bubble Sort
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Recorre el arreglo y realiza intercambios si es necesario
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Solicitar el número de elementos
    n = int(input("Enter number of elements: "))
    
    # Generar una lista de n elementos aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    print("Random elements:", arr)
    
    # Medir el tiempo de ejecución del Bubble Sort
    inicio = time.time()
    bubble_sort(arr)
    fin = time.time()
    
    # Mostrar el arreglo ordenado
    print("Sorted array:", arr)
    
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()