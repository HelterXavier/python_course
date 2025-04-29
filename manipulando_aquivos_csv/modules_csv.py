'''
Escrevendo em arquivos CSV

reader() -> leitor
writer() -> escritor
'''
# from csv import writer

# with open('manipulando_aquivos_csv/filmes.csv', 'w') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])

#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o gênero: ')
#             duracao = input('Informe a duração (em minutos): ')
#             escritor_csv.writerow([filme, genero, duracao])


# DICTWRITER

from csv import DictWriter

with open('manipulando_aquivos_csv/filmes.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow(
                {'Título': filme, 'Gênero': genero, 'Duração': duracao})
