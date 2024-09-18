"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
print('Soma dos pares'.upper())

pares = 0
for i in range(1, 7):
    num = int(input('Digite valor: '))
    if num % 2 == 0:
        pares += num

print('Soma dos pares: {}'.format(pares))
