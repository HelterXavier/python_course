# Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
# possui.

valores = []
pares: int = 0

print('Digite 10 valores:')

for i in range(6):
    numero = int(input(f'Valor {i+1}: '))
    valores.append(numero)

print(valores)


for i in valores:
    if i % 2 == 0:
        pares += 1

print(f'Quantidade de valores pares: {pares}')
