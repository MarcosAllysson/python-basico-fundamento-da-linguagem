"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""
print('ANALISANDO TRIÂNGULOS')

reta1 = float(input('Comprimento reta 1: '))
reta2 = float(input('Comprimento reta 2: '))
reta3 = float(input('Comprimento reta 3: '))

# calculando se pode formar triângulo
if ((reta1 + reta2) > 3) and ((reta2 + reta3) > reta1) and ((reta3 + reta1) > reta2):
    if reta1 == reta2 and reta2 == reta3:
        print('Triângulo EQUILÁTERO - todos os lados iguais.')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Triângulo ESCALENO - todos os lados diferentes.')
    else:
        print('Triângulo ISÓSCELES - dois lados iguais e um diferente.')
else:
    print('As retas informadas não formam um triângulo.')
