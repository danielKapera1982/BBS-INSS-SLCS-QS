def min_max_selection_sort(arr):
    n = len(arr)
    inicio = 0
    fin = n - 1
    
    #bucle que solo se ejecuta hasta la mitad del arreglo
    while inicio < fin:
        indice_minimo = inicio
        indice_maximo = inicio
        
        #buscamos el min y el max en el rango actual
        for i in range(inicio, fin + 1):
            if arr[i] < arr[indice_minimo]:
                indice_minimo = i
            elif arr[i] > arr[indice_maximo]:
                indice_maximo = i
        
        #movemos el minimo al inicio
        arr[inicio], arr[indice_minimo] = arr[indice_minimo], arr[inicio]
        
        #caso especial: si el maximo estaba en la posicion 'inicio'
        #al hacer el swap anterior lo movimos a 'indice_minimo' hay que corregir el puntero
        if indice_maximo == inicio:
            indice_maximo = indice_minimo
        
        # Movemos el maximo al fianl
        arr[fin], arr[indice_maximo] = arr[indice_maximo], arr[fin]
        
        #reducimos los limites
        inicio += 1
        fin -= 1

#bloque de prueba
if __name__ == '__main__':
    datos_minmax = [29, 10, 14, 37, 13, 25, 42, 11]
    print(f"Originail: {datos_minmax}") 
    min_max_selection_sort(datos_minmax)
    print(f"Ordenado (Min - Max): {datos_minmax}") 