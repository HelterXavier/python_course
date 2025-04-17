# Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
# imprima ela por extenso como “1 de janeiro de 20204”

def date(date_str: str):
    months = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }

    day, month, year = date_str.split('/')

    for key, value in months.items():
        if month == key:
            month = value
            break

    return f'{int(day)} de {month} de {year}'


print(date('01/01/2024'))
