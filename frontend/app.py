import random
import pytesseract 
from PIL import Image 
import io
from flask import Flask, render_template, request
import base64 # Importar a biblioteca base64
import cv2 
import numpy as np
import os


# Configurar o Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar o texto com as palavras
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    # Separar as palavras individualmente
    palavras = texto.split()
    print(palavras)
    # mapeie quais palavras ja foram usadas e quais nao
    



# Variável para controlar o índice da palavra atual


# Função para gerar palavra linearmente
def gerar_palavra():
    palavras_usadas = [False] * len(palavras)
    # use o conteudo da pasta imagens para saber quais palavras ja foram usadas
    for arquivo in os.listdir("imagens"):
        if arquivo.startswith("imagem_"):
            index_palavra = int(arquivo.split("_")[1].split(".")[0])
            palavras_usadas[index_palavra] = True
    
        
    print(palavras_usadas)
    # Verificar a primeira palavra que não foi usada ainda
    for index, usada in enumerate(palavras_usadas):
        if not usada:
            print("Palavra gerada:", palavras[index])
            print("Indice da palavra:", index)
            return palavras[index]
    return "Todas as palavras foram usadas"


    
    

# Função para verificar palavra com OCR
def verificar_palavra(imagem, palavra_correta):
    print(palavra_correta)
    texto_ocr = pytesseract.image_to_string(imagem, lang="por", config="--psm 6", output_type=pytesseract.Output.STRING, timeout=10)
    print(texto_ocr)
    
    # Armazenar a imagem em um arquivo PNG na pasta ./imagens
    

    # Verificar se a palavra correta está no texto OCR
    if palavra_correta in texto_ocr:
        return True
    else:
        return False
    


app = Flask(__name__)

@app.route("/")
def index():
    palavra = gerar_palavra()
    tamanho = len(palavra)
    return render_template("./index.html", palavra=palavra, tamanho=tamanho)

@app.route("/verificar", methods=["POST"])
def verificar():
    imagem_base64 = request.get_json()["imagem"]
    imagem_bytes = base64.b64decode(imagem_base64.split(",")[1])
    imagem = Image.open(io.BytesIO(imagem_bytes))
    palavra_correta = request.get_json()["palavra"]
    if verificar_palavra(imagem, palavra_correta):
        index_palavra = palavras.index(palavra_correta)
        print("Palavra correta")
        print("Indice da palavra:", index_palavra)
        # Salvar a imagem em um arquivo PNG
        nome_arquivo = f"imagem_{index_palavra}.png"
        imagem.save(f"imagens/{nome_arquivo}")
        
        # Retirar as partes inúteis da imagem, como o fundo
        imagem = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            # cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped_image = imagem[y:y+h, x:x+w]
            padded_image = cv2.copyMakeBorder(cropped_image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            print("Dimensões da região original:", h, "x", w)

            # cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 0), -1)
            # padded_image_resized = cv2.resize(padded_image, (w, h))
            # imagem[y:y+h, x:x+w] = padded_image_resized
        imagem = Image.fromarray(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        
        imagem.save(f"imagens/{nome_arquivo}")
        
        print(f"imagens/{nome_arquivo}")

        return "Palavra correta!"
    else:
        print("Palavra incorreta")
        return "Palavra incorreta, tente novamente."

if __name__ == "__main__":
    app.run(debug=True)