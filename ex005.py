"""
Faça um programa que leia um número inteiro e mostre na tela o sucessor e seu antecessor
"""

print('SUCESSOR E ANTECESSOR')
numero = int(input('Digite um valor: '))
sucessor = numero + 1
antecessor = numero - 1

#print('O sucessor de {:=^5} é {:=^5}, e o antecessor é {:=^5}.'.format(numero, numero+1, numero-1))
print('O sucessor de {:=^5} é {:=^5}, e o antecessor é {:=^5}.'.format(numero, sucessor, antecessor))

