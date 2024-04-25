import io
from PIL import Image, ImageOps
import os
import fitz  # PyMuPDF

doc = fitz.open('texto_biblico.pdf')
for page_num in range(len(doc)):
    page = doc[page_num]
    words = page.get_text("words")  
    words.sort(key=lambda w: (w[3], w[0]))  
    image_folder = "./imagens3"
    image_files = os.listdir(image_folder)
    image_files.sort(key=lambda f: int(f.split("_")[1].split(".")[0]))  
    for i, w in enumerate(words):
        x0, y0, x1, y1 = w[:4]  
        y0_pil = page.rect.height - y1  # Convert y0 to PIL coordinates
        y1_pil = page.rect.height - y0  # Convert y1 to PIL coordinates
        rect = fitz.Rect(x0, y0_pil, x1, y1_pil)  
        if i < len(image_files):
            image_path = os.path.join(image_folder, image_files[i])
            image = Image.open(image_path)
            image = ImageOps.flip(image)  # Flip horizontally
            byte_stream = io.BytesIO()
            image.save(byte_stream, format='PNG')
            byte_stream.seek(0)
            page.insert_image(rect, stream=byte_stream, overlay=True)
        else:
            break

doc.save("primeiro_teste_texto_completo.pdf", garbage=4, deflate=True, clean=True)