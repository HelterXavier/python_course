
# 🐍 Python — Anotações

## 🎲 Tipos de Dados
```python
idade = 20 # INT
salario = 1000.50 # FLOAT
nome = 'João' # STRING
casado = False # BOOL
Genero = 'M' # CHAR

print(f'- Nome: {nome} \n- Idade: {idade} \n- Salário: {salario} \n- Casado: {casado} \n- Gênero: {Genero}')
```
## 🔢 Operadores Aritméticos

```python
# Soma
soma = 10 + 10
print(f'Soma: {soma}')

# Subtração
subtracao = 10 - 5
print(f'Subtração: {subtracao}')

# Multiplicação
multiplicacao = 10 * 5
print(f'Multiplicação: {multiplicacao}')

# Divisão
divisao = 10 / 2
print(f'Divisão: {divisao}')

# Divisão inteira
divisao_inteira = 10 // 3
print(f'Divisão inteira: {divisao_inteira}')

# Resto da divisão
resto = 10 % 3
print(f'Resto: {resto}')

# Potência
potencia = 2 ** 3
print(f'Potência: {potencia}')
```

---

## 🧮 Operadores de Comparação

```python
# Igual
igual = 10 == 10
print(f'Igual: {igual}')

# Diferente
diferente = 10 != 10
print(f'Diferente: {diferente}')

# Maior
maior = 10 > 10
print(f'Maior: {maior}')

# Menor
menor = 10 < 10
print(f'Menor: {menor}')

# Maior ou igual
maior_igual = 10 >= 10
print(f'Maior ou igual: {maior_igual}')

# Menor ou igual
menor_igual = 10 <= 10
print(f'Menor ou igual: {menor_igual}')
```

---

## 🧠 Operadores Lógicos

```python
# E (and)
e = True and True
print(f'E: {e}')

# OU (or)
ou = True or False
print(f'OU: {ou}')

# Negação (not)
negacao = not True
print(f'Negação: {negacao}')
```

---

## 📝 Operadores de Atribuição

```python
# Atribuição
a = 10
print(f'Atribuição: {a}')

# Adição
a += 10
print(f'Adição: {a}')

# Subtração
a -= 5
print(f'Subtração: {a}')

# Multiplicação
a *= 5
print(f'Multiplicação: {a}')

# Divisão
a /= 2
print(f'Divisão: {a}')

# Divisão inteira
a //= 3
print(f'Divisão inteira: {a}')

# Resto
a %= 3
print(f'Resto: {a}')

# Potência
a **= 3
print(f'Potência: {a}')
```

---

## 🆔 Operadores de Identidade

```python
b = 10
c = 10

# is
identidade = b is c
print(f'Identidade: {identidade}')

# is not
identidade_negacao = b is not c
print(f'Identidade negação: {identidade_negacao}')
```

---

## 📦 Operadores de Associação

```python
lista = [1, 2, 3, 4, 5]

# in
print(3 in lista)      # True
print(6 in lista)      # False

# not in
print(3 not in lista)  # False
```

---

## 🧵 Strings

```python
nome1 = 'Helter Xavier'           # Aspas simples
nome2 = "Helter Xavier"           # Aspas duplas
nome3 = '''Helter Xavier'''       # Aspas triplas simples (string multilinha)
nome3 = """Helter Xavier"""       # Aspas triplas (string multilinha)

nomeBar = "Gina's bar"

print(nome.upper())  # Transforma em letra maiúscula
print(nome.lower())  # Transforma em letra minúscula
print(nome.split())  # Transforma em uma lista de strings


```

---

## 📐 PEP8 - Boas Práticas

- Classes devem usar **CamelCase**:
  Ex: `CalculadoraCientifica`
- Funções e variáveis devem usar **snake_case**:
  Ex: `soma_dois`
- Indentação de **4 espaços** por nível:
```python
if 'a' in 'banana':
    print('tem')
```

---

## 👤 Receber dados do usuário

```python
print("Qual seu nome ?")
nome = input()

print('Seja bem-vindo(a) %s' % nome)
```


## 🦾 Estruturas condicionais

### IF | ELSE | ELIF

