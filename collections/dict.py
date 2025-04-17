'''
Dicionátios -> dict

Dicionários são mutáveis
Dicionários são indexados por chaves, não por números
Dicionários são representados por chaves {}

print(type({}))

'''

# paises = {
#     'br': 'Brasil',
#     'eua': 'Estados Unidos',
#     'fr': 'França'
# }

# print(paises.keys())
# print(type(paises))

# print(paises['br'])
# print(paises.get('br'))


'''
MAPAS -> dict
'''

receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300
}

print(receita)

# for chave in receita:
#     print(chave)

# for valor in receita:
#     print(receita[valor])

# print(receita.keys())
# for chave in receita.keys():
#     print(receita[chave])


# Acessando valores
# print(receita.values())

# for valor in receita.values():
#     print(valor)


# Desempacotamento de dicionários

# for chave, valor in receita.items():
#     print(chave, valor)

# print(sum(receita.values()))
# print(max(receita.values()))
# print(min(receita.values()))
# print(len(receita))
