import re
from nltk.tokenize import word_tokenize
import os



def identificar_palavras_faltantes(texto, pasta_imagens):
  # 1. Tokenizar o texto
  tokens = word_tokenize(texto, language='portuguese', preserve_line=True)
  
  # 2. Indexar imagens existentes
  indices_imagens = set()
  for nome_imagem in os.listdir(pasta_imagens):
    # Extrair o índice da imagem a partir do nome do arquivo (exemplo: "imagem_1.jpg" -> 1)
    match = re.match(r"imagem_(\d+)\.png", nome_imagem)
    if match:
      indice_imagem = int(match.group(1))
      indices_imagens.add(indice_imagem)
    

  # 3. Identificar palavras faltantes 
  indices_esperados = set(range(len(tokens)))
  indices_faltantes = indices_esperados - indices_imagens
  palavras_faltantes = [tokens[i] for i in indices_faltantes]
  #adicionar o indice da palavra faltante
  palavras_faltantes = [(i, palavra) for i, palavra in zip(indices_faltantes, palavras_faltantes)]

  
  
  return palavras_faltantes

# Teste
texto = """Livro: Gênesis
Capitulo: 1
1 NO princípio criou Deus os céus e a terra.
2 E a terra era sem forma e vazia; e havia trevas sobre a face do abismo; e o Espírito de Deus se movia sobre a face das águas.
3 E disse Deus: Haja luz; e houve luz.
4 E viu Deus que era boa a luz; e fez Deus separação entre a luz e as trevas.
5 E Deus chamou à luz Dia; e às trevas chamou Noite. E foi a tarde e a manhã, o dia primeiro."""
pasta_imagens = "imagens"
restantes = identificar_palavras_faltantes(texto, pasta_imagens)
print(restantes)
