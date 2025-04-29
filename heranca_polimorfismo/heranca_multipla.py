'''
POO -> Herança Multipla:

É a possibilidade de uma classe herdar de mútiplas clasess, fazendo com que a classe filha
herde de múltiplas classes, fazendo com que a classes filha herde de todas as classes herdads.


#OBS: A herança múltipla pode ser feita de duas maneiras
    - Por multiderivação direta
    - Por multiderivação Indireta
'''

# Exemplo 1 = Multiderivação Direta


# class Base1:
#     pass


# class Base2:
#     pass


# class Base3:
#     pass


# class MultiDerivada(Base1, Base2, Base3):
#     pass


# Exemplo 2 -> Multiderivação indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass
