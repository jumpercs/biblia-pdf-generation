import io
from PIL import Image, ImageOps
import os
import fitz  # PyMuPDF

doc = fitz.open('genesis.pdf')
new_doc = fitz.open()  # Criar um novo documento PDF limpo

for page_num in range(len(doc)):
    page = doc[page_num]
    words = page.get_text("words")
    words.sort(key=lambda w: (w[3], w[0]))
    image_folder = "./frontend/imagens"
    image_files = os.listdir(image_folder)
    image_files.sort(key=lambda f: int(f.split("_")[1].split(".")[0]))
    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)  # Criar uma nova página no novo documento
    for i, w in enumerate(words):
        x0, y0, x1, y1 = w[:4]  # rectangle where w was found
        rect = fitz.Rect(x0, y0, x1, y1)  # make rect from word bbox
        
        if i < 50:
            print(i)
            image_path = os.path.join(image_folder, image_files[i])
            image = Image.open(image_path)
            # image = ImageOps.flip(image)  # Inverter horizontalmente
            byte_stream = io.BytesIO()
            image.save(byte_stream, format='PNG')
            byte_stream.seek(0)
            new_page.insert_image(rect, stream=byte_stream, overlay=True)  # Inserir imagem na nova página
        else:
            break

new_doc.save("genesis_gerado.pdf", garbage=4, deflate=True, clean=True)  # Salvar o novo documento PDF limpo

