"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
print('ANÁLISE DE DADOS DO GRUPO')

pessoa_maior_18 = homem_cadastrado = mulher_menor = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '

    # enquanto resposta de continuar for diferente de Homem ou Mulher, pergunto de novo...
    while sexo not in 'HM':
        sexo = str(input('Homem ou mulher? ')).strip().upper()[0]

    # verificando quantas pessoas são maiores de 18 anos.
    if idade > 18:
        pessoa_maior_18 += 1

    # verificando se sexo foi homem, e adicionando mais um ao total
    if sexo == 'H':
        homem_cadastrado += 1

    # verificando quantas mulheres são menores de 20 anos.
    if sexo == 'M':
        if idade < 20:
            mulher_menor += 1

    # enquanto resposta de continuar for diferente de Sim ou Não, pergunto de novo...
    while continuar not in 'SN':
        continuar = str(input('Quer cadastrar outra pessoa? (SIM/NÃO)? ')).strip().upper()[0]

    # caso usuário não queira mais cadastrar usuários.
    if continuar == 'N':
        break

print(f'Tem {pessoa_maior_18} maiores de 18 anos. Dos quais {homem_cadastrado} são homens,'
      f' e {mulher_menor} mulheres menores de 20 anos.')
