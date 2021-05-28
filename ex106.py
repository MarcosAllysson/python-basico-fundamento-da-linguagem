"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""
from time import sleep
print('INTERACTIVE HELP SYSTEM IN PYTHON\n')

while True:
    comando = str(input('\033[1;30;43mManual do Interactive Help do Python! '
                        '\n"FIM" para encerrar. '
                        '\nDigite o comando: ')).strip().lower()

    if comando == 'fim':
        print('\033[30;43mSaindo da tela interativa...')
        sleep(2)
        break

    print(f'\033[1;30;43m\nAcessando manual do {comando}...\033[m')
    sleep(1.5)
    print(f'\033[30;42m{help(comando)}\033[m')
