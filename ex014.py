"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

print('CONVERSOR DE TEMPERATURA')
celcius = float(input('Graus celcius: '))
fah = (celcius * 9/5) + 32
print('Convertendo de {}° Celcius para Fahrenheit, fica {:.0f} °F.'.format(celcius, fah))
