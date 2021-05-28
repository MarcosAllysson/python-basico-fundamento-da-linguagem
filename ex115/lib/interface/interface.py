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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[31m{cont}\033[m - \033[36m{item}\033[m')
        cont += 1
    print(linha())
    opcao_menu = leiaInt('\033[32mSua opção\033[m: ')
    return opcao_menu
