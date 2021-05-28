"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
print('UNINDO DICIONÁRIOS E LISTAS\n')

pessoas = {}
lista_pessoas = []
tot_pessoas = 0

while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()

    while True:
        pessoas['sexo'] = str(input('Sexo: (M/F): ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Somente digite Masculino (M) ou Feminino (F)!')

    pessoas['idade'] = int(input('Idade: '))

    # adicionando dicionário à lista via cópia
    lista_pessoas.append(pessoas.copy())

    # somando 1 ao total de pessoas cadastrados
    tot_pessoas += 1

    # opção de adicionar mais pessoas
    while True:
        opcao = str(input('Quer adicionar outra pessoa? (Sim/Não): ')).strip().upper()[0]
        print() # só pra quebrar linha
        if opcao in 'SN':
            break
        print("Digite somente Sim ou não (S/N)!")

    if opcao == 'N':
        break

# Calculando média de idade. Cada índice da lista retona dicionário, basta acessar cada chave/valor pra somar.
media_idade = 0
soma_idade = 0
for indice_lista in lista_pessoas:
    soma_idade += indice_lista["idade"]

media_idade = soma_idade / tot_pessoas
print(f'\nMédia das idades: [{media_idade:.2f}] anos.')


# Uma lista com as mulheres
print('\nAs mulheres da lista são: ')
for pessoa in lista_pessoas:
    if pessoa["sexo"] == 'F':
        print(f' - [{pessoa["nome"]}]')


# Uma lista de pessoas com idade acima da média
print('\nPessoas com idade acima da média: ')
for pessoa in lista_pessoas:
    if pessoa["idade"] > media_idade:
        print(f' - {pessoa["nome"]}, que tem {pessoa["idade"]} anos, do sexo {pessoa["sexo"]}')


#print(lista_pessoas)
print(f'\nForam cadastrados - [{tot_pessoas}] pessoas.')
