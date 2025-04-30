'''
Trabalhando com Deltas

data_inicial = dd/mm/yyyy 12:55:34.9939328
data_final = dd/mm/yyyy 13:34:23.0948484

delta = data_final - data_inicial
'''
import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2026, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje

print(
    f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas')
