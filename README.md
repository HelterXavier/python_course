
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
