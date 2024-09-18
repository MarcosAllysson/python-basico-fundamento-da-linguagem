"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
from time import sleep
print('FUNÇÃO PARA FATORIAL\n')

def fatorial(numero=1, show=False):
    """
    Função que efetua cálculo do fatorial de um número, e também tem opção de mostrar o processo do cálculo
    Fatorial é calculado pelo número x o antecessor, até que chegue a 0.
    Exercício resolvido usando laço de repetição: for.
    :param numero: inteiro a receber pela função para calcular fatorial
    :param show: exibir ou não o processo do cálculo
    :return: o fatorial do número, seguido, ou não, do processo de cálculo.
    """
    print(f'Calculando fatorial de {numero}...')
    sleep(1)

    cont_fatorial = 1
    for i in range(numero, 0, -1):
        cont_fatorial *= i

        # se show for True
        if show:
            print(f'{i}', end='')

            # se o contador for maior que 1, printa x -> i x i x i...
            if i > 1:
                print(' x ', end='')
            # se não, sendo o último, printa sinal de igual i x i = ...
            else:
                print(' = ', end='')

    return cont_fatorial


numero_usuario = int(input('Quer calcular o fatorial de qual número? '))
while True:
    escolha_usuario = str(input(f'Quer ver o processo de cálculo do fatorial de {numero_usuario}, (Sim/Não)? ')).strip().upper()[0]
    if escolha_usuario in 'SN':
        break
    print('Digite somente S ou N!')

if escolha_usuario == 'S':
    print(fatorial(numero_usuario, True))
else:
    # por padrão, já é False.
    print(fatorial(numero_usuario))

#help(fatorial)
