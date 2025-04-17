'''
# Named Tuple
'''
from collections import namedtuple

cachorro = namedtuple('Cachorro', 'nome raca idade')
cachorro2 = namedtuple('Cachorro', 'nome, raca, idade')
cachorro3 = namedtuple('Cachorro', ['nome', 'raca', 'idade'])

# Utilizando
cachorro1 = cachorro('Rex', 'Labrador', 5)

print(cachorro1)
