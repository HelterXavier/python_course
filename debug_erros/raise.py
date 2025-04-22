'''
Raise -> Raise é um comando que gera uma exceção, ou seja, um erro.
# O comando raise é utilizado para gerar uma exceção de forma intencional, ou seja, quando o programador deseja interromper a execução do programa e sinalizar que ocorreu um erro.
# O comando raise pode ser utilizado em conjunto com o comando try/except para tratar exceções de forma personalizada.
# O comando raise pode ser utilizado para gerar exceções personalizadas, ou seja, o programador pode criar suas próprias exceções e utilizá-las em seu código.
'''

# Exemplo 1: Utilizando o comando raise para gerar uma exceção


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto deve ser uma string')
    if type(cor) is not str:
        raise TypeError('A cor deve ser uma string')
    else:
        print(f'O texto {texto} será exibido na cor {cor}')


colore('Geek', 'azul')
colore('Geek', 123)
