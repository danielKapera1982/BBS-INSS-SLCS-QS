'''
Nivel Intermedio - Binary Insertion Sort
El Reto: En la versión básica, para encontrar dónde insertar la clave, 
hacemos una búsqueda lineal hacia atrás. Dado que la parte izquierda del arreglo ya está ordenada, 
podemos optimizar la cantidad de comparaciones utilizando Búsqueda Binaria (Binary Search).

reducir el numero de comparaciones de O(n) a O(log n) por iteracion
memoria sigue siendo O(n2)
'''

def busqueda_binaria(arr, clave, inicio, fin):
    # Encuentra la posicion correcta para insertar usando particion binaria
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] < clave:
            inicio = medio + 1
        else:
            fin = medio - 1
    return inicio

def binary_inserion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        
        # Encontramos la posicion donde debe ir la clave usando busqueda binaria
        posicion_insercion = busqueda_binaria(arr, clave, 0, i - 1)
        
        # Deplazamos los elementos a la derecha de un solo golpe
        # (esto es una ventaja sintactica de python usando slices)
        arr = arr[:posicion_insercion] + [clave] + arr[posicion_insercion:i] + arr[i + 1:]
    return arr

#bloque de prueba
if __name__ == "__main__":
    datos_binarios = [37, 23, 0, 17, 12, 72, 31]
    print(f"Original: {datos_binarios}")
    datos_ordenados = binary_inserion_sort(datos_binarios)
    print(f"Ordenado (Busqueda Binaria): {datos_ordenados}\n")

