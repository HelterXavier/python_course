from models.cliente import Cliente
from models.conta import Conta

helter: Cliente = Cliente(
    'Helter Xavier', 'helter.xavier@semeq.com', '123.456.789-01', '17/11/1998')
raissa: Cliente = Cliente(
    'Raíssa Xavier', 'raissa.xavier@gmail.com', '123.456.789-01', '17/10/2003')


# print(helter)
# print(raissa)


contaf: Conta = Conta(helter)
contaa: Conta = Conta(raissa)


print(contaf)
print(contaa)
