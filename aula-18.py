teste = []
teste.append('Marcos')
teste.append(23)

galera = []
galera.append(teste[:])

teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])

#galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 12], ['Maria', 23]]

#print(galera)
#print(galera2[2][1])

#for pessoa in galera2:
#    print(f' O {pessoa[0]} tem {pessoa[1]} anos de idade.')

galera2 = []
dado = []

for i in range(1, 4):
    dado.append(str(input('Qual nome: ')))
    dado.append(int(input('Qual idade: ')))

    galera2.append(dado[:]) # fazendo cópia da lista de dado pra galera
    dado.clear() # deletando lista de dados a cada iteração.

#print(galera2)

for pessoa in galera:
    if pessoa[1] > 20:
        print(f'{pessoa[0]} tem mais de 20 anos.')
    else:
        print(f'{pessoa[0]} é menor de idade.')
