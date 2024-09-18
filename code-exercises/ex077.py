"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
print('\033[31mCONTANDO VOGAIS EM TUPLA\033[m \n')

palavras = ('Bolsa', 'Dinheiro',
            'Oportunidade', 'Jesus',
            'Prosperidade', 'Abundância',
            'Família', 'Conexões',
            'Riqueza', 'Conhecimento',
            'Sabedoria', 'Amor',
            'Networking', 'Livros', 'Grátis')

for i in palavras:
    print(f'Palavra: \033[4;36m{i}\033[m, \033[4mtêm as vogais\033[m: ', end=' ')

    if 'a' or 'á' in i.lower():
        print('a', end=', ')
    if 'e' in i.lower():
        print('e', end=', ')
    if 'i' in i.lower():
        print('i', end=', ')
    if 'o' in i.lower():
        print('o', end=', ')
    if 'u' in i.lower():
        print('u', end=', ')
    print()
