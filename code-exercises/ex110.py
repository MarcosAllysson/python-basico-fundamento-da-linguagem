from uteis import moeda_2

"""
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
print('Reduzindo ainda mais seu programa\n'.title())

preco = float(input('Digite o valor: R$ '))
print(moeda_2.resumo(preco, 13, 10))

#help(moeda_2.resumo)
