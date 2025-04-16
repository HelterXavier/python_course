'''
Dicionátios -> dict

Dicionários são mutáveis
Dicionários são indexados por chaves, não por números
Dicionários são representados por chaves {}

print(type({}))

'''

paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'fr': 'França'
}

print(paises.keys())
print(type(paises))

print(paises['br'])
print(paises.get('br'))
