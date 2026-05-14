'''
Nivel Profesional - Cocktail Shaker Sort
Esta variante bidireccional resuelve el problema de las "tortugas" 
(valores pequeños al final del arreglo que tardan muchas iteraciones en moverse al principio en el Bubble Sort tradicional).
    Complejidad de Tiempo: O(n^2) en el peor caso, pero el rendimiento práctico mejora significativamente frente a listas casi 
    ordenadas o con "tortugas".
    Complejidad de Espacio: O(1).
'''
def Cocktail_Shaker_Sort(arr):
    n = len(arr)
    intercambiado = True
    inicio = 0
    fin = n - 1
    
    while intercambiado:
        intercambiado = False
        
        # 1. Pasada de izquierda a derecha (Mueve las "liebres" al final)
        for i in range(inicio, fin):
            if arr[i] > arr[i + 1]:
                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
                 intercambiado = True
        
        # Si no hubo intercambios, terminamos
        if not intercambiado:
            break
        
        # Reiniciar bandera para la pasada de regreso y ajustar el limite final
        intercambiado = False
        fin -= 1
        
        # 2. Pasada de derecha a izquierda (mueve las "Tortugas" al inicio)
        for i in range(fin - 1, inicio -1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intercambiado = True
        
        # Ajustar el limite inicial, ya que el primer elemento quedo ordenado
        inicio += 1

# Bloque de prueba
if __name__ == "__main__":
    # El '0' y el '2' al final porque son tortugas
    datos_pro = [5, 1, 4, 2, 8, 0, 2]
    print(f"Arreglo Original: {datos_pro}")
    Cocktail_Shaker_Sort(datos_pro)
    print(f"Arreglo Ordenado: {datos_pro}")
