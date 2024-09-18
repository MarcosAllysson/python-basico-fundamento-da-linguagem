"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
print('TABUADA 2.0')

numero = int(input('Digite um número: '))

print()
print('-'*11)
for i in range(1, 11):
    print('{} x {} = {}'.format(numero, i, numero * i))
print('-'*11)
