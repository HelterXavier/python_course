'''
Funcções de Maior grande - Highr Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras
funções como resultado ou meso que podemos passar funções como argumento para outras funções,
e até mesmo criar variáveis do tipo de funções nos nossos programas

'''

# Função que retorna uma função


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


double = make_multiplier_of(2)
triple = make_multiplier_of(3)

print(double(5))  # 10
print(triple(5))  # 15
