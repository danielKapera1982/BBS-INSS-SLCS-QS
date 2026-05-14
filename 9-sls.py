def stable_selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        indice_minimo = i
        
        #encontramos el minimo
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        # guardamos el valor minimo
        valor_minimo = arr[indice_minimo]
        
        # en lugar de un swap directo, desplazamos los elementos hacia la derecha
        #esto preserva el orden relativo de los elemento iguales
        while indice_minimo > i:
            arr[indice_minimo] = arr[indice_minimo - 1]
            indice_minimo -= 1
        #colocamos el minimo en su posicion correcta
        arr[i] = valor_minimo
#bloque de prueba
if __name__ == "__main__":
    #usamos tuplas (valor, id original) para demostrar la estabilidad
    #tenemos dos '20', ID A aparece antes que el ID 'B'
    datos_estables=[(20, 'A'), (15, 'X'), (20, 'B'), (5, 'Y')]
    print(f"Original: {datos_estables}")
    stable_selection_sort(datos_estables)
    print(f"Ordenado (Estable): {datos_estables}")