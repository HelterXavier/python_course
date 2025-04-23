'''
Criando sua propria versão de loop
'''


def meu_for(iteravel):
    it = iter(iteravel)  # cria um iterador
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


# Testando a função
meu_for([1, 2, 3, 4, 5])
meu_for('Lucas')
