import random
import pytesseract 
from PIL import Image 
import io
from flask import Flask, render_template, request
import base64 
import cv2 
import numpy as np
import os
import re
from nltk.tokenize import word_tokenize


# Configurar o Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar o texto com as palavras
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    # Separar as palavras individualmente
    palavras = texto.split()


# Função para gerar palavra aleatória
def gerar_palavra():
    # Identificar palavras faltantes com base nas imagens existentes
    palavras_faltantes = identificar_palavras_faltantes(texto, "imagens")
    print(palavras_faltantes)

    # Verificar se há palavras faltantes
    if palavras_faltantes:
        # Escolher aleatoriamente uma palavra faltante
        indice_palavra, palavra = random.choice(palavras_faltantes)
        nome_arquivo = f"imagem_{indice_palavra}.png"
        return palavra
    else:
        # Caso todas as palavras tenham sido utilizadas, retornar None ou outra indicação
        return None


# Função para verificar palavra com OCR
def verificar_palavra(imagem, palavra_correta):
    print(palavra_correta)
    texto_ocr = pytesseract.image_to_string(imagem, lang="por", config="--psm 6", output_type=pytesseract.Output.STRING, timeout=10)
    print(texto_ocr)
    
    # Armazenar a imagem em um arquivo PNG na pasta ./imagens
    nome_arquivo = "imagem_ocr.png"
    imagem.save(f"./imagens/{nome_arquivo}")

    # Verificar se a palavra correta está no texto OCR
    if palavra_correta in texto_ocr:
        return True
    else:
        return False
    


# Função para identificar palavras faltantes (mesclada)
def identificar_palavras_faltantes(texto, pasta_imagens):
    # Tokenizar o texto
    tokens = word_tokenize(texto, language='portuguese', preserve_line=True)

    # Indexar imagens existentes
    indices_imagens = set()
    for nome_imagem in os.listdir(pasta_imagens):
        match = re.match(r"imagem_(\d+)\.png", nome_imagem)
        if match:
            indice_imagem = int(match.group(1))
            indices_imagens.add(indice_imagem)

    # Identificar palavras faltantes 
    indices_esperados = set(range(len(tokens)))
    indices_faltantes = indices_esperados - indices_imagens
    palavras_faltantes = [(i, tokens[i]) for i in indices_faltantes]

    return palavras_faltantes




app = Flask(__name__)

@app.route("/")
def index():
    palavra = gerar_palavra()
    if palavra:
        tamanho = len(palavra)
        index_palavra = palavras.index(palavra)
        return render_template("./index.html", palavra=palavra, tamanho=tamanho, index_palavra=index_palavra)
    else:
        return "Todas as palavras já foram utilizadas."

@app.route("/verificar", methods=["POST"])
def verificar():
    imagem_base64 = request.get_json()["imagem"]
    imagem_bytes = base64.b64decode(imagem_base64.split(",")[1])
    imagem = Image.open(io.BytesIO(imagem_bytes))
    palavra_correta = request.get_json()["palavra"]
    if verificar_palavra(imagem, palavra_correta):
        index_palavra = palavras.index(palavra_correta)
        # Salvar a imagem em um arquivo PNG
        nome_arquivo = f"imagem_{index_palavra}.png"
        imagem.save(f"imagens/{nome_arquivo}")
        
        # Retirar as partes inúteis da imagem, como o fundo
        imagem = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        imagem = Image.fromarray(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        
        imagem.save(f"imagens/{nome_arquivo}")
        
        print(f"imagens/{nome_arquivo}")

        return "Palavra correta!"
    else:
        print("Palavra incorreta")
        return "Palavra incorreta, tente novamente."

if __name__ == "__main__":
    app.run(debug=True)