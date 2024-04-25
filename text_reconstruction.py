import os
from fpdf import FPDF
from PIL import Image

def criar_pdf_imagens(pasta_imagens, nome_pdf):
    imagens = []
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.endswith((".png", ".jpg", ".jpeg")):  # Add more extensions if needed
            nome_base, extensao = os.path.splitext(arquivo)
            try:
                numero_imagem = int(nome_base.split("_")[-1])  # Extract number from filename
                imagens.append((numero_imagem, os.path.join(pasta_imagens, arquivo)))
            except ValueError:
                print(f"Ignoring file with invalid number: {arquivo}")

    imagens.sort(key=lambda x: x[0])  # Sort by image number

    pdf = FPDF()
    for _, caminho_imagem in imagens:
        imagem = Image.open(caminho_imagem)
        largura, altura = imagem.size
        pdf.add_page(orientation="P" if largura < altura else "L")  # Portrait or landscape based on image dimensions
        pdf.image(caminho_imagem, 0, 0, pdf.w, pdf.h)

    pdf.output(nome_pdf, "F")

# Example usage:
criar_pdf_imagens("imagens3", "texto_reconstruido.pdf")