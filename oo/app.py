'''
POO -> Paradigma de programação que utiliza mapeamento de objetos do mundo para modelos computacionais

Pricipais elementos do POO:
  -> Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
  -> Atributo -> Características do objeto
  -> Método -> Comportamento do objeto (funções)
  -> Construtor -> Método especial utilizado para criar os objetos
  -> Objeto -> Instância da classe

OBS:
  -> Quando uma classe ainda não está implementada é utilizado o "pass"

Decorator @property -> Permite acessar o retorno de um método como se fosse um atributo, ou seja, sem precisar usar ().
          _calculate_discount -> O prefixo _ no inicio da função indica que é um método "privado"


A função json.dump() é usada para serializar (converter) um objeto Python em formato JSON e gravar no arquivo especificado.


MÉTODOS

- Métodos (Funções) -> Representam os comportamentos do objeto. Ou Seja, as ações e Métodos de Classe
- Métodos de Instância e Métodos de Classe:
    -> Métodos de Instância -> (self) -> Quando você precisa acessar ou modificar os atributos do objeto (instância).
    -> Métodos de Classe (@classmethod) ->  Recebem automaticamente a classe (cls) como primeiro parâmetro, não a instância. Usamos o decorador @classmethod para indicá-los.
        Exemplo:
            class Produto:
                def __init__(self, nome, preco):
                    self.nome = nome
                    self.preco = preco

                @classmethod
                def criar_com_desconto(cls, nome, preco, desconto):
                    preco_com_desconto = preco - (preco * desconto / 100)
                    return cls(nome, preco_com_desconto)

            # Cria o produto usando o método de classe
            p2 = Produto.criar_com_desconto("Teclado", 100, 10)
            print(p2.nome, p2.preco)  # Teclado 90.0
'''
import os
from decimal import Decimal
import json


class Product:
    # Constructor
    def __init__(self, name, price, discount, qtd):
        self.name = name
        self.price = Decimal(str(price))
        self.discount = Decimal(str(discount))
        self.qtd = int(qtd)

    # Método privado para calcular o desconto
    def _calculate_discount(self):
        return round(self.price * (self.discount / 100), 2)

    # Decorador para utilizar o método como se fosse um atributo. Utilizado assim p1.productName
    @property
    def productName(self):
        return f'Nome do produto {self.name}'

    @property
    def productPrice(self):
        return f'Valor do Produto R$ {self.price}'

    @property
    def productDiscount(self):
        return f"Desconto do Produto escolhido: {self.discount}%"

    @property
    def calcDiscount(self):
        valueDiscount = self._calculate_discount()
        return f'Valor total do produto com desconto aplicado: R$ {self.price - valueDiscount}'

    @property
    def qtdProduct(self):
        valueDiscount = self._calculate_discount()
        priceTotal = self.price - valueDiscount
        return f'Preço total da compra: R$ {priceTotal * self.qtd}'

    @property
    def save_to_dict(self):
        return {
            "name": self.name,
            "price": float(self.price),
            "discount": float(self.discount),
            "amount": self.qtd
        }


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_product_in_json(product, file="oo/products.json"):
    products = []

    # Verificação se o file existe e se tem conteúdo
    if os.path.exists(file):
        with open(file, 'r', encoding="utf-8") as f:
            try:
                # Tenta carregar os dados do aquivo
                products = json.load(f)
            except json.JSONDecodeError:  # Caso não seja um json válido
                products = []

    products.append(product.save_to_dict)

    with open(file, 'w', encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)


product_name = input('Digite o nome do produto: ')
product_price = input('Digite o preço do produto (ex: 25.00): R$ ')
product_discount = input('Digite o desconto do produto (ex:10): ')
product_qtd = input('Digite a quantidade do produto: ')
clear()


try:
    product = Product(product_name, product_price,
                      product_discount, product_qtd)
    print(product.productName)
    print(product.productPrice)
    print(product.productDiscount)
    print(product.calcDiscount)
    print(product.qtdProduct)

    save_product_in_json(product)
    print('Produto salvo com sucesso!')
except Exception as e:
    print(f'Erro ao criar Produto {e}')
