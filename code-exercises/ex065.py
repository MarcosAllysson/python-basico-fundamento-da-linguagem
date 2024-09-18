"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
"""
print('MAIOR E MENOR VALORES')

resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? S/N? ')).strip().upper()[0]

media = soma / quant
print('Foram digitados {} números, e a média vale {:.2f}.'.format(quant, media))
print('Maior digitado {}, e o menor, {}.'.format(maior, menor))
