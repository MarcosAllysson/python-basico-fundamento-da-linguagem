from uteis import moeda_2

"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.
"""
print('Formatando Moedas em Python\n')

valor = float(input('Informe um valor: R$ '))
print(moeda_2.aumentar(valor, 10))
print(moeda_2.diminuir(valor, 10))
print(moeda_2.dobro(valor))
print(moeda_2.metade(valor))

"""
print(help(moeda.dobro()))
print(help(moeda.metade()))
print(help(moeda.diminuir()))
print(help(moeda.aumentar()))
"""
