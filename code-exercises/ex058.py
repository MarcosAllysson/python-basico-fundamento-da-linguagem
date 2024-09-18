"""
Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
"""
from random import randint
from emoji import emojize

print('\033[4;36mJOGO DA ADIVINHAÇÃO 2.0\033[m')
numero_computador = randint(0, 10)
numero_usuario = -1 # outra opção é aceitar Booleano: False e comparar while not numero_usuario...
numero_palpites = 0

while numero_usuario != numero_computador:
    #numero_computador = randint(0, 10)
    numero_usuario = int(input('\033[31mAdivinhe qual número estou pensando: \033[m'))

    if numero_usuario == numero_computador:
        print('\033[36mVocê acertou\033[m, eu realmente pensei no \033[1m{}\033[m, '
              'e você disse exatamente: \033[1m{}\033[m'.format(numero_computador, numero_usuario))
    elif numero_usuario < numero_computador:
        numero_palpites += 1
        print('\033[33mQuase\033[m, um pouco mais...')

        #print('\033[33mQuase\033[m, eu pensei no {}. Vai de novo.'.format(numero_computador))
        #print('\033[33mQuase\033[m, vai de novo.'.format())

    else:
        numero_palpites += 1
        print('\033[33mQuase\033[m, um pouco menos...')

# numero_palpites+1, pra incluir mais um após a verificação do número igual.
print(emojize('\nVocê precisou de {} palpites pra acertar meu número, :collision::collision::collision:!'
              .format(numero_palpites+1), use_aliases=True))
