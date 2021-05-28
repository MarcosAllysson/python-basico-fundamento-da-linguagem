def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B = {a + b}')


# Programa principal
#soma(4, 5)


def contador(* num):
    soma = 0
    for i in num:
        soma += i
    print(f'Somando {num} temos {soma}.')


contador(2, 1, 7)
contador(8, 0)
contador(5, 4, 2, 9)



def dobra(lista):
    cont = 0
    while cont < len(lista):
        lista[cont] *= 2
        cont += 1


lista = [2, 3, 4, 5, 6, 9]
dobra(lista)
#print(lista)
