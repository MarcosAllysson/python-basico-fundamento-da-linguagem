"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
print('\033[4;35mNÚMERO POR EXTENSO\033[m')

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')

while True:
    while True:
        ler_numero_teclado = int(input('\nQuer ver qual valor por extenso? Escolha entre 0 e 20 (apenas): '))
        if ler_numero_teclado >= 0 and ler_numero_teclado <= 20:
            break
        print('Somente entre 0 e 20.')

    print(f'O número {ler_numero_teclado} por extenso é {numero[ler_numero_teclado]}')

    while True:
        escolha = str(input('\nQuer continuar (Sim/Não)? ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Digite somente sim ou não (S/N)!')

    if escolha == 'N':
        print('Beleza, saindo...')
        break
