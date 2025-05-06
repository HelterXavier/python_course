# def get_sum(a, b):
#     if a <= b:
#         numbers = list(range(a, b + 1))
#     elif a >= b:
#         numbers = list(range(a, b - 1, -1))

#     soma = sum(numbers)

#     return soma


# print(get_sum(0, 1))
# print(get_sum(0, -1))


'''
A POPULAÇÃO TEM p0 = 1000 HABITANTES NO INÍCIO DO ANO.
A POPULAÇÃO AUEMENTA 2% (0.2) CADA ANO.
A CIDADE RECEBE 50 NOVOS HABITANTES
RETORNA QUANTO TEMPO
'''


def nb_year(p0, percent, aug, p):
    years = 0
    inhabitants: int = p0

    while inhabitants < p:
        inhabitants += int(inhabitants * (percent / 100)) + aug
        years += 1

    return years


print(nb_year(1000, 2, 50, 1200))
