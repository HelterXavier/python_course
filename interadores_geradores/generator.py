'''
Geradores

- Geradores (Generators) são funções que permitem criar iteradores de forma mais simples e eficiente.
- Eles utilizam a palavra-chave yield para retornar valores, permitindo que a função pause sua execução e retome posteriormente.
- Isso é útil para economizar memória, pois os valores são gerados sob demanda, em vez de serem armazenados todos de uma vez.
- Os geradores são uma forma de criar iteradores personalizados, permitindo que você defina a lógica de iteração de maneira mais flexível e legível.
- Eles são frequentemente usados em situações onde a quantidade de dados é grande ou desconhecida, como leitura de arquivos grandes, processamento de streams de dados, etc.
'''


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(50)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
