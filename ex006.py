"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

print('DOBRO, TRIPLO E RAIZ QUADRADA')
numero = int(input('Digite um valor: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

#print('Seu número: {}, o dobro vale {}, triplo vale {} e a raiz quadrada {}.'.format(numero, numero*2, numero*3, numero**2))
#print('Seu número: {}, o dobro vale {}, triplo vale {} e a raiz quadrada {:.2f}.'.format(numero, numero*2, numero*3, pow(numero, (1/2))))
print('Seu número: {}, o dobro vale {}, triplo vale {} e a raiz quadrada {:.2f}.'.format(numero, dobro, triplo, raiz_quadrada))

# posso usar pow(numero, (1/2)) pro cálculo da raiz quadrada.