```python

idade = 6

if idade < 18:
  print('Menor de idade')
elif idade == 18:
  print('Tem 18 anos')
else:
  print('Maior de idade')
````

## 🔁 Estruturas de repetição

Python oferece duas estruturas de repetição: `for` e `while`.

---

### 🔂 `for` - Laço de Repetição com Iteração

utilizado para iterar sobre uma sequência (como listas, strings, tuplas, etc).

#### Exemplo: Percorrendo uma lista

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

#### Exemplo: Utilizando `range`

```python
# Imprime de 0 a 4
for i in range(5):
    print(i)
```

---

#### Exemplo: Utilizando `while`

 `while` executa o bloco de código **enquanto** a condição for verdadeira.

#### Exemplo: Contando até 5

```python
contador = 0
while contador <= 5:
    print(contador)
    contador += 1
```

⚠️ **Cuidado com loops infinitos!** Certifique-se de que a condição em algum momento será falsa.

---

### ⏹️ `break` - Interrompe o loop

O `break` é utilizado para sair de um laço antes que ele termine naturalmente.

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

---

### 🔃 `continue` - Pula para a próxima iteração

O `continue` pula o restante do código no loop e vai direto para a próxima iteração.

```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```

---

### 🔄 `else` com `for` ou `while`

O `else` é executado quando o loop termina **sem ser interrompido por um `break`**.

```python
for i in range(3):
    print(i)
else:
    print("Loop finalizado normalmente.")
```

---

## 🧪 Exemplo prático: Verificar se número é primo

```python
numero = 7

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} não é primo")
        break
else:
    print(f"{numero} é primo")
```

---



# 📚 Listas (`list`) em Python

Listas são coleções ordenadas e mutáveis usadas para armazenar itens em uma única variável.

---

## 🧱 Criando uma Lista

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas)
```

---

## 📌 Acessando Elementos

```python
print(frutas[0])  # Primeiro item
print(frutas[-1]) # Último item
```

---

## 🔄 Iterando sobre uma Lista

```python
for fruta in frutas:
    print(fruta)
```

---

## ✏️ Modificando Elementos

```python
frutas[1] = "uva"
print(frutas)
```

---

## ➕ Adicionando Elementos

```python
# Adiciona ao final
frutas.append("abacaxi")

# Insere em posição específica
frutas.insert(1, "morango")
```

---

## ❌ Removendo Elementos

```python
# Remove por valor
frutas.remove("maçã")

# Remove o último item
frutas.pop()

# Remove item por índice
del frutas[0]

# Remove todos os itens
frutas.clear()
```

---

## 🔍 Verificando Existência de Item

```python
if "banana" in frutas:
    print("Tem banana!")
```

---

## 📏 Tamanho da Lista

```python
print(len(frutas))
```

---

## 🔁 Juntando Listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

junta = lista1 + lista2
```

---

## 🔄 Compreensão de Lista (List Comprehension)

```python
quadrados = [x**2 for x in range(6)]
print(quadrados)
```

---

## 🧪 Métodos Úteis

```python
numeros = [5, 3, 8, 1, 9]

numeros.sort()       # Ordena crescente
numeros.reverse()    # Inverte ordem
print(numeros.index(8))  # Índice do elemento
print(numeros.count(3))  # Quantidade de vezes que o elemento aparece
```

---

## 📋 Cópia de Lista

```python
lista_original = [1, 2, 3]
copia = lista_original.copy()
```

---

---

## 📦 Desempacotamento de listas

```python
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
```

---


# 🔐 Tuplas (`tuple`) em Python

- São representadas por parênteses ()
- São imutáveis (não podem ser alteradas após a criação)

---

## 🧱 Criando uma Tupla

```python
frutas = ("maçã", "banana", "laranja")
print(frutas)
```

### Tupla com um único item

```python
# Note a vírgula no final
sozinha = ("maçã",)
```

---

## 📌 Acessando Elementos

```python
print(frutas[0])   # Primeiro item
print(frutas[-1])  # Último item
```

---

## 🔄 Iterando sobre uma Tupla

```python
for fruta in frutas:
    print(fruta)
