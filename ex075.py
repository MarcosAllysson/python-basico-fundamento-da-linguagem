"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
print('ANÁLISE DE DADOS EM TUPLA')

total9 = 0
pares = []

numero1 = int(input(f'Digite 1° número: '))
numero2 = int(input(f'Digite 2° número: '))
numero3 = int(input(f'Digite 3° número: '))
numero4 = int(input(f'Digite 4° número: '))

numeros = (numero1, numero2, numero3, numero4)

for i in numeros:
    if i == 9:
    # outra opção: usar count(9)
        total9 += 1
    if i % 2 == 0:
        pares.append(i)

print(f'\nNúmero 9 apareceu {total9}x;'
      f'\nNúmeros pares digitados foram: {pares}.')

if 3 in numeros:
    print(f'Número 3 apareceu na {numeros.index(3)+1}° posição')
else:
    print('Número 3 não consta na tupla.')
