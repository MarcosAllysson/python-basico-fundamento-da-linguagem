"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
print('\033[34mÍNDICE DE MASSA CORPORAL\033[m')

peso = float(input('\033[1;31mQual seu peso?\033[m '))
altura = float(input('\033[1;31mQual sua altura?\033[m '))

# É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
calculo_imc = peso / (altura ** 2)
print('\033[1;36mSeu IMC é:\033[m {:.2f}.'.format(calculo_imc))

if calculo_imc < 18.5:
    print('Abaixo do peso.')
elif calculo_imc >= 18.5 and calculo_imc <= 25:
    print('Peso ideal.')
elif calculo_imc > 25 and calculo_imc <= 30:
    print('Sobrepeso.')
elif calculo_imc > 30 and calculo_imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
