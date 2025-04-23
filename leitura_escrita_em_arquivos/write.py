'''
Escrever em arquivos

1 -> Abrir o arquivo
2 -> Abrir para escrita e não leitura
3 -> Quando é escrito o arquivo, o conteúdo anterior é apagado
4 -> Se o arquivo não existir, ele será criado
'''


# with open('write.txt', 'w') as arquivo:
#     arquivo.write('Escrevendo no arquivo texto.txt')

with open('frutas.txt', 'w') as arquivo:

    while True:
        fruta = input('Digite o nome da fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
