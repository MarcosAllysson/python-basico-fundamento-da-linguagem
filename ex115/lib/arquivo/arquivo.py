from ex115.lib.interface import interface


def arquivoExiste(nome_arquivo):
    try:
        nome_arquivo = open(nome_arquivo, 'rt')  # read text
        nome_arquivo.close()
    except Exception as error:
        print(f'Erro: {error}')
        return False
    else:
        return True


def criarArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+')  # write text, + -> caso não encontrar, então cria o arquivo.
        arquivo.close()
    except Exception as error:
        print(f'Erro na criação -> {error}')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')


def lerArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except Exception as error:
        print(f'Erro ao ler o arquivo: {error}')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadatrarPessoa(nome_arquivo, nome='unknown', idade=0):
    try:
        arquivo = open(nome_arquivo, 'at')  # append text
    except Exception as error:
        print(f'Erro na abertura do arquivo: {error}')
    else:
        try:
            arquivo.write(f'{nome.title()};{idade}\n')
        except:
            print('Erro ao tentar cadastrar pessoa no arquivo de txt.')
        else:
            print(f'Registro de nome: {nome} e idade: {idade} anos, criado!')
            arquivo.close()
