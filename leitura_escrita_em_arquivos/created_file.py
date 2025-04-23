'''
Sistema de arquivos - Manipulação
'''

import os
# Função sem paramentro para usuario criar nome e extensão do arquivo
typeFile = input(
    'Digite o tipo do arquivo: \n- txt = Texto \n- csv = CSV \n- json = JSON \nDigite: ')

# Se for diferente de txt, csv ou json, o programa não irá criar o arquivo
if typeFile not in ['txt', 'csv', 'json']:
    print('Tipo de arquivo inválido!')
    exit()
else:
    fileName = input('Agora digite o nome do arquivo: ')


if fileName == '':
    fileName = 'Novo Arquivo.txt'
else:
    fileName = fileName + '.' + typeFile


def criar_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        print('Arquivo já existe!')
        write_in_the_file = input('Escreva o conteúdo nele: ')
        if write_in_the_file == '':
            print('Nada foi escrito no arquivo!')
            exit()
        else:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(write_in_the_file + '\n')
                print('Texto escrito no arquivo!')
    else:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('')
            print('Arquivo criado com sucesso!')

            write_s_n = input('Deseja escrever algo no arquivo? (s/n): ')
            if write_s_n == 's':
                write_in_the_file = input('Escreva o conteúdo nele: ')
                if write_in_the_file == '':
                    print('Nada foi escrito no arquivo!')
                    exit()
                else:
                    with open(nome_arquivo, 'w') as arquivo:
                        arquivo.write(write_in_the_file + '\n')
                        print('Texto escrito no arquivo!')
            else:
                print('Nada foi escrito no arquivo!')


criar_arquivo(fileName)
