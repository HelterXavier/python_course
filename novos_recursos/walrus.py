'''
Operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.

variavel := expressão

nome = "Helter Xavier"
print(nome)

print(nome := 'Helter Xavier')
'''

# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')


cesta = []
while (fruta := input('Informe a fruta')) != 'jaca':
    cesta.append(fruta)
