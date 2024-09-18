nome = str(input('Qual é seu nome? ')).strip().upper()

if nome == 'MARCOS':
    print('Que \033[1;36m nome lindo!\033[m')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'ANA BEATRIZ JOYCE MANU':
    print('Belo nome \033[1;33m feminino!\033[m')
else:
    print('Seu nome é bem \033[4;35m normal...\033[m')

print('Tenha um bom dia, \033[4m {}.'.format(nome.capitalize()))
