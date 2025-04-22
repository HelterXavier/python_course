'''
DebugGando com PDB -> Python Debugger
'''
# Exemplo para PDB


def dividir(a, b):
    try:
        return round(int(a) / int(b), 2)
    except ZeroDivisionError as e:
        return f"Erro: {e}"


print(dividir(4, 7))
