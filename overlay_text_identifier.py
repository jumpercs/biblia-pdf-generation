# identifique o texto de cada imagem dentro da pasta escritas e sobreponha-o no PDF texto_biblico.pdf.

# Path: overlay_text_identifier.py
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from fpdf import FPDF
import logging
import os

logging.basicConfig(level=logging.INFO)
def sobrepor_imagem_pdf(input_pdf, output_pdf, imagens):
    logging.info('Converting PDF to images...')
    pages = convert_from_path(input_pdf)

    for imagem in imagens:
        # Open the image and remove white margins
        overlay = Image.open(imagem)
        bbox = overlay.getbbox()
        overlay = overlay.crop(bbox)

        overlay_text = pytesseract.image_to_string(overlay, config='--psm 6')
        logging.info(f'Overlay text: {overlay_text}')

        for i, page in enumerate(pages):
            
            data = pytesseract.image_to_data(page, output_type=pytesseract.Output.DICT)
            for j in range(len(data['text'])):
                if data['text'][j].strip() == overlay_text.strip():
                    
                    x, y, w, h = data['left'][j], data['top'][j], data['width'][j], data['height'][j]
                    overlay_resized = overlay.resize((w, h))
                    
                    page.paste(overlay_resized, (x, y))

            page.save(f'page{i}.png')

    logging.info('Combining images back into a PDF...')
    pdf = FPDF()
    for i in range(len(pages)):
        pdf.add_page()
        pdf.image(f'page{i}.png', 0, 0, 210, 297)  # A4 size
    pdf.output(output_pdf, "F")

    logging.info('Done.')

# Get list of all images in the directory
imagens = [os.path.join('./escritas', img) for img in os.listdir('./escritas') if img.endswith('.png') or img.endswith('.jpg')]
# Exemplo de uso
sobrepor_imagem_pdf('texto_biblico.pdf', 'output.pdf', imagens)
# identifique o texto de cada imagem dentro da pasta escritas e sobreponha-o no PDF texto_biblico.pdf.