```

---

## 📏 Tamanho da Tupla

```python
print(len(frutas))
```

---

## ❌ Tuplas são Imutáveis

```python
# Isso causará erro!
frutas[0] = "uva"
```

Se você precisa modificar uma tupla, deve convertê-la para lista, modificar, e reconverter:

```python
lista_frutas = list(frutas)
lista_frutas[0] = "uva"
frutas = tuple(lista_frutas)
```

---

## 🔍 Verificando Existência de Item

```python
if "banana" in frutas:
    print("Tem banana!")
```

---

## 📋 Métodos de Tupla

```python
print(frutas.count("maçã"))   # Conta quantas vezes aparece
print(frutas.index("banana")) # Retorna o índice da primeira ocorrência
```

---

## 🧪 Desempacotamento de Tuplas

```python
pessoa = ("João", 30, "Desenvolvedor")
nome, idade, profissao = pessoa

print(nome)
print(idade)
print(profissao)
```

---

## 🔁 Juntando Tuplas

```python
tupla1 = (1, 2)
tupla2 = (3, 4)

tupla3 = tupla1 + tupla2
```

---



# 📖 Dicionários (`dict`) em Python

- Dicionários são coleções de pares **chave:valor**
- Dicionários são mutáveis
- Dicionários são indexados por chaves, não por números
- Dicionários são representados por chaves {}

---

## 🧱 Criando um Dicionário

```python
pessoa = {
    "nome": "João",
    "idade": 30,
    "profissao": "Desenvolvedor"
}
print(pessoa)
```

---

## 📌 Acessando Valores

```python
print(pessoa["nome"])
print(pessoa.get("idade"))  # Forma segura (não lança erro se a chave não existir)
```

---

## ✏️ Modificando Valores

```python
pessoa["idade"] = 31
```

---

## ➕ Adicionando Novos Pares

```python
pessoa["cidade"] = "São Paulo"
```

---

## ❌ Removendo Itens

```python
pessoa.pop("profissao")     # Remove a chave e retorna o valor
del pessoa["idade"]         # Remove a chave diretamente
pessoa.clear()              # Limpa todo o dicionário
```

---

## 🔁 Iterando em Dicionários

```python
# Pelas chaves
for chave in pessoa:
    print(chave, pessoa[chave])

# Pelos valores
for valor in pessoa.values():
    print(valor)

# Pelos itens (chave e valor)
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

---

## 🔍 Verificando Existência de Chave

```python
if "nome" in pessoa:
    print("Chave 'nome' existe")
```

---

## 🧪 Métodos Úteis

```python
keys = pessoa.keys()        # Retorna todas as chaves
values = pessoa.values()    # Retorna todos os valores
items = pessoa.items()      # Retorna todos os pares (chave, valor)
```

---

## 🧬 Cópia de Dicionário

```python
copia = pessoa.copy()
```

---

## 🧱 Dicionário Aninhado

```python
usuarios = {
    "usuario1": {"nome": "Ana", "idade": 25},
    "usuario2": {"nome": "Carlos", "idade": 40}
}
print(usuarios["usuario1"]["nome"])
```

---

> 💡 *Dicionários são ideais para armazenar dados estruturados, como registros, perfis, e configurações. São largamente utilizados em APIs, banco de dados e manipulação de JSON.*


# 🧮 Conjuntos (`set`) em Python

Conjuntos são coleções **não ordenadas** de **elementos únicos**. Muito úteis em operações matemáticas como **união**, **interseção**, **diferença** e **diferença simétrica**.

---

## 📌 Características dos Conjuntos

- Elementos **únicos** (sem duplicatas)
- **Não ordenados** (sem índice)
- **Mutáveis** (você pode adicionar e remover elementos)
- Elementos **imutáveis** (listas, dicionários e outros sets não podem ser membros de um set)
- Usados para testes de **pertinência** e para **remoção de duplicatas**

---

## 🧱 Criando Conjuntos

```python
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = set({1, 2, 3, 4, 5})
conjunto3 = set([1, 2, 3, 4, 5])
conjunto4 = set("12345")

print(conjunto4)  # {'1', '2', '3', '4', '5'}
```


# 📚 Direnças de Coleções em Python: Listas, Tuplas, Dicionários, Conjuntos e Mapas

