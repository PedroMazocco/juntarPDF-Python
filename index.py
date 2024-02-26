from PyPDF2 import PdfMerger
import os

pdf_list = os.listdir("pdfsJuntar")

juntar = PdfMerger()

for pdf in pdf_list:
    juntar.append(f'pdfsJuntar/{pdf}')

juntar.write('pronto.pdf')
print("PDF pronto!")
juntar.close()