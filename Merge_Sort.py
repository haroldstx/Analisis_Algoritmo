# Merge Sort
import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        # Encuentra el punto medio del arreglo
        mid = len(arr) // 2
        
        # Divide el arreglo en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Ordena cada mitad recursivamente
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Fusiona las dos mitades ordenadas
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copia los elementos restantes de la mitad izquierda (si los hay)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copia los elementos restantes de la mitad derecha (si los hay)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Solicitar el número de elementos
    n = int(input("Enter number of elements: "))
    
    # Generar una lista de n elementos aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    print("Random elements:", arr)
    
    # Medir el tiempo de ejecución del Merge Sort
    inicio = time.time()
    merge_sort(arr)
    fin = time.time()
    
    # Mostrar el arreglo ordenado
    print("Sorted array:", arr)
    
    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()