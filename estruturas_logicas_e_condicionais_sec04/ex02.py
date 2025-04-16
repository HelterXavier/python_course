# Faça um programa que leia um número inteiro fornecido pelo usuário.
# Se esse número for positivo, calcule a raiz quadrada do número e apresente-a.
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido

num = int(input('Digite um número inteiro: '))

if num > 0:
  calc = num ** 2
  print(f'A raiz quadrada no número é: {calc}')
else:
  print(f'O número {num} é negativo. Número inválido')
