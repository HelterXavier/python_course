#  3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.

def maior_valor(list: list[int]) -> int:
    maior = list[0]
    for i in list:
        if i > maior:
            maior = i
    return maior


print(maior_valor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
