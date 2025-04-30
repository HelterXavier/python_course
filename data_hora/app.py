'''
Manipulando Data e Hora

Python tem um módulo para se trabalhar com data e hora
'''
import datetime

# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

# print(datetime.datetime.now())

# inicio = datetime.datetime.now()
# print(inicio)

# date_replace = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
# print(date_replace)


# evento = datetime.datetime(2023, 8, 25, 0)

# print(type(evento))

# print(evento)

nascimento = input('Informa sua date da nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(
    int(nascimento[2]),
    int(nascimento[1]),
    int(nascimento[0]))
print(nascimento)
