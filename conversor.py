import fitz
pdf_documento = "paper.pdf"
documento = fitz.open(pdf_documento)
print("Número de páginas: ", documento.pageCount)
print("Metadatos: ", documento.metadata)
""" error """