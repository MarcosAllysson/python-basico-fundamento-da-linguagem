"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import requests
print('Site está acessível?\n')


def siteIsAvailable(url):
    try:
        site_pudim = requests. get(f'{url}')
    except Exception as error:
        print('Site não acessível')
        print(f'Erro -> {error}')
    else:
        print(f'Site: \033[4;33m{url}\033[m, está acessível. Retornou status code: {site_pudim}')
        #print(site_pudim.content)


siteIsAvailable(('http://pudim.com.br/'))
