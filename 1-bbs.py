'''
Implementacion Basica
comparar pares adyacentes y empujarlos hacia el final del arreglo
Complejidad de tiempo: O(n2) para todos los casos
Complejidad de espacio: O(1)
'''

def bubble_sort_basico(arr):
    n = len(arr)
    #bucle interno para el numero de pasadas
    for i in range(n - 1):
        #Bucle interno para las comparaciones
        #n - i - 1 evita iterar sobre los elementos que ya flotaron al final
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#bloque de prueba
if __name__ == "__main__":
    datos_basicos = [64, 34, 25, 12, 22, 11, 90]
    print(f"Arreglo Original: {datos_basicos}")
    bubble_sort_basico(datos_basicos)
    print(f"Arreglo Ordenado: {datos_basicos}\n")

