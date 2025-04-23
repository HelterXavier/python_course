'''
StringIO é uma classe que permite trabalhar com strings como se fossem arquivos.

Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
  - Permissão de leitura: permite ler o arquivo.
  - Permissão de escrita: permite escrever no arquivo.
  - Permissão de execução: permite executar o arquivo.

StringIO -> Usado para ler e criar arquivos em memória.
'''

from io import StringIO

mensagem = 'String normal'

# Criando um arquivo em memória
arq = StringIO(mensagem)

# Lendo o arquivo em memória
print(arq.read())

# Escrevendo no arquivo em memória
arq.write(' - String escrita no arquivo em memória')

arq.seek(0)  # Move o cursor para o início do arquivo
print(arq.read())
