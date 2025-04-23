# Ler arquivo pdf
import os
from PyPDF2 import PdfReader

reader = PdfReader('leitura_escrita_em_arquivos/CV.pdf')
page = reader.pages[0]
text = page.extract_text()

# Pegar palavras-chave
# keywords = ['Golang']
keywords = ['Python', 'Java', 'JavaScript']

# Se existe alguma keywords no text deve mover o arquivo na pasta 'aprovados'
if any(keyword in text for keyword in keywords):
    if not os.path.exists('aprovados'):  # Se a pasta aprovados não existe
        os.makedirs('aprovados')  # criar a pasta 'aprovados' se não existir
    # move o arquivo para a pasta 'aprovados'
    os.rename('leitura_escrita_em_arquivos/CV.pdf',
              'leitura_escrita_em_arquivos/aprovados/CV.pdf')
    print('Currículo aprovado')
else:
    # Se não existe nenhuma keywords no text deve mover o arquivo na pasta 'reprovados'
    if not os.path.exists('reprovados'):  # Se a pasta reprovados não existe
        os.makedirs('reprovados')
    # criar a pasta 'reprovados' se não existir
    # move o arquivo para a pasta 'reprovados'
    os.rename('leitura_escrita_em_arquivos/CV.pdf',
              'leitura_escrita_em_arquivos/reprovados/CV.pdf')
    print('Currículo não aprovado')
