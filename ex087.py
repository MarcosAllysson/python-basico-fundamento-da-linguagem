"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
print('MAIS SOBRE MATRIZ EM PYTHON\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

# 0 a 3 porque são 3 linhas x 3 colunas
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'\033[36mDigite valor para\033[m \033[4;31m[ {linha}, {coluna} ]\033[m: '))

print('\n \033[4mMATRIZ 3X3:\33[m')
for linha in range(0, 3):
    for coluna in range(0, 3):
        # analisando pares e somando
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        # printando matriz
        print(f'\033[35m[ {matriz[linha][coluna]:^5} ]\033[m', end='')

    # só pra quebrar linha
    print()

print(f'\n \033[1;34mSoma dos pares\033[m: {soma_pares}.')

# somando elementos da 3° coluna:
for linha in range(0, 3):
    # somo apenas [0,2], [1,2], [2,2]
    soma_terceira_coluna += matriz[linha][2]

# soma 3° coluna
print(f'\033[1;34mSoma da 3° coluna é\033[m: {soma_terceira_coluna}')

# valor mais alto da 2° linha:
for coluna in range(0, 3):
    # analisando apenas colunas [1,0], [1,1], [1,2] da mesma linha: 1
    if coluna == 0:
        maior_segunda_linha = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maior_segunda_linha:
            maior_segunda_linha = matriz[1][coluna]

# printando maior númeo da 2° linha:
print(f'\033[1;34mMaior número da 2° linha é\033[m: {maior_segunda_linha}.')
