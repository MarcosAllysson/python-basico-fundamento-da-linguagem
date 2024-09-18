"""
Tuplas são imutáveis, uma vez criado e programa em execução, não é possível alterar valores.
Variável que armazena vários valores
"""
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# percorrendo tupla com for
for i in lanche:
    print(f'Eu vou comer {i}...')

print()
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print()
# enumerate me da tanto o valor quanto a posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# pra mostrar na ordem
print('\nTupla em ordem: ', sorted(lanche))

a = (2, 3, 4)
b = (1, 2, 2, 4)
c = a + b
print(c)

#printando quantos elementos 'x' aparece na tupla
#print(c.count(2))

# printando onde um determinado elemento aparece na tupla. Se tiver mais de um, ele mostra posição do 1°
print(c.index(2))