As principais diferenças entre os tipos de coleções em Python, quando usar cada uma e exemplos práticos de uso.

---

## 📦 1. Listas (`list`)

Listas são coleções **ordenadas** e **mutáveis** que permitem elementos duplicados.

### ✅ Quando usar:
- Precisa de ordenação
- Precisa adicionar/remover elementos
- Permite valores repetidos

### 🔧 Exemplo:

```python
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")
print(frutas[0])  # 'maçã'
```


## 🔐 2. Tuplas (tuple)
Tuplas são coleções ordenadas e imutáveis, ideais para dados fixos.

✅ Quando usar:
- Dados constantes, como coordenadas ou configurações
- Deseja proteger os dados de alterações

```python

coordenadas = (10.0, 20.5)
print(coordenadas[1])  # 20.5
# coordenadas[0] = 15.0  -> ❌ erro
```

## 📚 3. Dicionários (dict)
Dicionários armazenam pares chave:valor. As chaves são únicas e os valores acessados via chave.

✅ Quando usar:
- Precisa associar identificadores a valores
- Precisa acessar dados por nome
-
```python
pessoa = {"nome": "João", "idade": 30}
print(pessoa["nome"])  # 'João'
pessoa["idade"] += 1
```

## 🧮 4. Conjuntos (set)
Conjuntos são coleções não ordenadas de elementos únicos. Muito usados para garantir unicidade e fazer operações matemáticas.

✅ Quando usar:
- Remover duplicatas
- Verificar se um elemento existe
- Fazer operações como união e interseção

```python
numeros = {1, 2, 3, 2, 1}
print(numeros)  # {1, 2, 3}
numeros.add(4)


# Operações úties

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # União: {1, 2, 3, 4, 5}
print(a & b)  # Interseção: {3}
print(a - b)  # Diferença: {1, 2}
print(a ^ b)  # Diferença simétrica: {1, 2, 4, 5}
```


## 🗺️ 5. Mapas (map())
Em Python, map() é uma função que aplica outra função a cada item de uma coleção. Não é uma estrutura como em outras linguagens.

✅ Quando usar:
- Precisa transformar elementos de forma preguiçosa (lazy)
- Quer evitar loops explícitos

### 🔧 Exemplo:
```python
numeros = [1, 2, 3]
dobros = list(map(lambda x: x * 2, numeros))
print(dobros)  # [2, 4, 6]
```

## 📋 Tabela Resumo

| Tipo   | Ordenado  | Mutável | Duplicatas     | Acesso por     | Uso típico                          |
|--------|-----------|---------|----------------|----------------|-------------------------------------|
| list   | ✅         | ✅       | ✅              | Índice         | Listas genéricas                    |
| tuple  | ✅         | ❌       | ✅              | Índice         | Dados fixos                         |
| dict   | ✅ (3.7+)  | ✅       | ❌ (chaves)     | Chave          | Mapeamento chave/valor              |
| set    | ❌         | ✅       | ❌              | Não suportado  | Remoção de duplicatas, conjuntos    |
| map()  | -         | -       | -              | Iteração       | Transformações funcionais           |



---


# 📦 Módulo `collections` em Python

O módulo `collections` fornece tipos de dados especializados que estendem as funcionalidades das estruturas padrão do Python. Abaixo estão os principais:

---

## 1. `Counter`

- `Counter` é uma subclasse de `dict` que conta a frequência de elementos em uma coleção (geralmente listas ou strings).
- O `Counter` mostra o número de ocorrencias de cada elemento em uma lista

### ✅ Exemplo:

```python
from collections import Counter

frutas = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
contagem = Counter(frutas)

print(contagem)
# Saída: Counter({'maçã': 3, 'banana': 2, 'laranja': 1})
```

---

## 2. `defaultdict`

`defaultdict` é como um dicionário normal, mas permite definir um valor padrão para chaves inexistentes, evitando erros de `KeyError`.

### ✅ Exemplo:

```python
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
d['b'] += 2

print(d)
# Saída: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
```

---

## 3. `OrderedDict`

Antes do Python 3.7, os dicionários não mantinham a ordem de inserção. `OrderedDict` resolve isso.

