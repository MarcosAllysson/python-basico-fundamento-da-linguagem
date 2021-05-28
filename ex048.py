"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
"""
print('\033[1;31mSOMA ÍMPARES MÚLTIPLOS DE 3\033[m')

soma = 0
qnt = 0

# começando do 3, até o 500, pulando de 3 em 3. Economizar processamento e conto ímpares múltiplos de 3
for cont in range(3, 501, 3):
    #if cont % 2 != 0:
    if cont % 3 == 0:
        soma += cont
        qnt += 1
print('\033[36mSoma de todos os {} múltiplos de 3, entre 1 e 500:\033[m \033[4m{}.\033[m'.format(qnt, soma))
