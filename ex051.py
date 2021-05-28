"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.

Progressão aritmética (PA) é uma sequência numérica que possui a seguinte definição:
a diferença entre dois termos consecutivos é sempre igual a uma constante, geralmente
chamada de razão da PA. É possível, a partir apenas do primeiro termo e da razão de uma
PA, encontrar o valor de qualquer termo.
"""
print('PROGRESSÃO ARITMÉTICA')

primeiro = int(input('Primeiro elemento: '))
razao = int(input('Razão: '))

elementos = 10
ultimo = primeiro + (elementos-1) * razao # fórmula do enésimo termo de uma PA.
ultimo += 1

for i in range(primeiro, ultimo, razao):
    print(i)
