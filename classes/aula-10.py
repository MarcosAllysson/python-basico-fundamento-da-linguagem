#nome = str(input('Qual é seu nome? '))
#if nome == 'Marcos':
#    print('Que nome lindo!')
#else:
#    print('Seu nome é tão normal...')
#print('Bom dia, {}.'.format(nome))

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

print('A sua média foi {:.1f}'.format(media))

#condição simplificada
print('Parabéns' if media >= 6 else 'Estude mais!')

#if media >= 6:
#    print('Média boa, parabéns!')
#else:
#    print('Média não esperada, continue estudando.')
