"""
Dentro do pacote uteis que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

def leiaDinheiro(msg):
    valido = False

    while not valido:
        # recebendo string do input, já substituindo vírgula por ponto
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! \033[31m{entrada}\033[m é um preço inválido.')
        else:
            valido = True
            return float(entrada)
