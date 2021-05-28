num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 0)
num.pop(2)
if 7 in num:
    num.remove(7)
else:
    print('Não achei número 4.')
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

print('\nVarrendo com for')
for c, v in enumerate(num):
    print(f'Na posição {c}, encontrei o valor {v}...')
print('Terminei de verificar a lista.')