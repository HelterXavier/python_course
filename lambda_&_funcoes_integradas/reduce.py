'''
REDUCE -> Função que aplica uma função cumulativa a um iterável, reduzindo-o a um único valor.
'''

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]


def multi(x, y): return x*y


res = reduce(multi, dados)
print(res)
