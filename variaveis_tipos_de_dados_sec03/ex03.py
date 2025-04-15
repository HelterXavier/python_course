# Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

print('Digite 3 valores inteiros!')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

sumAll = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)

print(f'A soma dos quadrados dos valores é: {sumAll}')
