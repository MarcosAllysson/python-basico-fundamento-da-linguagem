"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print('\033[31mLISTA DE PREÇOS COM TUPLA\033[m \n')

produtos = ('PC', 2500,
            'Fone', 320,
            'Relógio', 25000,
            'Terno', 12000,
            'Bike', 540,
            'Celular', 9000,
            'Mouse', 15)

for posicao in range(0, len(produtos)):
    # se o índice for par, mostra somente os produtos, alinhados à esquerda
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')

    # se o índice for par, mostra somente os preços, alinhados à direita
    else:
        print(f'R$ {produtos[posicao]:>10.2f}')
