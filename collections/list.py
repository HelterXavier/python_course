# LIST -> VETORES/MATRIZES (ARRAYS)
# DINÂMICO E PODE SER COLOCADO QUALQUER TIPO DE DADOS

# - DINÂMICO: Não possui tamanho fico
# Pode criar a lista e simplesmente adicionar mais elementos com qualquer tipo de dado

# List

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['H', 'e', 'l', 't', 'e', 'r', 'X', 'a', 'v', 'i', 'e', 'r']
list3 = []
lista4 = list(range(11))
lista5 = list('Helter Xavier')

# Checar se um valor está na lista
# if 8 in lista1:
#     print('Valor 8 está na lista')
# else:
#     print('O valor 8 não está na lista')

# ORDERNAR NÚMEROS
# lista1.sort()
# print(lista1)

# Contar nnúmero de ocorrências de um valor em uma lista
# print(lista1.count(1))
# print(lista2.count('e'))

# Inserir um novo elemento na lista informado a posição do índice
# lista1.insert(2, 'Novo valor')
# print(lista1)

# Juntar duas listas
# lista6 = lista1 + lista2
# print(lista6)

# lista1.extend(lista2)
# print(lista1)


# Lista reversa
# print(lista1[::-1])
# lista1.reverse()
# print(lista1)

# Remover elemento da lista
print(lista5)
lista5.pop()
lista5.pop(0)
print(lista5)
