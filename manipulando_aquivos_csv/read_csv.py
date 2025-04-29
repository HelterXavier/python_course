'''
Lendo arquivos CSV

CSV - Comma Separeted Values
'''

# with open('manipulando_aquivos_csv/lutadores.csv', encoding='utf-8') as arquivo:
#     data = arquivo.read()
#     data = data.split(',')[2:]
#     print(data)


# IDEAL COM READER
# from csv import reader

# with open('manipulando_aquivos_csv/lutadores.csv', encoding='utf-8') as arquivo:
#     leitor_csv = reader(arquivo)
#     next(leitor_csv)
#     for linha in leitor_csv:
#         print(
#             f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetro')


# IDEAL COM DICTREADER
from csv import DictReader

with open('manipulando_aquivos_csv/lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(
            f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetro')