> ⚠️ A partir do Python 3.7+, `dict` já preserva a ordem de inserção, tornando `OrderedDict` menos necessário.

### ✅ Exemplo:

```python
from collections import OrderedDict

dados = OrderedDict()
dados['nome'] = 'Maria'
dados['idade'] = 25
dados['cidade'] = 'São Paulo'

print(dados)
```

---

## 4. `namedtuple`

Cria tuplas com campos nomeados, facilitando o acesso e deixando o código mais legível.

### ✅ Exemplo:

```python
from collections import namedtuple

Pessoa = namedtuple('Pessoa', 'nome idade')
p1 = Pessoa(nome='João', idade=30)

print(p1.nome)  # João
print(p1.idade)  # 30
```

---

## 5. `deque`

É uma fila dupla (double-ended queue), ideal para operações rápidas de inserção e remoção em ambas as extremidades.

### ✅ Exemplo:

```python
from collections import deque

fila = deque()
fila.append('a')      # adiciona ao final
fila.appendleft('b')  # adiciona ao início
print(fila)

fila.pop()            # remove do final
fila.popleft()        # remove do início
```

---

## 📋 Resumo Rápido

| Tipo           | O que faz                                     | Quando usar                         |
|----------------|-----------------------------------------------|-------------------------------------|
| `Counter`      | Conta elementos repetidos                     | Frequência em listas ou strings     |
| `defaultdict`  | Dicionário com valor padrão automático        | Evitar KeyError                     |
| `OrderedDict`  | Dicionário que mantém ordem de inserção       | Compatibilidade com versões < 3.7   |
| `namedtuple`   | Tupla com nomes de campos                     | Substituir classes simples          |
| `deque`        | Fila dupla com alta performance               | Filas e pilhas                      |

---

> 💡 Esses tipos estão no módulo `collections`, então lembre-se de importar com: `from collections import ...`



---




# 🐍 Funções em Python — `def`, `*args`, `**kwargs` e Parâmetros

Funções são blocos reutilizáveis de código que executam uma tarefa específica. Em Python, usamos a palavra-chave `def` para definir funções.

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

---

## ✅ Criando uma função simples

```python
def saudacao():
    print("Olá, seja bem-vindo!")
```

Para chamar a função:

```python
saudacao()
```

---

## 📥 Parâmetros e Argumentos

Parâmetros são variáveis definidas na assinatura da função. Argumentos são os valores passados quando chamamos a função.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")  # Olá, João!
```

Você pode também definir valores padrão para parâmetros:

```python
def saudacao(nome="visitante"):
    print(f"Olá, {nome}!")

saudacao()          # Olá, visitante!
saudacao("Maria")   # Olá, Maria!
```

---

## 🌟 `*args` — Argumentos Posicionais Variáveis

`*args` permite passar um número indefinido de argumentos **posicionais** para uma função.

```python
def somar(*numeros):
    return sum(numeros)

print(somar(1, 2, 3))        # 6
print(somar(5, 10, 15, 20))  # 50
```

> Internamente, `args` é uma tupla.

---

## 🔑 `**kwargs` — Argumentos Nomeados Variáveis

`**kwargs` permite passar um número indefinido de argumentos **nomeados** (chave=valor) para uma função.

```python
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=25, cidade="São Paulo")
```

> Internamente, `kwargs` é um dicionário.

---

## 💡 Misturando `*args` e `**kwargs`

Você pode usar ambos na mesma função:

```python
def funcao_tudo(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)

funcao_tudo(1, 2, 3, 4, 5, nome="Carlos", ativo=True)
```

---

## 📌 Ordem dos parâmetros

A ordem correta ao declarar uma função com diferentes tipos de parâmetros é:

```
(parâmetros normais, *args, parâmetros nomeados com valor padrão, **kwargs)
```

Exemplo:

```python
def exemplo(a, b, *args, opcional=0, **kwargs):
    pass
```

---

## 🧪 Exemplo prático

```python
def apresentar_usuario(nome, idade, *hobbies, **informacoes_extra):
    print(f"Nome: {nome}, Idade: {idade}")
    print("Hobbies:", hobbies)
    print("Informações Extras:", informacoes_extra)

