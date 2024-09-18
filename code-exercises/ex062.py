"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('SUPER PROGRESSÃO ARITMÉTICA 3.0')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10 # simulando que o usuário quer mais 10 termos.

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1

    print('Pausa')
    mais = int(input('Quer mostrar quantos termos a mais? '))

print('Fim, com {} termos mostrados.'.format(total))
