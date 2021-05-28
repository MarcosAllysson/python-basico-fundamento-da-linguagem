pessoas = {
    "nome": "Marcos",
    "sexo": "M",
    "idade": 23
}

# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} e é do sexo {pessoas["sexo"]}.')

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# del pessoas['sexo']
pessoas["nome"] = "Allysson"
pessoas["peso"] = 63
# posso usar .values(), .keys() e .items()
# for chave, valor in pessoas.items():
#    print(f'{chave}: {valor}.')


brasil2 = []
estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'siglas': 'SP'
}
brasil2.append(estado1)
brasil2.append(estado2)
# print(brasil2[0]['sigla'])

estado = dict()  # ou {}
brasil = list()  # ou []

for i in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for indice_lista in brasil:
    for chave, valor in indice_lista.items():
        print(f'O campo {chave} tem valor {valor}.')
