'''
Leitura de Arquivos

Para ler é utilizado a função open() com o modo 'r' (read).
Para ler um arquivo, é necessário abrir o arquivo com a função open() e o modo 'r' (read).
'''

# # Lendo o arquivo
# arquivo = open('texto.txt')

# # readFile = arquivo.read()
# readFile = arquivo.read()

# print(readFile)


'''
Seek e Cursor

seek() => É utilizado para mover o cursor para uma posição específica no arquivo.
read() => Lê o arquivo a partir da posição atual do cursor.
write() => Escreve no arquivo a partir da posição atual do cursor.
close() => Fecha o arquivo.
'''

arquivo = open('texto.txt')

# print(arquivo.read())
# print(arquivo.read())
# Lê o arquivo e remove as vogais
# print(arquivo.read().translate(str.maketrans('', '', 'aeiouAEIOU')))

# arquivo.seek(6)

# print('Refaz a leitura a partir do sexto caractere', arquivo.read())


# print(arquivo.readline())

print(arquivo.read())

arquivo.close()
