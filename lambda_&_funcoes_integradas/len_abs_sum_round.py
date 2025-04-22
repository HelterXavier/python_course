'''
Len -> Retorna o tamanho de um objeto.
Abs -> Retorna o valor absoluto de um número.
Sum -> Retorna a soma de um iterável.
Round -> Retorna um número arredondado para o inteiro mais próximo ou para um número específico de casas decimais.
# Exemplo de uso das funções len, abs, sum e round
# Definindo uma lista de números
'''


numeros = [1, -2, 3.5, -4.7, 5]
# Calculando o tamanho da lista
tamanho_lista = len(numeros)
# Calculando o valor absoluto de um número
valor_absoluto = abs(-10)
# Calculando a soma dos números da lista
soma_lista = sum(numeros)
# Arredondando um número
numero = 3.14159
numero_arredondado = round(numero, 2)  # Arredonda para 2 casas decimais
# Exibindo os resultados
print(f'Tamanho da lista: {tamanho_lista}')
print(f'Valor absoluto de -10: {valor_absoluto}')
print(f'Soma da lista: {soma_lista}')
print(f'Número arredondado: {numero_arredondado}')
