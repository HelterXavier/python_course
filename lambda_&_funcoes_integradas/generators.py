'''
GENERATORS -> São funções que geram valores sob demanda, ou seja, não armazenam todos os valores na memória.
           -> Os geradores são iteráveis, mas não são listas. Eles são criados usando a palavra-chave yield em vez de return.
           -> Um generator é uma função especial que "gera" valores sob demanda, um por vez, sem armazenar tudo na memória de uma vez.
           -> Funções normais usam return e encerram após retornar o valor. Generators usam yield e "pausam" a execução, retomando do ponto onde parara
'''


# def contador():
#     yield 1
#     yield 2
#     yield 3


# gen = contador()
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # StopIteration: O gerador não tem mais valores para gerar


# Lista (ocupa memória toda de uma vez)
valores = [x * 2 for x in range(1000000)]

# Generator (gera sob demanda)
valores = (x * 2 for x in range(1000000))
