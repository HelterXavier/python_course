'''
Try/Except -> É uma estrutura de controle de fluxo que permite lidar com exceções (erros) em Python.
# # O comando try/except é utilizado para tratar exceções de forma personalizada, ou seja, o programador pode criar suas próprias exceções e utilizá-las em seu código.
# # O comando try/except é utilizado para evitar que o programa seja interrompido por um erro, permitindo que o programador trate o erro de forma personalizada.
'''

# Exemplo 1: Utilizando o comando try/except para tratar exceções
try:
    numero = int(input('Digite um número: '))
    print(f'O número digitado foi {numero}')
except ValueError:
    print('Valor inválido! Por favor, digite um número inteiro.')