apresentar_usuario("Lucas", 30, "Futebol", "Cinema", cidade="Recife", ativo=True)
```

---

> ✅ Use `*args` quando não souber quantos argumentos posicionais a função receberá.
> ✅ Use `**kwargs` para capturar argumentos nomeados opcionais.

---





# 🐍 List Comprehension em Python

List Comprehension é uma forma concisa e elegante de criar listas em Python. Ela permite escrever loops e condições dentro de uma única linha.

---

## ✅ Sintaxe Básica

```python
nova_lista = [expressão for item in iterável]
```

### Exemplo:
```python
numeros = [1, 2, 3, 4, 5]
quadrados = [n**2 for n in numeros]
print(quadrados)  # [1, 4, 9, 16, 25]
```

---

## 🔁 Com Condição

```python
nova_lista = [expressão for item in iterável if condição]
```

### Exemplo:
```python
pares = [n for n in range(10) if n % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

## ⚡ Com `if` e `else`

```python
nova_lista = [valor1 if condição else valor2 for item in iterável]
```

### Exemplo:
```python
resultado = ["par" if n % 2 == 0 else "ímpar" for n in range(5)]
print(resultado)  # ['par', 'ímpar', 'par', 'ímpar', 'par']
```

---

## 💡 Compreensões Aninhadas

Você pode usar list comprehension dentro de outra.

### Exemplo: Matriz transposta

```python
matriz = [[1, 2], [3, 4], [5, 6]]
transposta = [[linha[i] for linha in matriz] for i in range(2)]
print(transposta)  # [[1, 3, 5], [2, 4, 6]]
```

---

## 📌 Vantagens

- Código mais limpo e legível
- Reduz a quantidade de linhas
- Ideal para filtragem e transformação de dados simples

---

## ⚠️ Cuidados

- Evite criar compreensões muito complexas (com muitos `if`, `else`, aninhamentos)
- Para lógicas mais elaboradas, prefira `for` tradicional

---

## 🧪 Exemplos variados

### Gerar lista com caracteres de uma string:
```python
caracteres = [letra for letra in "Python"]
print(caracteres)  # ['P', 'y', 't', 'h', 'o', 'n']
```

### Criar lista com números ao quadrado e maiores que 10:
```python
resultados = [n**2 for n in range(10) if n**2 > 10]
print(resultados)  # [16, 25, 36, 49, 64, 81]
```

---

# 🐍 Lambda

Em Python, uma **função lambda** é uma forma **rápida e concisa** de declarar **funções pequenas e simples**, sem precisar usar o `def`.

Ela é conhecida como **função anônima**, porque geralmente não recebe um nome.


## Sintaxe

```python
lambda argumentos: expressão
```

## Exemplo
```python

soma = lambda x, y: x + y
# OU
def soma(x, y): return x + y

print(soma(3, 5))  # Saída: 8
```

### Esse exemplo é equivalente a:
```python
def soma(x, y):
    return x + y
```
# 🚨 Erros

- **SyntaxError** -> Ocorre quando o Python encontra um erro de sintaxe.
- **NameError** -> Ocorre quando uma variavel ou função não foi definida
- **TypeError** -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado
- **IndexError** -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido
- **ValueError** -> Ocorre uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado
- **KeyError** -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe
- **AttributeError** -> Ocorre quando uma variável não tem um atributo/função
- **IdentationError** -> Ocorre quando não é respeitado a identação


---

# 🧱 Orientação a Objetos (POO) com Python

## O que é POO?

**Programação Orientada a Objetos (POO)** é um paradigma de programação baseado no conceito de "objetos", que são mapeamentos de elementos do mundo real representados em código.

Esses objetos possuem:

- **Atributos**: características ou dados (estado);
- **Métodos**: comportamentos ou ações que os objetos podem executar.

---

## 🧩 Elementos da POO

### ✅ Classe
É o **modelo** ou **molde** para criação de objetos. Define os atributos e métodos comuns a todos os objetos do mesmo tipo.

```python
class Pessoa:
    pass  # Classe ainda não implementada
```

### ✅ Objeto
É uma **instância** de uma classe — ou seja, um objeto criado com base naquela estrutura.

```python
p1 = Pessoa()
```

### ✅ Atributos
São as **características** dos objetos. Podem ser definidos diretamente ou no construtor.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

### ✅ Métodos
São as **ações** ou comportamentos da classe. São funções definidas dentro da classe.

```python
    def falar(self):
        print(f"{self.nome} está falando")
```

### ✅ Construtor (`__init__`)
Método especial que é executado automaticamente quando um objeto é criado.

```python
    def __init__(self, nome):
        self.nome = nome
```

---

## 🏷️ Tipos de Métodos

### 🔹 Método de Instância
- Recebe o `self` como primeiro parâmetro.
- Usa ou modifica atributos da instância.

```python
def mostrar_nome(self):
    print(self.nome)
```

### 🔹 Método de Classe (`@classmethod`)
- Recebe o `cls` como primeiro parâmetro.
- Atua sobre a classe, não em uma instância específica.

```python
@classmethod
def criar_com_desconto(cls, nome, preco, desconto):
    preco_com_desconto = preco - (preco * desconto / 100)
    return cls(nome, preco_com_desconto)
```

### 🔹 Método Estático (`@staticmethod`)
- Não recebe `self` nem `cls`.
- É uma função utilitária relacionada à classe.

```python
@staticmethod
def converter_real_para_dolar(valor):
    return valor / 5.2
```

---

## 🧩 Encapsulamento e Atributos Privados

Por convenção, atributos ou métodos iniciados com `_` (underscore) são considerados **privados** (de uso interno).

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco  # privado por convenção
```

---

## 🧠 Decorador `@property`

Permite acessar o retorno de um método como se fosse um atributo, sem precisar usar parênteses `()`.

```python
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco_com_imposto(self):
        return self._preco * 1.1

produto = Produto(100)
print(produto.preco_com_imposto)  # 110.0
```

---

## 🗂️ Serialização com `json.dump()`

Usado para **converter objetos Python em JSON** e gravar em arquivos:

```python
import json

dados = {"nome": "João", "idade": 30}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)
```





# 🧬 Herança e Polimorfismo em Python

## 🧭 Herança

A **herança** permite que uma classe (filha) herde atributos e métodos de outra classe (pai). Isso promove **reuso de código** e facilita a **organização hierárquica** dos componentes do sistema.

### ✅ Exemplo de Herança

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som do animal")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido")

class Gato(Animal):
    def emitir_som(self):
        print("Miado")
```

