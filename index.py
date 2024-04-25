import pytesseract
from PIL import Image, ImageDraw
from pdf2image import convert_from_path
from fpdf import FPDF
import logging

logging.basicConfig(level=logging.INFO)

def sobrepor_imagem_pdf(input_pdf, output_pdf, imagem):
    logging.info('Converting PDF to images...')
    pages = convert_from_path(input_pdf)

    for i, page in enumerate(pages):
        logging.info(f'Processing page {i+1}...')
        data = pytesseract.image_to_data(page, output_type=pytesseract.Output.DICT)

        overlay_text = pytesseract.image_to_string(Image.open(imagem), config='--psm 6')
        
        logging.info(f'Overlay text: {overlay_text}')

        for j in range(len(data['text'])):
           

            if data['text'][j].strip() == overlay_text.strip():
                logging.info(f'Found text "{overlay_text}" at position {j}...')
                x, y, w, h = data['left'][j], data['top'][j], data['width'][j], data['height'][j]
                overlay = Image.open(imagem)
                overlay = overlay.resize((w, h))
                logging.info(f'Overlay position: {x}, {y}')
                page.paste(overlay, (x, y))

        page.save(f'page{i}.png')

    logging.info('Combining images back into a PDF...')
    pdf = FPDF()
    for i in range(len(pages)):
        pdf.add_page()
        pdf.image(f'page{i}.png', 0, 0, 210, 297)  # A4 size
    pdf.output(output_pdf, "F")

    logging.info('Done.')

# Exemplo de uso
sobrepor_imagem_pdf('texto_biblico.pdf', 'output.pdf', 'imagem_palavra2.png')


def draw_boxes(image_path, output_path):
    # Open image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Use pytesseract to get bounding boxes
    boxes = pytesseract.image_to_boxes(image)

    # Draw boxes on image
    for box in boxes.splitlines():
        b = box.split(' ')
        draw.rectangle(((int(b[1]), int(b[2])), (int(b[3]), int(b[4]))), outline='green')
        padding = 5
        draw.text((int(b[1])+padding, int(b[2])+padding), b[0], fill='green') 

    

    # Save image
    image.save(output_path)

# Example usage
draw_boxes('imagem_palavra2.png', 'output.png')