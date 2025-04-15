
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
