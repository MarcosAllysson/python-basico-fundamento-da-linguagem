"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
print('VALIDAÇÃO DE DADOS')

valores_corretos = 'MF'
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo? \n[M/F]: ')).strip().upper()

    if sexo in valores_corretos:
        sexo = sexo
        print('Ok.')
    else:
        print('Sexo inválido.')

print('Sexo digitado: {}.'.format(sexo))
