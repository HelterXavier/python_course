'''
Definição de funções

- Trexos de codigo que realizam uma tarefa específica
- Podem receber parâmetros e retornar valores
- Podem ser reutilizadas em diferentes partes do código
- Podem ser definidas em módulos e importadas em outros arquivos
- Podem ser aninhadas (funções dentro de funções)
- Podem ser decoradas (funções que modificam o comportamento de outras funções)
- Podem ser geradoras (funções que retornam um iterador)
- Podem ser assíncronas (funções que permitem execução concorrente)
- Podem ser lambda (funções anônimas de uma linha)
- Podem ser de classe (funções que pertencem a uma classe)
- Podem ser estáticas (funções que não dependem de instância de classe)
- Podem ser de classe (funções que pertencem a uma classe)

- *ARGS: permite passar um número variável de argumentos posicionais para uma função
- **KWARGS ou **xis: permite passar um número variável de argumentos nomeados para uma função
'''


def calcImc(weith: float, height: float) -> float:
    calc = weith / (height ** 2)
    return round(calc, 2)


def soma_valores(*args):
    soma = 0
    for valor in args:
        soma += valor
    return f'A soma dos valores é: {soma}'


def cores(**kwargs):
    for cor, valor in kwargs.items():
        print(f'A cor {cor} tem o valor {valor}')


calcImc(70.0, 1.70)
soma_valores(20, 40, 60, 80, 100)
cores(azul='blue', verde='green', vermelho='red', amarelo='yellow')
