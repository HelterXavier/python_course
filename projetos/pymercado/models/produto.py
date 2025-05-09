from utils.helper import formata_float_str_moeda


class Produto:

    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f'Código : {self.__codigo} \nNome: {self.__nome} \nPreço: {formata_float_str_moeda(self.__preco)}'
