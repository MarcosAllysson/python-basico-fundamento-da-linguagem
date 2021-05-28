from uteis import moeda

"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
print('Exercitando módulos em Python\n'.title())

valor = float(input('Informe um valor: R$ '))
print(moeda.aumentar(valor, 10))
print(moeda.diminuir(valor, 10))
print(moeda.dobro(valor))
print(moeda.metade(valor))

"""
print(help(moeda.dobro()))
print(help(moeda.metade()))
print(help(moeda.diminuir()))
print(help(moeda.aumentar()))
"""
