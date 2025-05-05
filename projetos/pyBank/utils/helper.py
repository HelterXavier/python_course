from datetime import date
from datetime import datetime


# Formatar data para string
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


# Formatar data como string para formato padrão EUA
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


# Formata moeda para float para string
def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
