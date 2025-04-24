'''
POO -> Abstração e Encapsulamento

O objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes

Escapsular -> Cápsula

                                  Classe
--------------------------------------------------------------------------------
|                                                                              |
|                           Atributos e Métodos                                |
|                                                                              |

# Atributos/Métodos privados em Python

Imagine que temos uma classes chamada Pessoa, contendo um atributo privado chamado __nome
e um método privado chamado __falar()

Esses elementos privados só deve ser acessados dentro da class. Mas o Python não bloqueia esse acesso a classe.
Com o Python existe o Name Mangling, que faz uma alteração  na forma de se acessar os elementos privados, conforme:

_ClassName_elemento

instancia.Pessoa__nome


# Abstração é o ato de expor apenas dados relevantes de uma classe, econdendo atributos e métodos privados de usuário
'''


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


conta1 = Conta('Helter', 150.00, 1500)

conta1.depositar(150)
print(conta1.__dict__)
