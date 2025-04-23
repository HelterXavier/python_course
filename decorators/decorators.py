'''
Decoradoes (Decorators)

-> Decoradores são funções
-> Decoradores envolvem outras funções e aprimoram seu comportamento
-> Decoradores também são exemplos de Highr Order Functions (Funções de Ordem Superior)
-> Decoradores tem uma sintaxe especial com o símbolo @ (Syntact Sugar / Açucar Sintático)
'''

# Exemplo 1 - Decorador simples


# def meu_decorador(funcao):
#     def funcao_interna():
#         print('Antes da execução da função')
#         funcao()
#         print('Depois da execução da função')
#     return funcao_interna


# @meu_decorador
# def minha_funcao():
#     print('Executando a função principal')


# # Chama a função decorada
# minha_funcao()

# Saída:
# Antes da execução da função
# Executando a função principal
# Depois da execução da função
# --------------------------------------------------------------------
# Exemplo 2 - Decorador com parâmetros
def meu_decorador(funcao):
    def funcao_interna(*args, **kwargs):
        print('Antes da execução da função')
        resultado = funcao(*args, **kwargs)
        print('Depois da execução da função')
        return resultado
    return funcao_interna


@meu_decorador
def soma(a, b):
    return a + b


# Chama a função decorada
resultado = soma(5, 3)
print(f'Resultado da soma: {resultado}')
