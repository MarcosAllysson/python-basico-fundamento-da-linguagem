#cont = 1
#while True: # executa indeterminadamente ou para no break ou flag (condição de parada)
#while cont <= 10:
#    print(cont, ' ', end='')
#    cont += 1
#print('Finish')

n = s = 0
while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    s += n
#print('Finish. The sum of values is: {}.'.format(s))
print(f'Finish. The sum of numbers provided is: {s}')
