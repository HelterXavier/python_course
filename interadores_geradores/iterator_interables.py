'''
Entendo Interadores e Iteráveis


Interator:
          -> Um objeto que implementa o protocolo de iteração, ou seja, possui os métodos __iter__ e __next__.
          -> Um iterador é um objeto que pode ser percorrido, ou seja, você pode obter os elementos um a um.

Iterables:
          -> Um objeto que pode ser iterado, ou seja, você pode obter um iterador a partir dele.
          -> Um iterável é um objeto que possui o método __iter__, que retorna um iterador.
          -> Um iterável pode ser uma lista, tupla, dicionário, conjunto, string, etc.
'''

# nome = 'Lucas'  # String é um iterável
# numeros = [1, 2, 3, 4, 5]  # Lista é um iterável
# tupla = (1, 2, 3, 4, 5)  # Tupla é um iterável
# dicionario = {'a': 1, 'b': 2, 'c': 3}  # Dicionário é um iterável
# conjunto = {1, 2, 3, 4, 5}  # Conjunto é um iterável

# # Interavel
# for numero in numeros:
#     print(numero)


lista = [1, 2, 3]

# Isso é um iterável
print(hasattr(lista, '__iter__'))  # True
print(hasattr(lista, '__next__'))  # False

# Criando um iterador a partir do iterável
iterador = iter(lista)

print(hasattr(iterador, '__iter__'))  # True
print(hasattr(iterador, '__next__'))  # True

# Consumindo os valores manualmente
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
# print(next(iterador))  # Erro: StopIteration
