"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""
print('AQUELE CLÁSSICA DA MÉDIA')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Você não estudou o suficiente está REPROVADO. Média {}'.format(media))
elif media <= 6.9:
    print('Passou raspando com {}, você consegue melhorar!'.format(media))
else:
    print('Parabéns, aprovado com {}! Continue estudando e sempre melhorando.'.format(media))
