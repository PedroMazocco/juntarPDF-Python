from PyPDF2 import PdfMerger

pdf_list = ['pdf1.pdf', 'pdf2.pdf']

juntar = PdfMerger()

for pdf in pdf_list:
    juntar.append(pdf)

juntar.write('pronto.pdf')
print("PDF pronto!")
juntar.close()