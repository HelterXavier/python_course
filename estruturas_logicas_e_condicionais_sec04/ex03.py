# Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

num = int(input('Digite um número: '))

if num % 2 == 0:
  print(f'O {num} é par')
else:
  print(f'O {num} é impar')
