"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
print('VÁRIOS NÚMEROS COM FLAG')

# inicializando variável contador e soma com 0.
cont_digitados = soma = 0

# Loop infinito pra que seja parado somente quando 999 for digitado. Assim não preciso comparar com outro valor.
while True:
    numeros = int(input('Digite um valor \033[31m(para parar, digite 999)\033[m: '))
    if numeros == 999:
        break
    else:
        cont_digitados += 1
        soma += numeros

print(f'Foram digitados \033[4m{cont_digitados}\033[m e a soma total é \033[4m{soma}.\033[m')
