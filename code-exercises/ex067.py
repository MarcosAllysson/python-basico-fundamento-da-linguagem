"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
print('{:=^74}'.format('TABUADA 3.0'))

# loop infinido pra parar somente quando número negativo for digitado
while True:
    tabuada = int(input('Quer saber a tabuada de qual número \033[36m(digite valor negativo para parar)\033[m: '))

    # verificando se número é negativo
    if tabuada < 0:
        # se for, programa para.
        break

    # tabuada com while
    #cont = 0
    #print(f'\033[1;35mTabuada de {tabuada}\033[m')
    #while cont < 11:
    #    print(f'{tabuada} x {cont} = {tabuada * cont}')
    #    cont += 1

    # tabuada com for
    print(f'\033[1;35mTabuada de {tabuada}\033[m')
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada * i}')

    # imprimindo tabuada do número do usuário de forma mais trabalhosa.
    #print(f"""
    #    {tabuada} x 0 = {tabuada * 0}
    #    {tabuada} x 1 = {tabuada * 1}
    #    {tabuada} x 2 = {tabuada * 2}
    #    {tabuada} x 3 = {tabuada * 3}
    #    {tabuada} x 4 = {tabuada * 4}
    #    {tabuada} x 5 = {tabuada * 5}
    #    {tabuada} x 6 = {tabuada * 6}
    #    {tabuada} x 7 = {tabuada * 7}
    #    {tabuada} x 8 = {tabuada * 8}
    #    {tabuada} x 9 = {tabuada * 9}
    #    {tabuada} x 10 = {tabuada * 10}
    #    """)

print('Número negativo digitado, programa finalizado =D')
