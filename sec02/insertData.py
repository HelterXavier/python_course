# print("Qual seu nome ?")
# nome = input()

# print('Seja bem-vindo(a) %s' % nome)

nome = input('Qual é o seu nome? ')
idade = int(input('Qual a sua idade ? '))
peso = float(input('Qual é seu peso ? '))

print(f'Seu nome é {nome} e você tem {idade} anos. \n Peso: {peso} KG ')

if idade >= 18:
    print('Você é maior de idade')
