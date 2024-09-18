"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""
print('UM PRINT ESPECIAL\n')


def escreva(txt):
    print('~' * int(len(txt) + 4))  # +4 pra ter uma borda e texto centralizado
    print(f'  {txt}')  # 2 espaços em branco pra centralizar.
    print('~' * int(len(txt) + 4))


escreva('Marcos Allysson')
escreva('Olá Mundo!')
escreva('Oi')
