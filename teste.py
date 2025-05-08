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


# def nb_year(p0, percent, aug, p):
#     years = 0
#     inhabitants: int = p0

#     while inhabitants < p:
#         inhabitants += int(inhabitants * (percent / 100)) + aug
#         years += 1

#     return years


# print(nb_year(1000, 2, 50, 1200))


# def narcissistic(value):
#     num: int = len(str(value))

#     digitos = [int(d) for d in str(value)]

#     soma: int = 0
#     for n in digitos:
#         soma += n ** num

#     result = soma

#     if result == value:
#         return True
#     else:
#         return False


# print(narcissistic(4887))


# def unique_in_order(sequence):

#     if isinstance(sequence, str):
#         sequence = sequence.replace(',', '').replace(' ', '')

#     result = []
#     previous = None
#     for item in sequence:
#         if item != previous:
#             result.append(item)
#             previous = item
#     return result


# print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D' , B]
# print(unique_in_order('ABBCcAD'))  # ['A', 'B', 'C', 'D', 'c', 'A', 'D']
# print(unique_in_order('1, 2, 2, 3, 3'))     # ['1', '2', '3']
# print(unique_in_order('1, 2, 2, 3, 3'))     # ['1', '2', '3']


# def open_or_senior(data):

#     output = []
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
#             result = "Senior"
#         else:
#             result = "Open"
#         output.append(result)

#     return output


# print(open_or_senior(
#     [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

# print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))


def friend(x):
    words = x[:]
    for f in x:
        if len(str(f)) > 4 or len(str(f)) < 4:
            words.remove(f)
    return words


print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))
