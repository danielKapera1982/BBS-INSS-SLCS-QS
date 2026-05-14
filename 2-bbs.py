'''
Optimizacion de parada temprana
agregar una bandera simple(intercambiado), evitamos iteraciones innecesarias
si el arreglo(o el resto de el) ya se encuentra en orden
    * complejidad en tiempo: O(n2) en el peor caso, pero Ω(n) en el mejor caso(si ya esta ordenado)
    *complejidad en espacio: O(1)
'''
def bubble_sort_optimizado(arr):
    n = len(arr)
    for i in range(n):
        intercambiado =False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        
        # Si la bandera sigue en False, el arreglo ya esta ordenado
        if not intercambiado:
            print(f"[!] Optimizacion: Algoritmo detenido en la pasada {i + 1}")
            break

if __name__ == "__main__":
    datos_basicos = [64, 34, 25, 12, 22, 11, 90]
    print(f"Arreglo Original: {datos_basicos}")
    bubble_sort_optimizado(datos_basicos)
    print(f"Arreglo Ordenado: {datos_basicos}\n")
