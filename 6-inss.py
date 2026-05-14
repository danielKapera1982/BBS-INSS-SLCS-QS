'''
Nivel Profesional - La Evolución a Shell Sort
El Reto: El mayor cuello de botella del Insertion Sort clásico es que solo intercambia
elementos adyacentes; si un número pequeño está al final, debe desplazarse posición
por posición hasta el principio. El Shell Sort resuelve esto permitiendo intercambios de
elementos que están muy separados, reduciendo gradualmente la separación (el "gap")
hasta llegar a 1 (que se convierte en un Insertion Sort estándar, pero sobre un arreglo ya muy perfilado).
'''

def shell_sort(arr):
    n = len(arr)
    # inicializamos el gap (separacion), usualmente la mitad del tamaño del arreglo
    gap = n // 2
    
    # vamos reduciendo el gap a la mitad en cada iteracion hasta llegar a 0
    while gap > 0:
        # hacemos un InsertioSort modificado para el gap actual
        for i in range(gap, n):
            clave = arr[i]
            j = i
            
            # comparamos e intercambiamos con elementos que estan a una distancia del 'gap'
            while j >= gap and arr[j - gap] > clave:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = clave
        
        # Reducimos el gap
        gap //= 2
        
# bloque de prueba
if __name__ == "__main__":
    datos_shell = [89, 45, 68, 90, 29, 34, 17, 12]
    print(f"Original: {datos_shell}")
    shell_sort(datos_shell)
    print(f"Ordenado: {datos_shell}")