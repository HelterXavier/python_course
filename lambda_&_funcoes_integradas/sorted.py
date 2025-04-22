'''
Sorted -> Função que ordena os elementos de um iterável.
sorted(iterable, key=None, reverse=False) -> list
# sorted() -> Retorna uma lista ordenada a partir de um iterável.
# key -> Função que serve como critério de ordenação.
# reverse -> Se True, a lista é ordenada em ordem decrescente.
# sorted() -> Retorna uma nova lista ordenada, não altera o iterável original.
# sorted() -> Pode ser usado com qualquer iterável, como listas, tuplas, strings, dicionários, etc.
# sorted() -> A função sorted() é uma função embutida em Python que permite ordenar os elementos de um iterável, como listas, tuplas, strings, dicionários, etc. Ela retorna uma nova lista ordenada, sem modificar o iterável original.
'''

numeros = {6, 1, 8, 2}

# sorted() -> Retorna uma nova lista ordenada.

convert = sorted(numeros)  # [1, 2, 6, 8]
print(type(convert))  # <class 'list'>
print(convert)  # [1, 2, 6, 8]

# Converter para tupla
convert = tuple(sorted(numeros))  # (1, 2, 6, 8)
print(type(convert))  # <class 'tuple'>
print(convert)  # (1, 2, 6, 8)

convert_to_set = set(sorted(numeros))  # {1, 2, 6, 8}
print(type(convert_to_set))  # <class 'set'>
print(convert_to_set)  # {1, 2, 6, 8}
