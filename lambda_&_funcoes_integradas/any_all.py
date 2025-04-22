'''
Any e All
- any: Retorna True se algum elemento do iterável for verdadeiro.
- all: Retorna True se todos os elementos do iterável forem verdadeiros.
- Ambos podem ser usados com listas, tuplas, conjuntos e dicionários.
- Exemplo:
# any([0, 1, 2]) -> True (pois 1 e 2 são verdadeiros)
# all([0, 1, 2]) -> False (pois 0 é falso)
'''

# print(all([0, 1, 2, 3, 4]))  # False, O número 0 é considerado falso

nomes_c = ['Carlos', 'Camila', 'Caio', 'Cristiane', 'Helter']

# # True se todos os nomes começam com 'C'
print(all([nome[0] == 'C' for nome in nomes_c]))

# True se algum nome começa com 'C'
print(any([nome[0] == 'C' for nome in nomes_c]))
