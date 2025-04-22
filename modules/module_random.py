'''
Módulo Random e o que são módulos?
Um módulo é um arquivo que contém definições e implementações de funções, classes e variáveis que podem ser reutilizadas em outros programas. Os módulos ajudam a organizar o código e a evitar duplicação. O Python possui uma biblioteca padrão rica em módulos, como o módulo `random`, que fornece funções para gerar números aleatórios.
O módulo `random` é um módulo embutido do Python que fornece funções para gerar números aleatórios. Ele é amplamente utilizado em jogos, simulações e outras aplicações que requerem aleatoriedade. Algumas das funções mais comuns do módulo `random` incluem:
'''

import random

# Função para gerar um número inteiro aleatório entre dois valores


def gerar_numero_inteiro_aleatorio(inicio, fim):
    """
    Gera um número inteiro aleatório entre 'inicio' e 'fim' (inclusive).
    """
    return random.randint(inicio, fim)


print(gerar_numero_inteiro_aleatorio(1, 1000))  # Exemplo de uso da função0,
