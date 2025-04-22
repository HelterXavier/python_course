'''
Lambda

- Funções anonimas que podem ser executadas em resposta a eventos, como alterações em dados em um bucket do S3 ou atualizações em uma tabela do DynamoDB.
- São executadas em um ambiente gerenciado, o que significa que não é necessário se preocupar com a infraestrutura subjacente.
'''

# lambda x: 3 * x + 1
# A função acima é uma função lambda que recebe um argumento x e retorna o resultado da expressão 3 * x + 1.


# soma = lambda x, y: x + y
# def soma(x, y): return x + y

# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


# def nome_completo(nome, sobrenome): return nome.strip(
# ).title() + ' ' + sobrenome.strip().title()


# print(nome_completo('  joão  ', '  da silva  '))

# def soma(x, n): return x + n


# print(soma(5, 30))
# print((lambda x=1, n=8: x + n)())


def gerador_funcao_quadrativa(a, b, c):
  # Retorna função quadratica f(x) = a*x^2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c


print(gerador_funcao_quadrativa(1, 2, 3)(5))
