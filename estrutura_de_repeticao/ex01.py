# Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0


count = 0
num = 1

while count < 5:
    if num % 3 == 0:
        print(num)
        count += 1
    num += 1
