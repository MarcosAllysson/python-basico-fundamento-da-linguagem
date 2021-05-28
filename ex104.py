"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
"""
print('VALIDANDO ENTRADA DE DADOS EM PYTHON\n')


def leiaInt(msg):
    ok = False
    valor = 0

    while True:
        num = str(input(msg))
        #print(num)
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'\033[1;31mDigite número válido!\033[m')
        if ok:
            break

    return valor


num = leiaInt('Digite um número: ')
print(f'Você digitou número {num}.')
