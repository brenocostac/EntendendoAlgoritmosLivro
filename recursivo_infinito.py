def regressivo(i):
    print(i)
    if i <= 1:
        return
    else:
        regressivo(i-1)

regressivo(10)