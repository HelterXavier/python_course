'''
List Comprehension em Python
É uma forma rápida de criar listas a partir de iteráveis
'''
# print(list(range(10)))

# SEM LIST COMPREHENSION
# lista = []
# for numero in range(10):
#     lista.append(numero)

# print(lista)

#  COM LISTA COMPREHENSION
# lista = [numero * 2 for numero in range(10)]
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos]

print(*novos_produtos, sep='\n')
