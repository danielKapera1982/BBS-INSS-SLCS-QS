def selection_sort_basico(arr):
    n = len(arr)
    
    #iteramos todo el arreglo
    for i in range(n):
        #Asumimos que el primer elemento no ordenado es el minimo
        indice_minimo = i
        
        #Buscanos en el resto del arreglo si hay un elemento menor
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j # actualizamos la posicion del nuevo minimo
                
        # Intercambiamos el minimo encontrado con el primer elemento no ordenado
        #(solo hacemos un swap por iteracion externa)
        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

# bloque de prueba
if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11]
    print(f"Originail: {datos}")
    selection_sort_basico(datos)
    print(f"Ordenado: {datos}") 