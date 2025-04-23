'''
Preservando Metadata com Wraps

O que é Metadata ?
  - Informações adicionais sobre um objeto, como nome, tipo, descrição, etc.
  - Pode ser usada para documentação, validação, serialização, etc.
  - Pode ser armazenada em dicionários, listas ou outros tipos de dados.
  - Pode ser acessada através de funções ou métodos específicos, como `__dict__`, `__annotations__`, etc.

O que são wraps ?
  - Função decoradora que preserva a metadata de uma função original.
  - É usada para criar funções decoradoras que não alteram a metadata da função original.
  - É uma função do módulo `functools` que copia a metadata da função original para a função decorada.
  - É usada para garantir que a função decorada tenha o mesmo nome, docstring e outras informações da função original.
  - É usada para evitar problemas de documentação e depuração.
'''

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Preserva a metadata da função original
    def logar(*args, **kwargs):
        print(f'Você está chmando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    '''Soma dois números'''
    return a + b


print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números
