from ex115.lib.interface import interface
from ex115.lib.arquivo import arquivo
from time import sleep

"""
A) Vamos criar um menu em Python, usando modularização.
B) Vamos ver como fazer acesso a arquivos usando o Python.
C) Finalizando o projeto - cadastro de pessoas
"""

# verificando existência do arquivo
nome_arquivo = 'pessoas.txt'
if not arquivo.arquivoExiste(nome_arquivo):
    # se o arquivo não existe, então cria!
    arquivo.criarArquivo(nome_arquivo)


# programa / menu
while True:
    opcao_escolhida = interface.menu(['Consultar Pessoas', 'Cadastrar Pessoa', 'Fechar Programa'])
    if opcao_escolhida == 1:
        # Opção de listar conteúdo do arquivo!
        arquivo.lerArquivo(nome_arquivo)

    elif opcao_escolhida == 2:
        # Opção de cadastrar nova pessoa
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Digite nome: '))
        idade = interface.leiaInt('Digite idade: ')
        arquivo.cadatrarPessoa(nome_arquivo, nome, idade)

    elif opcao_escolhida == 3:
        # Opção de sair do programa
        interface.cabecalho('Ok, sistema fechando...')
        break

    else:
        # Caso opção inválida
        print('\033[31mErro! Opção inválida...\033[m ')
    sleep(1)
