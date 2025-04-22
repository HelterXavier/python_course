'''
Zip -> Função embutida que combina dois ou mais iteráveis (listas, tuplas, etc.) em um único iterável de tuplas.
'''

# Exemplo 1: Usando zip com listas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]
# Usando zip para combinar as listas
resultado = zip(lista1, lista2, lista3)
# Convertendo o resultado para uma lista
resultado_lista = list(resultado)
print(resultado_lista)  # Saída: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
