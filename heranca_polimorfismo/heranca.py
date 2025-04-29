'''
POO HERANÇA & POLIMORFISMO

HERANÇA (INHERITANCE):
  -> Reaproveitação de classes.
  -> Extensão das classes
  -> Com a herança, a partir de uma classes existente, nós extendemos outra classes
que passa a g=herdar atributos e métodos da classe herdada
  EX ->
  Client
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

  Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;


  OBS -> QUANDO UMA CLASSE HERDA DE OUTRA CLASSE, A CLASSE HERDADA É CONHECIDA POR:
      -> SUPER CLASSE
      -> CLASSE MÃE
      -> CLASSE PAI
      -> CLASSE BASE

  OBS -> QUANDO UMA CLASSE HERDA DE OUTRA CLASSE, ELA É CHAMADA:
      [Cliente, Funcionário]
      -> SUB CLASSE
      -> CLASSE FILHAS
      -> CLASSE ESPECÍFICA

  EXEMPLO SEM HERANÇA:

  class Cliente:

  def __init__(self, nome, sobrenome, cpf, renda):
    self.__nome = nome
    self.__sobrenome = sobrenome
    self.__cpf = cpf
    self.__renda = renda

  def nome_completo(self):
    return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

  def __init__(self, nome, sobrenome, cpf, renda):
    self.__nome = nome
    self.__sobrenome = sobrenome
    self.__cpf = cpf
    self.__matricula = matricula

  def nome_completo(self):
    return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Helter', 'Xavier', '123.456.789-12', 3000)
funcionario1 = Cliente('Thiago', 'Henrique', '987.654.321.52', 1650)

print(cliente1.nome_completo)
print(funcionario1.nome_completo)



'''

# SUPER CLASSE


class Pessoa:
    # CONSTRUTOR
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        # ACESSO AO CONSTRUTOR
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        # ACESSO AO CONSTRUTOR
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula}'


cliente1 = Cliente('Helter', 'Xavier', '123.456.789-12', 3000)
funcionario1 = Funcionario('Thiago', 'Henrique', '987.654.321.52', 1650)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
