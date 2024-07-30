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


# Função para gerar palavra aleatória

def gerar_palavra():
    # Criar uma lista com os índices das palavras que não foram utilizadas ainda baseado nas imagens dentro da pasta ./imagens
    
    indices_nao_utilizados = [i for i in range(len(palavras)) if not os.path.exists(f"imagens/imagem_{i}.png")]
    print(indices_nao_utilizados)
    # Verificar se há índices não utilizados
    if indices_nao_utilizados:
        # Escolher aleatoriamente um índice não utilizado
        index_palavra = random.choice(indices_nao_utilizados)
        # Remover o índice escolhido da lista de não utilizados
        indices_nao_utilizados.remove(index_palavra)
        # Obter a palavra correspondente ao índice escolhido
        palavra = palavras[index_palavra]
        print(index_palavra)
        nome_arquivo = f"imagem_{index_palavra}.png"

        return palavra
    else:
        # Caso todos os índices tenham sido utilizados, retornar None ou outra indicação
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
    


app = Flask(__name__)

@app.route("/")
def index():
    palavra = gerar_palavra()
    tamanho = len(palavra)
    return render_template("./index.html", palavra=palavra, tamanho=tamanho, index_palavra=palavras.index(palavra) )

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