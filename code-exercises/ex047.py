"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
print('\033[36mCONTAGEM DE PARES\033[m')

print('\033[mNúmeros pares entre 1 e 50 são:')

# outra opção:
# for i in range(1, 51):
#    if i % 2 == 0:
#            print(i)

for i in range(2, 51, 2):
    print(i)
# maneira acima é melhor pois economiza processamento.
