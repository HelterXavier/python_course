'''
Sistema de arquivos e Navegação
'''

import os  # Importa o módulo os para manipulação de arquivos e diretórios

# print(os.getcwd())  # Imprime o diretório de trabalho atual
# os.chdir('..')  # Altera o diretório de trabalho para o diretório pai
# print(os.getcwd())  # Imprime o novo diretório de trabalho


# print(os.path.isabs('..'))  # Verifica se o caminho é absoluto (False)
# # Verifica se o caminho é absoluto (True)
# print(os.path.isabs('C:\\Users\TESTE'))


arquivos = list(os.scandir())

# Lista os arquivos e diretórios no diretório atual)
print('Arquivos e diretórios no diretório atual:', arquivos)
