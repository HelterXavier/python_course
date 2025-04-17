'''
Lambda

- Funções anonimas que podem ser executadas em resposta a eventos, como alterações em dados em um bucket do S3 ou atualizações em uma tabela do DynamoDB.
- São executadas em um ambiente gerenciado, o que significa que não é necessário se preocupar com a infraestrutura subjacente.
'''

lambda x: 3 * x + 1
# A função acima é uma função lambda que recebe um argumento x e retorna o resultado da expressão 3 * x + 1.


# soma = lambda x, y: x + y
def soma(x, y): return x + y
