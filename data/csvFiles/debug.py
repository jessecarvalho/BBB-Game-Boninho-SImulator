from random import randint

def sorteio():
    sorteado = randint(0,15)
    return sorteado

def a():
    i = 0
    lista = []
    while i < 3:
        newSorteado = sorteio()
        print(newSorteado)
        if newSorteado in lista:
            pass
        else:
            lista.append(newSorteado)
            i += 1
    print(lista)

a()