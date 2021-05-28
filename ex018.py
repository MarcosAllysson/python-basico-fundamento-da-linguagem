"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
casseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians
print('SENO, COSSENO E TANGENTE')
angulo = float(input('Digite um ângulo qualquer: '))
angulo_convertido = radians(angulo)
seno = sin(angulo_convertido)
coseno = cos(angulo_convertido)
tangente = tan(angulo_convertido)

print('Ângulo convertido para randiano {}, '
      'o seno vale {:.2f}, '
      'coseno {:.2f} '
      'e tangente {:.2f}.'.format(angulo_convertido, seno, coseno, tangente))
