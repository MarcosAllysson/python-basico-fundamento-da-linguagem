"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
print('\033[36mMATRIZ EM PYTHON\033[m \n')

# montando e atribuindo 0 à matriz para serem trocados pelos valores lidos no teclado
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 0 a 3 porque são 3 linhas x 3 colunas
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira valor para [{linha}, {coluna}]: '))

print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
