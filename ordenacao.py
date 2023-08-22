def buscarMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1,len(arr)):
        if menor > arr[i]:
            menor = arr[i]
            menor_indice = i

    return menor_indice

def ordenacao(arr):
    novo_arr = []
    for i in range(0,len(arr)):
        menor = buscarMenor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

arr = [2,65,7,8,40,20,34,54,76,45,33,23,45,78,9,0,2,3,23,4,4,432]
 
print(ordenacao(arr))