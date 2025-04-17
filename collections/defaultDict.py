'''
Default Dict

- É Informado um valor padrão para o dicionário, caso a chave não exista.
- Pode usar um lambda ou uma função para definir o valor padrão.

OBS: Lambda é uma função anônima, ou seja, não tem nome.
- O valor padrão é retornado quando a chave não existe no dicionário.
'''

from collections import defaultdict

dicionarion = defaultdict(lambda: 'Valor padrão')
dicionarion['a'] = 1
dicionarion['b'] = 2

print(dicionarion['a'])  # Saída: 1
print(dicionarion['b'])  # Saída: 2
print(dicionarion['c'])  # Saída: Valor padrão
