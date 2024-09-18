"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
print('VALIDANDO EXPRESSÕES MATEMÁTICAS\n')

cont_a = cont_b = 0

expressao = str(input('Qual expressão quer analisar? '))
print('Expressão digitada:', expressao)

for i in expressao:
    if i == '(':
        cont_a += 1

    if i == ')':
        cont_b += 1

if (cont_a - cont_b) == 0:
    print('\nExpressão válida.')
else:
    print('\nExpressão inválida.')


# solução da aula - pra cada '(' encontrado, é adicionado à lista, e se ')' encontrado, removo último índice.
exp = str(input('\nQual expressão quer analisar? '))
pilha = []
for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append((')'))
            break

if len(pilha) == 0:
    print('Expressão validada corretamente.')
else:
    print('Expressão inválida.')