### ✅ Uso das classes

```python
c1 = Cachorro("Rex")
g1 = Gato("Mimi")

c1.emitir_som()  # Latido
g1.emitir_som()  # Miado
```

> A classe `Cachorro` e a `Gato` herdaram o método `emitir_som` de `Animal`, mas **sobrescreveram** esse comportamento com uma implementação própria.

---

## 🧠 Polimorfismo

**Polimorfismo** significa "muitas formas". Em POO, refere-se à capacidade de diferentes classes responderem de maneira diferente ao **mesmo método**.

### ✅ Exemplo com polimorfismo

```python
animais = [Cachorro("Bolt"), Gato("Luna")]

for animal in animais:
    animal.emitir_som()
```

### ✅ Saída

```
Latido
Miado
```

> Mesmo que os objetos estejam em uma lista do tipo `Animal`, cada um executa seu próprio método `emitir_som`. Isso é polimorfismo.

---

## 🔧 `super()` — Acessando métodos da superclasse

Você pode usar `super()` para acessar a implementação da superclasse (classe pai).

```python
class Cavalo(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def emitir_som(self):
        super().emitir_som()
        print("Relincho")
```

### ✅ Uso

```python
c = Cavalo("Spirit", "Mustang")
c.emitir_som()
```

### ✅ Saída

```
Som do animal
Relincho
```

---

## 🧩 Conclusão

- **Herança** permite o reuso e especialização de comportamentos.
- **Polimorfismo** permite tratar objetos de diferentes classes de forma genérica, chamando métodos comuns com resultados específicos.
- O uso de **`super()`** garante que comportamentos da superclasse possam ser reutilizados ou estendidos.
