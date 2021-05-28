# help(print)
# interactive help
# print(input.__doc__)

# DOCSTRING
def manual(txt):
    """
    This is a function created only to print the message.
    It was created by docstring on python.
    """
    print(txt)


# help(manual)


# PARÂMETRO OPCIONAL
def somar(a, b, c=0):
    """
    -> função que retorna a soma de 3 números, sendo que o 3° parâmetro é opcional,
    e recebe 0 como padrão caso não seja recebido valor.
    :param a: recebe inteiro de um número, guardado na variável A
    :param b: recebe inteiro de um número, guardado na variável B
    :param c: recebe inteiro de um número, guardado na variável C, sendo este opcional
    :return: a soma dos 3 valores.
    """
    soma = a + b + c
    print(f'Soma dos valores é: {soma}.')


# print('Soma:', somar(1, 2))
# help(somar)


# ESCOPO DE VARIÁVEL
def funcao():
    global n1  # informo ao python utilizar a mesma variável global.
    n1 = 4  # por mais que eu tenha atribuído valor, é ignorado por estou usando a variável global
    print(f'Variável n1 dentro, vale {n1}. Pois é variável LOCAL, só existe dentro da função.')


n1 = 10
#funcao()
#print(f'Variável n1 fora, vale {n1}. Pois é variável GLOBAL, ou seja, existe fora dos métodos.')


# RETORNANDO VALORES
def somar(a, b, c=0):
    """
    -> função que retorna a soma de 3 números, sendo que o 3° parâmetro é opcional,
    e recebe 0 como padrão caso não seja recebido valor.
    :param a: recebe inteiro de um número, guardado na variável A
    :param b: recebe inteiro de um número, guardado na variável B
    :param c: recebe inteiro de um número, guardado na variável C, sendo este opcional
    :return: a soma dos 3 valores.
    """
    soma = a + b + c
    return soma


soma1 = somar(1, 2)
soma2 = somar(10, 22)
soma3 = somar(120, 90, 87)

print(f'As somas de soma1, soma2 e soma3, valem respectivamente: {soma1}, {soma2} e {soma3}.')
