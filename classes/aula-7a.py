# Operadores aritméticos
#nome = input('Qual seu nome? ')

# com :20, o último caracter, no caso o !, vai ser impresso depois de 20 espaços.
#print('Prazer te conhecer {:20}!'.format(nome))

# com :>20, o último caracter, no caso o !, vai ser impresso alinha à direita depois de 20 espaços.
#print('Prazer te conhecer {:>20}!'.format(nome))

# com :^20, o último caracter, no caso o !, vai ser impresso no centro depois de 20 espaços.
#print('Prazer te conhecer {:^20}!'.format(nome))

# com :=^20, o último caracter, no caso o !, vai ser impresso no centro, rodeado por = depois de 20 espaços.
#print('Prazer te conhecer {:=^20}!'.format(nome))

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
soma = n1 + n2
multi = n1 * n2
divisao = n1 / n2
div_inteira = n1 // n2
exponenciacao = n1 ** n2

# {.2f}, irá imprmir apenas 2 casas após a vírgula
# .format(soma, multi, divisao), end=' ', faz com que ao final da linha o print() não quebre linha
# \n -> quebra linha
print('A soma vale: {:=^20}, \nO produto é: {:=^20}, \nA divisão é: {:=^20.2f}.'.format(soma, multi, divisao))
print('Divisão inteira: {:=^20}, \nExponenciação: {:=^20}.'.format(div_inteira, exponenciacao))
