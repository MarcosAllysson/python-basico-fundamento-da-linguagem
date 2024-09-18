"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
print('Funções aprofundadas em Python\n')


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite somente inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[36mOperação finalizada pelo usuário\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite somente inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[36mOperação finalizada pelo usuário\033[m')
            return 0
        else:
            return num


num = leiaInt('Digite um inteiro: ')
flo = leiaFloat('Digite um float: ')

print(f'O valor inteiro digitado foi {num}. E o float foi {flo}.')
