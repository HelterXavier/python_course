'''
MAP
MAP é uma função que aplica uma função a todos os itens de um iterável (lista, tupla, etc.) e retorna um iterador.
O MAP é uma funlçai qyhe recebe dois parametros: O primeiro a funlçai, o segundo é um iterável.
'''
import math


# def area(r): return round(math.pi * r**2, 2)


# raios = [2, 5, 7.1, 0.3, 10, 44]
# areas = []

# areas = map(area, raios)

# print(list(areas))
# print(list(areas))

# print(type(areas))


cidades = [('Berlim', 22), ('Paris', 26),
           ('Londres', 18), ('Roma', 30), ('Madri', 16)]

print(cidades)

# f = 9/5 * c + 32


def c_to_f(data): return (data[0], round((9/5 * data[1] + 32), 2))


print(list(map(c_to_f, cidades)))
