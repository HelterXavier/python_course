'''
Módulos Externos
Gerenciador de pacotes do Python é chamado de pip.
-> pip install colorama -> Permitir impressão de textos coloridos no terminal.
'''

# from colorama import init, Fore, Back

# init()
# print(Fore.MAGENTA + 'Módulos Externos')
# print(Fore.RED + Back.WHITE + 'Módulos Externos')


import pydf

pdf = pydf.generate_pdf('<h1>Helter Barbosa Xavier </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
