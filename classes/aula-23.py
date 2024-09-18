x = 'valor da variável'
try:
    print('\033[36mTry bem sucedido! \033[m')
    print(f'\033[31m{x}\033[m')
#except Exception as error:
except NameError:
    print('Variável não definida')
    #print(f'Vixe, deu não! Resolver {error.__class__}')
else:
    print('Boa, funcionou - \033[36mElse!\033[m')
finally:
    print('Volte sempre - \033[36m Finally! \033[m')