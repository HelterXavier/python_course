'''
With -> Passo para se usar o with, não é necessário fechar o arquivo, pois o próprio with fecha o arquivo automaticamente.

1 -> Abrimos o arquivo
2 -> Manipulamos o arquivo
3 -> Fechamos o arquivo
4 -> O with fecha o arquivo automaticamente, mesmo que ocorra um erro durante a manipulação do arquivo.

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o block with
'''

with open('texto.txt') as arquivo:
    print(arquivo.read())
