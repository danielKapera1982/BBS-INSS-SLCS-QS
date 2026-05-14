'''
Nivel Básico - La Implementación Clásica
El Reto: Implementar la lógica estándar. 
El algoritmo mantiene un subarreglo ordenado al principio y va tomando elementos uno por uno para insertarlos en su lugar.
Complejidad:
    * Tiempo: O(n2) en el peor de los casos(arreglo en orden inverso), pero Θ(n) es el mejor caso
    * Espacio: O(1) ya que es in-place
'''
def insertion_sort_basico(arr):
    # Empezamos desde el segundo elemento (indice 1)
    # porque asumimos que el primer elemento ya esta ordenado consigo mismo
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        
        # Desplazamos los elementos de la parte ordenada que sean mayores que la clave
        # una posicion hacia la derecha para hacer espacio
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        
        # insertamos la clave en el espacioque quedó libre 
        arr[j + 1] = clave

# bloque de prueba
if __name__ == "__main__":
    datos = [42, 12, 8, 55, 20, 3]
    print(f"Arreglo Original: {datos}")
    insertion_sort_basico(datos)
    print(f"Arreglo Ordenado: {datos}")
