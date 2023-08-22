def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

def fat_recursivo_cauda(x,acc = 1):
    if x == 0:
        return acc
    else:
        return fat_recursivo_cauda(x-1,x*acc)


def fat2(x):
    return fat_recursivo_cauda(x)

print(fat(6))
print(fat2(6))