def pesquisaBinaria(lista,item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lista = [1,3,5,7,9,10,11,12,13,14,15,16,17,18,19,20]

print(pesquisaBinaria(lista,14))
print(pesquisaBinaria(lista,-1))