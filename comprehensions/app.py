'''
LIST COMPREHENSION

- List comprehension é uma maneira concisa de criar listas em Python.
- Ele permite que você crie uma nova lista aplicando uma expressão a cada item de uma sequência existente, como uma lista ou um intervalo.
- A sintaxe básica é: [expressão for item in sequência if condição].
'''
# numeros = [1, 2, 3, 4, 5]

# Processa numero * 10 para cada numero na lista numeros
# res = [numero * 10 for numero in numeros]

# print(res)  # [10, 20, 30, 40, 50]

# LOOP
numeros = [1, 2, 3, 4, 5]

# numeros_sobrados = []
# for numero in numeros:
#     numeros_sobrado = numero * 2
#     numeros_sobrados.append(numeros_sobrado)

# print(numeros_sobrados)


# def numeros(*args):
#     res = [n * 10 for n in args]
#     return res


# print(numeros(1, 2, 3, 4, 5))
