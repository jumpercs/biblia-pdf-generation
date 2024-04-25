import os
from PIL import ImageFont, Image, ImageDraw
import random


# Check if the directory exists
if not os.path.exists('genesis2'):
    # If not, create the directory
    os.makedirs('genesis2')


def gerar_imagem_palavra(texto):
    fonte_aleatoria = ImageFont.truetype(os.path.join("./fonts", random.choice(os.listdir("./fonts"))), 128)
    largura, altura = fonte_aleatoria.getbbox(texto)[2:]  # Use getbbox and get width/height


    imagem = Image.new('RGB', (largura, altura), color='white')  # Create a new image object

    # Escrever o texto na imagem com a fonte escolhida
    desenho = ImageDraw.Draw(imagem)
    desenho.text((0, 0), texto, font=fonte_aleatoria, fill="black")

    return imagem

def gerar_imagens_texto(texto):
  """
  Gera uma lista de imagens, uma para cada palavra do texto.

  Args:
      texto: O texto a ser processado.

  Returns:
      Uma lista de imagens PIL, cada uma contendo uma palavra do texto.
  """
  palavras = texto.split()
  imagens = [gerar_imagem_palavra(palavra) for palavra in palavras]
  return imagens

# Exemplo de uso:
texto = """Livro: Gênesis
Capitulo: 1
1 NO princípio criou Deus os céus e a terra.
2 E a terra era sem forma e vazia; e havia trevas sobre a face do abismo; e o Espírito de Deus se movia sobre a face das águas.
3 E disse Deus: Haja luz; e houve luz.
4 E viu Deus que era boa a luz; e fez Deus separação entre a luz e as trevas.
5 E Deus chamou à luz Dia; e às trevas chamou Noite. E foi a tarde e a manhã, o dia primeiro.
6 E disse Deus: Haja uma expansão no meio das águas, e haja separação entre águas e águas.
7 E fez Deus a expansão, e fez separação entre as águas que estavam debaixo da expansão e as águas que estavam sobre a expansão; e assim foi.
8 E chamou Deus à expansão Céus, e foi a tarde e a manhã, o dia segundo.
9 E disse Deus: Ajuntem-se as águas debaixo dos céus num lugar; e apareça a porção seca; e assim foi.
10 E chamou Deus à porção seca Terra; e ao ajuntamento das águas chamou Mares; e viu Deus que era bom.
11 E disse Deus: Produza a terra erva verde, erva que dê semente, árvore frutífera que dê fruto segundo a sua espécie, cuja semente está nela sobre a terra; e assim foi.
12 E a terra produziu erva, erva dando semente conforme a sua espécie, e a árvore frutífera, cuja semente está nela conforme a sua espécie; e viu Deus que era bom.
13 E foi a tarde e a manhã, o dia terceiro.
14 E disse Deus: Haja luminares na expansão dos céus, para haver separação entre o dia e a noite; e sejam eles para sinais e para tempos determinados e para dias e anos.
15 E sejam para luminares na expansão dos céus, para iluminar a terra; e assim foi.
16 E fez Deus os dois grandes luminares: o luminar maior para governar o dia, e o luminar menor para governar a noite; e fez as estrelas.
17 E Deus os pôs na expansão dos céus para iluminar a terra,
18 E para governar o dia e a noite, e para fazer separação entre a luz e as trevas; e viu Deus que era bom.
19 E foi a tarde e a manhã, o dia quarto.
20 E disse Deus: Produzam as águas abundantemente répteis de alma vivente; e voem as aves sobre a face da expansão dos céus.
21 E Deus criou as grandes baleias, e todo o réptil de alma vivente que as águas abundantemente produziram conforme as suas espécies; e toda a ave de asas conforme a sua espécie; e viu Deus que era bom.
22 E Deus os abençoou, dizendo: Frutificai e multiplicai-vos, e enchei as águas nos mares; e as aves se multipliquem na terra.
23 E foi a tarde e a manhã, o dia quinto.
24 E disse Deus: Produza a terra alma vivente conforme a sua espécie; gado, e répteis e feras da terra conforme a sua espécie; e assim foi.
25 E fez Deus as feras da terra conforme a sua espécie, e o gado conforme a sua espécie, e todo o réptil da terra conforme a sua espécie; e viu Deus que era bom.
26 E disse Deus: Façamos o homem à nossa imagem, conforme a nossa semelhança; e domine sobre os peixes do mar, e sobre as aves dos céus, e sobre o gado, e sobre toda a terra, e sobre todo o réptil que se
move sobre a terra.
27 E criou Deus o homem à sua imagem; à imagem de Deus o criou; homem e mulher os criou.
28 E Deus os abençoou, e Deus lhes disse: Frutificai e multiplicai-vos, e enchei a terra, e sujeitai-a; e dominai sobre os peixes do mar e sobre as aves dos céus, e sobre todo o animal que se move sobre a terra.
29 E disse Deus: Eis que vos tenho dado toda a erva que dê semente, que está sobre a face de toda a terra; e toda a árvore, em que há fruto que dê semente, ser-vos-á para mantimento.
30 E a todo o animal da terra, e a toda a ave dos céus, e a todo o réptil da terra, em que há alma vivente, toda a erva verde será para mantimento; e assim foi.
31 E viu Deus tudo quanto tinha feito, e eis que era muito bom; e foi a tarde e a manhã, o dia sexto.
Capitulo: 2
1 ASSIM os céus, a terra e todo o seu exército foram acabados.
2 E havendo Deus acabado no dia sétimo a obra que fizera, descansou no sétimo dia de toda a sua obra, que tinha feito.
3 E abençoou Deus o dia sétimo, e o santificou; porque nele descansou de toda a sua obra que Deus criara e fizera.
4 Estas são as origens dos céus e da terra, quando foram criados; no dia em que o Senhor Deus fez a terra e os céus,
5 E toda a planta do campo que ainda não estava na terra, e toda a erva do campo que ainda não brotava; porque ainda o Senhor Deus não tinha feito chover sobre a terra, e não havia homem para lavrar a terra.
6 Um vapor, porém, subia da terra, e regava toda a face da terra.
7 E formou o Senhor Deus o homem do pó da terra, e soprou em suas narinas o fôlego da vida; e o homem foi feito alma vivente.
8 E plantou o Senhor Deus um jardim no Éden, do lado oriental; e pôs ali o homem que tinha formado.
9 E o Senhor Deus fez brotar da terra toda a árvore agradável à vista, e boa para comida; e a árvore da vida no meio do jardim, e a árvore do conhecimento do bem e do mal.
10 E saía um rio do Éden para regar o jardim; e dali se dividia e se tornava em quatro braços.
11 O nome do primeiro é Pisom; este é o que rodeia toda a terra de Havilá, onde há ouro.
12 E o ouro dessa terra é bom; ali há o bdélio, e a pedra sardônica.
13 E o nome do segundo rio é Giom; este é o que rodeia toda a terra de Cuxe.
14 E o nome do terceiro rio é Hidequel; este é o que vai para o lado oriental da Assíria; e o quarto rio é o Eufrates.
15 E tomou o Senhor Deus o homem, e o pôs no jardim do Éden para o lavrar e o guardar.
16 E ordenou o Senhor Deus ao homem, dizendo: De toda a árvore do jardim comerás livremente,
17 Mas da árvore do conhecimento do bem e do mal, dela não comerás; porque no dia em que dela comeres, certamente morrerás.
18 E disse o Senhor Deus: Não é bom que o homem esteja só; far-lhe-ei uma ajudadora idônea para ele.
19 Havendo, pois, o Senhor Deus formado da terra todo o animal do campo, e toda a ave dos céus, os trouxe a Adão, para este ver como lhes chamaria; e tudo o que Adão chamou a toda a alma vivente, isso foi o
seu nome.
20 E Adão pôs os nomes a todo o gado, e às aves dos céus, e a todo o animal do campo; mas para o homem não se achava ajudadora idônea.
21 Então o Senhor Deus fez cair um sono pesado sobre Adão, e este adormeceu; e tomou uma das suas costelas, e cerrou a carne em seu lugar;
22 E da costela que o Senhor Deus tomou do homem, formou uma mulher, e trouxe-a a Adão.
23 E disse Adão: Esta é agora osso dos meus ossos, e carne da minha carne; esta será chamada mulher, porquanto do homem foi tomada.
24 Portanto deixará o homem o seu pai e a sua mãe, e apegar-se-á à sua mulher, e serão ambos uma carne.
25 E ambos estavam nus, o homem e a sua mulher; e não se envergonhavam.
Capitulo: 3
1 ORA, a serpente era mais astuta que todos os animais do campo que o Senhor Deus tinha feito. E esta disse à mulher: É assim que Deus disse: Não comereis de toda a árvore do jardim?
2 E disse a mulher à serpente: Do fruto das árvores do jardim comeremos,
3 Mas do fruto da árvore que está no meio do jardim, disse Deus: Não comereis dele, nem nele tocareis para que não morrais.
4 Então a serpente disse à mulher: Certamente não morrereis.
5 Porque Deus sabe que no dia em que dele comerdes se abrirão os vossos olhos, e sereis como Deus, sabendo o bem e o mal.
6 E viu a mulher que aquela árvore era boa para se comer, e agradável aos olhos, e árvore desejável para dar entendimento; tomou do seu fruto, e comeu, e deu também a seu marido, e ele comeu com ela.
7 Então foram abertos os olhos de ambos, e conheceram que estavam nus; e coseram folhas de figueira, e fizeram para si aventais.
8 E ouviram a voz do Senhor Deus, que passeava no jardim pela viração do dia; e esconderam-se Adão e sua mulher da presença do Senhor Deus, entre as árvores do jardim.
9 E chamou o Senhor Deus a Adão, e disse-lhe: Onde estás?
10 E ele disse: Ouvi a tua voz soar no jardim, e temi, porque estava nu, e escondi-me.
11 E Deus disse: Quem te mostrou que estavas nu? Comeste tu da árvore de que te ordenei que não comesses?
12 Então disse Adão: A mulher que me deste por companheira, ela me deu da árvore, e comi.
13 E disse o Senhor Deus à mulher: Por que fizeste isto? E disse a mulher: A serpente me enganou, e eu comi.
14 Então o Senhor Deus disse à serpente: Porquanto fizeste isto, maldita serás mais que toda a fera, e mais que todos os animais do campo; sobre o teu ventre andarás, e pó comerás todos os dias da tua vida.
15 E porei inimizade entre ti e a mulher, e entre a tua semente e a sua semente; esta te ferirá a cabeça, e tu lhe ferirás o calcanhar.
16 E à mulher disse: Multiplicarei grandemente a tua dor, e a tua conceição; com dor darás à luz filhos; e o teu desejo será para o teu marido, e ele te dominará.
17 E a Adão disse: Porquanto deste ouvidos à voz de tua mulher, e comeste da árvore de que te ordenei, dizendo: Não comerás dela, maldita é a terra por causa de ti; com dor comerás dela todos os dias da tua
vida.
18 Espinhos, e cardos também, te produzirá; e comerás a erva do campo.
19 No suor do teu rosto comerás o teu pão, até que te tornes à terra; porque dela foste tomado; porquanto és pó e em pó te tornarás.
20 E chamou Adão o nome de sua mulher Eva; porquanto era a mãe de todos os viventes.
21 E fez o Senhor Deus a Adão e à sua mulher túnicas de peles, e os vestiu.
22 Então disse o Senhor Deus: Eis que o homem é como um de nós, sabendo o bem e o mal; ora, para que não estenda a sua mão, e tome também da árvore da vida, e coma e viva eternamente,
23 O Senhor Deus, pois, o lançou fora do jardim do Éden, para lavrar a terra de que fora tomado.
24 E havendo lançado fora o homem, pôs querubins ao oriente do jardim do Éden, e uma espada inflamada que andava ao redor, para guardar o caminho da árvore da vida.
Capitulo: 4
1 E CONHECEU Adão a Eva, sua mulher, e ela concebeu e deu à luz a Caim, e disse: Alcancei do Senhor um homem.
2 E deu à luz mais a seu irmão Abel; e Abel foi pastor de ovelhas, e Caim foi lavrador da terra.
3 E aconteceu ao cabo de dias que Caim trouxe do fruto da terra uma oferta ao Senhor.
4 E Abel também trouxe dos primogênitos das suas ovelhas, e da sua gordura; e atentou o Senhor para Abel e para a sua oferta.
5 Mas para Caim e para a sua oferta não atentou. E irou-se Caim fortemente, e descaiu-lhe o semblante.
6 E o Senhor disse a Caim: Por que te iraste? E por que descaiu o teu semblante?
7 Se bem fizeres, não é certo que serás aceito? E se não fizeres bem, o pecado jaz à porta, e sobre ti será o seu desejo, mas sobre ele deves dominar.
8 E falou Caim com o seu irmão Abel; e sucedeu que, estando eles no campo, se levantou Caim contra o seu irmão Abel, e o matou.
9 E disse o Senhor a Caim: Onde está Abel, teu irmão? E ele disse: Não sei; sou eu guardador do meu irmão?
10 E disse Deus: Que fizeste? A voz do sangue do teu irmão clama a mim desde a terra.
11 E agora maldito és tu desde a terra, que abriu a sua boca para receber da tua mão o sangue do teu irmão.
12 Quando lavrares a terra, não te dará mais a sua força; fugitivo e vagabundo serás na terra.
13 Então disse Caim ao Senhor: É maior a minha maldade que a que possa ser perdoada.
14 Eis que hoje me lanças da face da terra, e da tua face me esconderei; e serei fugitivo e vagabundo na terra, e será que todo aquele que me achar, me matará.
15 O Senhor, porém, disse-lhe: Portanto qualquer que matar a Caim, sete vezes será castigado. E pôs o Senhor um sinal em Caim, para que o não ferisse qualquer que o achasse.
16 E saiu Caim de diante da face do Senhor, e habitou na terra de Node, do lado oriental do Éden.
17 E conheceu Caim a sua mulher, e ela concebeu, e deu à luz a Enoque; e ele edificou uma cidade, e chamou o nome da cidade conforme o nome de seu filho Enoque;
18 E a Enoque nasceu Irade, e Irade gerou a Meujael, e Meujael gerou a Metusael e Metusael gerou a Lameque.
19 E tomou Lameque para si duas mulheres; o nome de uma era Ada, e o nome da outra, Zilá.
20 E Ada deu à luz a Jabal; este foi o pai dos que habitam em tendas e têm gado.
21 E o nome do seu irmão era Jubal; este foi o pai de todos os que tocam harpa e órgão.
22 E Zilá também deu à luz a Tubalcaim, mestre de toda a obra de cobre e ferro; e a irmã de Tubalcaim foi Noema.
23 E disse Lameque a suas mulheres Ada e Zilá: Ouvi a minha voz; vós, mulheres de Lameque, escutai as minhas palavras; porque eu matei um homem por me ferir, e um jovem por me pisar.
24 Porque sete vezes Caim será castigado; mas Lameque setenta vezes sete.
25 E tornou Adão a conhecer a sua mulher; e ela deu à luz um filho, e chamou o seu nome Sete; porque, disse ela, Deus me deu outro filho em lugar de Abel; porquanto Caim o matou.
26 E a Sete também nasceu um filho; e chamou o seu nome Enos; então se começou a invocar o nome do Senhor.
Capitulo: 5
1 ESTE é o livro das gerações de Adão. No dia em que Deus criou o homem, à semelhança de Deus o fez.
2 Homem e mulher os criou; e os abençoou e chamou o seu nome Adão, no dia em que foram criados.
3 E Adão viveu cento e trinta anos, e gerou um filho à sua semelhança, conforme a sua imagem, e pôs-lhe o nome de Sete.
4 E foram os dias de Adão, depois que gerou a Sete, oitocentos anos, e gerou filhos e filhas.
5 E foram todos os dias que Adão viveu, novecentos e trinta anos, e morreu.
6 E viveu Sete cento e cinco anos, e gerou a Enos.
7 E viveu Sete, depois que gerou a Enos, oitocentos e sete anos, e gerou filhos e filhas.
8 E foram todos os dias de Sete novecentos e doze anos, e morreu.
9 E viveu Enos noventa anos, e gerou a Cainã.
10 E viveu Enos, depois que gerou a Cainã, oitocentos e quinze anos, e gerou filhos e filhas.
11 E foram todos os dias de Enos novecentos e cinco anos, e morreu.
12 E viveu Cainã setenta anos, e gerou a Maalalel.
13 E viveu Cainã, depois que gerou a Maalalel, oitocentos e quarenta anos, e gerou filhos e filhas.
14 E foram todos os dias de Cainã novecentos e dez anos, e morreu.
15 E viveu Maalalel sessenta e cinco anos, e gerou a Jerede.
16 E viveu Maalalel, depois que gerou a Jerede, oitocentos e trinta anos, e gerou filhos e filhas.
17 E foram todos os dias de Maalalel oitocentos e noventa e cinco anos, e morreu.
18 E viveu Jerede cento e sessenta e dois anos, e gerou a Enoque.
19 E viveu Jerede, depois que gerou a Enoque, oitocentos anos, e gerou filhos e filhas.
20 E foram todos os dias de Jerede novecentos e sessenta e dois anos, e morreu.
21 E viveu Enoque sessenta e cinco anos, e gerou a Matusalém.
22 E andou Enoque com Deus, depois que gerou a Matusalém, trezentos anos, e gerou filhos e filhas.
23 E foram todos os dias de Enoque trezentos e sessenta e cinco anos.
24 E andou Enoque com Deus; e não apareceu mais, porquanto Deus para si o tomou.
25 E viveu Matusalém cento e oitenta e sete anos, e gerou a Lameque.
26 E viveu Matusalém, depois que gerou a Lameque, setecentos e oitenta e dois anos, e gerou filhos e filhas.
27 E foram todos os dias de Matusalém novecentos e sessenta e nove anos, e morreu.
28 E viveu Lameque cento e oitenta e dois anos, e gerou um filho,
29 A quem chamou Noé, dizendo: Este nos consolará acerca de nossas obras e do trabalho de nossas mãos, por causa da terra que o Senhor amaldiçoou.
30 E viveu Lameque, depois que gerou a Noé, quinhentos e noventa e cinco anos, e gerou filhos e filhas.
31 E foram todos os dias de Lameque setecentos e setenta e sete anos, e morreu.
32 E era Noé da idade de quinhentos anos, e gerou Noé a Sem, Cão e Jafé.
Capitulo: 6
1 E ACONTECEU que, como os homens começaram a multiplicar-se sobre a face da terra, e lhes nasceram filhas,
2 Viram os filhos de Deus que as filhas dos homens eram formosas; e tomaram para si mulheres de todas as que escolheram.
3 Então disse o Senhor: Não contenderá o meu Espírito para sempre com o homem; porque ele também é carne; porém os seus dias serão cento e vinte anos.
4 Havia naqueles dias gigantes na terra; e também depois, quando os filhos de Deus entraram às filhas dos homens e delas geraram filhos; estes eram os valentes que houve na antiguidade, os homens de fama.
5 E viu o Senhor que a maldade do homem se multiplicara sobre a terra e que toda a imaginação dos pensamentos de seu coração era só má continuamente.
6 Então arrependeu-se o Senhor de haver feito o homem sobre a terra e pesou-lhe em seu coração.
7 E disse o Senhor: Destruirei o homem que criei de sobre a face da terra, desde o homem até ao animal, até ao réptil, e até à ave dos céus; porque me arrependo de os haver feito.
8 Noé, porém, achou graça aos olhos do Senhor.
9 Estas são as gerações de Noé. Noé era homem justo e perfeito em suas gerações; Noé andava com Deus.
10 E gerou Noé três filhos: Sem, Cão e Jafé.
11 A terra, porém, estava corrompida diante da face de Deus; e encheu-se a terra de violência.
12 E viu Deus a terra, e eis que estava corrompida; porque toda a carne havia corrompido o seu caminho sobre a terra.
13 Então disse Deus a Noé: O fim de toda a carne é vindo perante a minha face; porque a terra está cheia de violência; e eis que os desfarei com a terra.
14 Faze para ti uma arca da madeira de gofer; farás compartimentos na arca e a betumarás por dentro e por fora com betume.
15 E desta maneira a farás: De trezentos côvados o comprimento da arca, e de cinquenta côvados a sua largura, e de trinta côvados a sua altura.
16 Farás na arca uma janela, e de um côvado a acabarás em cima; e a porta da arca porás ao seu lado; far-lhe-ás andares, baixo, segundo e terceiro.
17 Porque eis que eu trago um dilúvio de águas sobre a terra, para desfazer toda a carne em que há espírito de vida debaixo dos céus; tudo o que há na terra expirará.
18 Mas contigo estabelecerei a minha aliança; e entrarás na arca, tu e os teus filhos, tua mulher e as mulheres de teus filhos contigo.
19 E de tudo o que vive, de toda a carne, dois de cada espécie, farás entrar na arca, para os conservar vivos contigo; macho e fêmea serão.
20 Das aves conforme a sua espécie, e dos animais conforme a sua espécie, de todo o réptil da terra conforme a sua espécie, dois de cada espécie virão a ti, para os conservar em vida.
21 E leva contigo de toda a comida que se come e ajunta-a para ti; e te será para mantimento, a ti e a eles.
22 Assim fez Noé; conforme a tudo o que Deus lhe mandou, assim o fez.
Capitulo: 7
1 DEPOIS disse o Senhor a Noé: Entra tu e toda a tua casa na arca, porque tenho visto que és justo diante de mim nesta geração.
2 De todos os animais limpos tomarás para ti sete e sete, o macho e sua fêmea; mas dos animais que não são limpos, dois, o macho e sua fêmea.
3 Também das aves dos céus sete e sete, macho e fêmea, para conservar em vida sua espécie sobre a face de toda a terra.
4 Porque, passados ainda sete dias, farei chover sobre a terra quarenta dias e quarenta noites; e desfarei de sobre a face da terra toda a substância que fiz.
5 E fez Noé conforme a tudo o que o Senhor lhe ordenara.
6 E era Noé da idade de seiscentos anos, quando o dilúvio das águas veio sobre a terra.
7 Noé entrou na arca, e com ele seus filhos, sua mulher e as mulheres de seus filhos, por causa das águas do dilúvio.
8 Dos animais limpos e dos animais que não são limpos, e das aves, e de todo o réptil sobre a terra,
9 Entraram de dois em dois para junto de Noé na arca, macho e fêmea, como Deus ordenara a Noé.
10 E aconteceu que passados sete dias, vieram sobre a terra as águas do dilúvio.
11 No ano seiscentos da vida de Noé, no mês segundo, aos dezessete dias do mês, naquele mesmo dia se romperam todas as fontes do grande abismo, e as janelas dos céus se abriram,
12 E houve chuva sobre a terra quarenta dias e quarenta noites.
13 E no mesmo dia entraram na arca Noé, seus filhos Sem, Cão e Jafé, sua mulher e as três mulheres de seus filhos.
14 Eles, e todo o animal conforme a sua espécie, e todo o gado conforme a sua espécie, e todo o réptil que se arrasta sobre a terra conforme a sua espécie, e toda a ave conforme a sua espécie, pássaros de toda
qualidade.
15 E de toda a carne, em que havia espírito de vida, entraram de dois em dois para junto de Noé na arca.
16 E os que entraram eram macho e fêmea de toda a carne, como Deus lhe tinha ordenado; e o Senhor o fechou dentro.
17 E durou o dilúvio quarenta dias sobre a terra, e cresceram as águas e levantaram a arca, e ela se elevou sobre a terra.
18 E prevaleceram as águas e cresceram grandemente sobre a terra; e a arca andava sobre a face das águas.
19 E as águas prevaleceram excessivamente sobre a terra; e todos os altos montes que havia debaixo de todo o céu, foram cobertos.
20 Quinze côvados acima prevaleceram as águas; e os montes foram cobertos.
21 E expirou toda a carne que se movia sobre a terra, tanto de ave como de gado e de feras, e de todo o réptil que se arrasta sobre a terra, e todo o homem.
22 Tudo o que tinha fôlego de espírito de vida em suas narinas, tudo o que havia em terra seca, morreu.
23 Assim foi destruído todo o ser vivente que havia sobre a face da terra, desde o homem até ao animal, até ao réptil, e até à ave dos céus; e foram extintos da terra; e ficou somente Noé, e os que com ele
estavam na arca.
24 E prevaleceram as águas sobre a terra cento e cinquenta dias.
Capitulo: 8
1 E LEMBROU-SE Deus de Noé, e de todos os seres viventes, e de todo o gado que estavam com ele na arca; e Deus fez passar um vento sobre a terra, e aquietaram-se as águas.
2 Cerraram-se também as fontes do abismo e as janelas dos céus, e a chuva dos céus deteve-se.
3 E as águas iam-se escoando continuamente de sobre a terra, e ao fim de cento e cinquenta dias minguaram.
4 E a arca repousou no sétimo mês, no dia dezessete do mês, sobre os montes de Ararate.
5 E foram as águas indo e minguando até ao décimo mês; no décimo mês, no primeiro dia do mês, apareceram os cumes dos montes.
6 E aconteceu que ao cabo de quarenta dias, abriu Noé a janela da arca que tinha feito.
7 E soltou um corvo, que saiu, indo e voltando, até que as águas se secaram de sobre a terra.
8 Depois soltou uma pomba, para ver se as águas tinham minguado de sobre a face da terra.
9 A pomba, porém, não achou repouso para a planta do seu pé, e voltou a ele para a arca; porque as águas estavam sobre a face de toda a terra; e ele estendeu a sua mão, e tomou-a, e recolheu-a consigo na arca.
10 E esperou ainda outros sete dias, e tornou a enviar a pomba fora da arca.
11 E a pomba voltou a ele à tarde; e eis, arrancada, uma folha de oliveira no seu bico; e conheceu Noé que as águas tinham minguado de sobre a terra.
12 Então esperou ainda outros sete dias, e enviou fora a pomba; mas não tornou mais a ele.
13 E aconteceu que no ano seiscentos e um, no mês primeiro, no primeiro dia do mês, as águas se secaram de sobre a terra. Então Noé tirou a cobertura da arca, e olhou, e eis que a face da terra estava enxuta.
14 E no segundo mês, aos vinte e sete dias do mês, a terra estava seca.
15 Então falou Deus a Noé dizendo:
16 Sai da arca, tu com tua mulher, e teus filhos e as mulheres de teus filhos.
17 Todo o animal que está contigo, de toda a carne, de ave, e de gado, e de todo o réptil que se arrasta sobre a terra, traze fora contigo; e povoem abundantemente a terra e frutifiquem, e se multipliquem sobre a
terra.
18 Então saiu Noé, e seus filhos, e sua mulher, e as mulheres de seus filhos com ele.
19 Todo o animal, todo o réptil, e toda a ave, e tudo o que se move sobre a terra, conforme as suas famílias, saiu para fora da arca.
20 E edificou Noé um altar ao Senhor; e tomou de todo o animal limpo e de toda a ave limpa, e ofereceu holocausto sobre o altar.
21 E o Senhor sentiu o suave cheiro, e o Senhor disse em seu coração: Não tornarei mais a amaldiçoar a terra por causa do homem; porque a imaginação do coração do homem é má desde a sua meninice, nem
tornarei mais a ferir todo o vivente, como fiz.
22 Enquanto a terra durar, sementeira e sega, e frio e calor, e verão e inverno, e dia e noite, não cessarão.
Capitulo: 9
1 E ABENÇOOU Deus a Noé e a seus filhos, e disse-lhes: Frutificai e multiplicai-vos e enchei a terra.
2 E o temor de vós e o pavor de vós virão sobre todo o animal da terra, e sobre toda a ave dos céus; tudo o que se move sobre a terra, e todos os peixes do mar, nas vossas mãos são entregues.
3 Tudo quanto se move, que é vivente, será para vosso mantimento; tudo vos tenho dado como a erva verde.
4 A carne, porém, com sua vida, isto é, com seu sangue, não comereis.
5 Certamente requererei o vosso sangue, o sangue das vossas vidas; da mão de todo o animal o requererei; como também da mão do homem, e da mão do irmão de cada um requererei a vida do homem.
6 Quem derramar o sangue do homem, pelo homem o seu sangue será derramado; porque Deus fez o homem conforme a sua imagem.
7 Mas vós frutificai e multiplicai-vos; povoai abundantemente a terra, e multiplicai-vos nela.
8 E falou Deus a Noé e a seus filhos com ele, dizendo:
9 E eu, eis que estabeleço a minha aliança convosco e com a vossa descendência depois de vós.
10 E com toda a alma vivente, que convosco está, de aves, de gado, e de todo o animal da terra convosco; com todos que saíram da arca, até todo o animal da terra.
11 E eu convosco estabeleço a minha aliança, que não será mais destruída toda a carne pelas águas do dilúvio, e que não haverá mais dilúvio, para destruir a terra.
12 E disse Deus: Este é o sinal da aliança que ponho entre mim e vós, e entre toda a alma vivente, que está convosco, por gerações eternas.
13 O meu arco tenho posto nas nuvens; este será por sinal da aliança entre mim e a terra.
14 E acontecerá que, quando eu trouxer nuvens sobre a terra, aparecerá o arco nas nuvens.
15 Então me lembrarei da minha aliança, que está entre mim e vós, e entre toda a alma vivente de toda a carne; e as águas não se tornarão mais em dilúvio para destruir toda a carne.
16 E estará o arco nas nuvens, e eu o verei, para me lembrar da aliança eterna entre Deus e toda a alma vivente de toda a carne, que está sobre a terra.
17 E disse Deus a Noé: Este é o sinal da aliança que tenho estabelecido entre mim e entre toda a carne, que está sobre a terra.
18 E os filhos de Noé, que da arca saíram, foram Sem, Cão e Jafé; e Cão é o pai de Canaã.
19 Estes três foram os filhos de Noé; e destes se povoou toda a terra.
20 E começou Noé a ser lavrador da terra, e plantou uma vinha.
21 E bebeu do vinho, e embebedou-se; e descobriu-se no meio de sua tenda.
22 E viu Cão, o pai de Canaã, a nudez do seu pai, e fê-lo saber a ambos seus irmãos no lado de fora.
23 Então tomaram Sem e Jafé uma capa, e puseram-na sobre ambos os seus ombros, e indo virados para trás, cobriram a nudez do seu pai, e os seus rostos estavam virados, de maneira que não viram a nudez do
seu pai.
24 E despertou Noé do seu vinho, e soube o que seu filho menor lhe fizera.
25 E disse: Maldito seja Canaã; servo dos servos seja aos seus irmãos.
26 E disse: Bendito seja o Senhor Deus de Sem; e seja-lhe Canaã por servo.
27 Alargue Deus a Jafé, e habite nas tendas de Sem; e seja-lhe Canaã por servo.
28 E viveu Noé, depois do dilúvio, trezentos e cinquenta anos.
29 E foram todos os dias de Noé novecentos e cinquenta anos, e morreu.
Capitulo: 10
1 ESTAS, pois, são as gerações dos filhos de Noé: Sem, Cão e Jafé; e nasceram-lhes filhos depois do dilúvio.
2 Os filhos de Jafé são: Gomer, Magogue, Madai, Javã, Tubal, Meseque e Tiras.
3 E os filhos de Gomer são: Asquenaz, Rifate e Togarma.
4 E os filhos de Javã são: Elisá, Társis, Quitim e Dodanim.
5 Por estes foram repartidas as ilhas dos gentios nas suas terras, cada qual segundo a sua língua, segundo as suas famílias, entre as suas nações.
6 E os filhos de Cão são: Cuxe, Mizraim, Pute e Canaã.
7 E os filhos de Cuxe são: Sebá, Havilá, Sabtá, Raamá e Sabtecá; e os filhos de Raamá: Sebá e Dedã.
8 E Cuxe gerou a Ninrode; este começou a ser poderoso na terra.
9 E este foi poderoso caçador diante da face do Senhor; por isso se diz: Como Ninrode, poderoso caçador diante do Senhor.
10 E o princípio do seu reino foi Babel, Ereque, Acade e Calné, na terra de Sinar.
11 Desta mesma terra saiu à Assíria e edificou a Nínive, Reobote-Ir, Calá,
12 E Resen, entre Nínive e Calá (esta é a grande cidade).
13 E Mizraim gerou a Ludim, a Anamim, a Leabim, a Naftuim,
14 A Patrusim e a Casluim (donde saíram os filisteus) e a Caftorim.
15 E Canaã gerou a Sidom, seu primogênito, e a Hete;
16 E ao jebuseu, ao amorreu, ao girgaseu,
17 E ao heveu, ao arqueu, ao sineu,
18 E ao arvadeu, ao zemareu, e ao hamateu, e depois se espalharam as famílias dos cananeus.
19 E foi o termo dos cananeus desde Sidom, indo para Gerar, até Gaza; indo para Sodoma e Gomorra, Admá e Zeboim, até Lasa.
20 Estes são os filhos de Cão segundo as suas famílias, segundo as suas línguas, em suas terras, em suas nações.
21 E a Sem nasceram filhos, e ele é o pai de todos os filhos de Éber, o irmão mais velho de Jafé.
22 Os filhos de Sem são: Elão, Assur, Arfaxade, Lude e Arã.
23 E os filhos de Arã são: Uz, Hul, Geter e Más.
24 E Arfaxade gerou a Selá; e Selá gerou a Éber.
25 E a Éber nasceram dois filhos: o nome de um foi Pelegue, porquanto em seus dias se repartiu a terra, e o nome do seu irmão foi Joctã.
26 E Joctã gerou a Almodá, a Selefe, a Hazarmavé, a Jerá,
27 A Hadorão, a Usal, a Dicla,
28 A Obal, a Abimael, a Sebá,
29 A Ofir, a Havilá e a Jobabe; todos estes foram filhos de Joctã.
30 E foi a sua habitação desde Messa, indo para Sefar, montanha do oriente.
31 Estes são os filhos de Sem segundo as suas famílias, segundo as suas línguas, nas suas terras, segundo as suas nações.
32 Estas são as famílias dos filhos de Noé segundo as suas gerações, nas suas nações; e destes foram divididas as nações na terra depois do dilúvio.
Capitulo: 11
1 E ERA toda a terra de uma mesma língua e de uma mesma fala.
2 E aconteceu que, partindo eles do oriente, acharam um vale na terra de Sinar; e habitaram ali.
3 E disseram uns aos outros: Eia, façamos tijolos e queimemo-los bem. E foi-lhes o tijolo por pedra, e o betume por cal.
4 E disseram: Eia, edifiquemos nós uma cidade e uma torre cujo cume toque nos céus, e façamo-nos um nome, para que não sejamos espalhados sobre a face de toda a terra.
5 Então desceu o Senhor para ver a cidade e a torre que os filhos dos homens edificavam;
6 E o Senhor disse: Eis que o povo é um, e todos têm uma mesma língua; e isto é o que começam a fazer; e agora, não haverá restrição para tudo o que eles intentarem fazer.
7 Eia, desçamos e confundamos ali a sua língua, para que não entenda um a língua do outro.
8 Assim o Senhor os espalhou dali sobre a face de toda a terra; e cessaram de edificar a cidade.
9 Por isso se chamou o seu nome Babel, porquanto ali confundiu o Senhor a língua de toda a terra, e dali os espalhou o Senhor sobre a face de toda a terra.
10 Estas são as gerações de Sem: Sem era da idade de cem anos e gerou a Arfaxade, dois anos depois do dilúvio.
11 E viveu Sem, depois que gerou a Arfaxade, quinhentos anos, e gerou filhos e filhas.
12 E viveu Arfaxade trinta e cinco anos, e gerou a Selá.
13 E viveu Arfaxade depois que gerou a Selá, quatrocentos e três anos, e gerou filhos e filhas.
14 E viveu Selá trinta anos, e gerou a Éber;
15 E viveu Selá, depois que gerou a Éber, quatrocentos e três anos, e gerou filhos e filhas.
16 E viveu Éber trinta e quatro anos, e gerou a Pelegue.
17 E viveu Éber, depois que gerou a Pelegue, quatrocentos e trinta anos, e gerou filhos e filhas.
18 E viveu Pelegue trinta anos, e gerou a Reú.
19 E viveu Pelegue, depois que gerou a Reú, duzentos e nove anos, e gerou filhos e filhas.
20 E viveu Reú trinta e dois anos, e gerou a Serugue.
21 E viveu Reú, depois que gerou a Serugue, duzentos e sete anos, e gerou filhos e filhas.
22 E viveu Serugue trinta anos, e gerou a Naor.
23 E viveu Serugue, depois que gerou a Naor, duzentos anos, e gerou filhos e filhas.
24 E viveu Naor vinte e nove anos, e gerou a Terá.
25 E viveu Naor, depois que gerou a Terá, cento e dezenove anos, e gerou filhos e filhas.
26 E viveu Terá setenta anos, e gerou a Abrão, a Naor, e a Harã.
27 E estas são as gerações de Terá: Terá gerou a Abrão, a Naor, e a Harã; e Harã gerou a Ló.
28 E morreu Harã estando seu pai Terá ainda vivo, na terra do seu nascimento, em Ur dos caldeus.
29 E tomaram Abrão e Naor mulheres para si: o nome da mulher de Abrão era Sarai, e o nome da mulher de Naor era Milca, filha de Harã, pai de Milca e pai de Iscá.
30 E Sarai foi estéril, não tinha filhos.
31 E tomou Terá a Abrão seu filho, e a Ló, filho de Harã, filho de seu filho, e a Sarai sua nora, mulher de seu filho Abrão, e saiu com eles de Ur dos caldeus, para ir à terra de Canaã; e vieram até Harã, e
habitaram ali.
32 E foram os dias de Terá duzentos e cinco anos, e morreu Terá em Harã.
Capitulo: 12
1 ORA, o Senhor disse a Abrão: Sai-te da tua terra, da tua parentela e da casa de teu pai, para a terra que eu te mostrarei.
2 E far-te-ei uma grande nação, e abençoar-te-ei e engrandecerei o teu nome; e tu serás uma bênção.
3 E abençoarei os que te abençoarem, e amaldiçoarei os que te amaldiçoarem; e em ti serão benditas todas as famílias da terra.
4 Assim partiu Abrão como o Senhor lhe tinha dito, e foi Ló com ele; e era Abrão da idade de setenta e cinco anos quando saiu de Harã.
5 E tomou Abrão a Sarai, sua mulher, e a Ló, filho de seu irmão, e todos os bens que haviam adquirido, e as almas que lhe acresceram em Harã; e saíram para irem à terra de Canaã; e chegaram à terra de Canaã.
6 E passou Abrão por aquela terra até ao lugar de Siquém, até ao carvalho de Moré; e estavam então os cananeus na terra.
7 E apareceu o Senhor a Abrão, e disse: À tua descendência darei esta terra. E edificou ali um altar ao Senhor, que lhe aparecera.
8 E moveu-se dali para a montanha do lado oriental de Betel, e armou a sua tenda, tendo Betel ao ocidente, e Ai ao oriente; e edificou ali um altar ao Senhor, e invocou o nome do Senhor.
9 Depois caminhou Abrão dali, seguindo ainda para o lado do sul.
10 E havia fome naquela terra; e desceu Abrão ao Egito, para peregrinar ali, porquanto a fome era grande na terra.
11 E aconteceu que, chegando ele para entrar no Egito, disse a Sarai, sua mulher: Ora, bem sei que és mulher formosa à vista;
12 E será que, quando os egípcios te virem, dirão: Esta é sua mulher. E matar-me-ão a mim, e a ti te guardarão em vida.
13 Dize, peço-te, que és minha irmã, para que me vá bem por tua causa, e que viva a minha alma por amor de ti.
14 E aconteceu que, entrando Abrão no Egito, viram os egípcios a mulher, que era mui formosa.
15 E viram-na os príncipes de Faraó, e gabaram-na diante de Faraó; e foi a mulher tomada para a casa de Faraó.
16 E fez bem a Abrão por amor dela; e ele teve ovelhas, vacas, jumentos, servos e servas, jumentas e camelos.
17 Feriu, porém, o Senhor a Faraó e a sua casa, com grandes pragas, por causa de Sarai, mulher de Abrão.
18 Então chamou Faraó a Abrão, e disse: Que é isto que me fizeste? Por que não me disseste que ela era tua mulher?
19 Por que disseste: É minha irmã? Por isso a tomei por minha mulher; agora, pois, eis aqui tua mulher; toma-a e vai-te.
20 E Faraó deu ordens aos seus homens a respeito dele; e acompanharam-no, a ele, e a sua mulher, e a tudo o que tinha.
Capitulo: 13
1 SUBIU, pois, Abrão do Egito para o lado do sul, ele e sua mulher, e tudo o que tinha, e com ele Ló.
2 E era Abrão muito rico em gado, em prata e em ouro.
3 E fez as suas jornadas do sul até Betel, até ao lugar onde a princípio estivera a sua tenda, entre Betel e Ai;
4 Até ao lugar do altar que outrora ali tinha feito; e Abrão invocou ali o nome do Senhor.
5 E também Ló, que ia com Abrão, tinha rebanhos, gado e tendas.
6 E não tinha capacidade a terra para poderem habitar juntos; porque os seus bens eram muitos; de maneira que não podiam habitar juntos.
7 E houve contenda entre os pastores do gado de Abrão e os pastores do gado de Ló; e os cananeus e os perizeus habitavam então na terra.
8 E disse Abrão a Ló: Ora, não haja contenda entre mim e ti, e entre os meus pastores e os teus pastores, porque somos irmãos.
9 Não está toda a terra diante de ti? Eia, pois, aparta-te de mim; e se escolheres a esquerda, irei para a direita; e se a direita escolheres, eu irei para a esquerda.
10 E levantou Ló os seus olhos, e viu toda a campina do Jordão, que era toda bem regada, antes do Senhor ter destruído Sodoma e Gomorra, e era como o jardim do Senhor, como a terra do Egito, quando se
entra em Zoar.
11 Então Ló escolheu para si toda a campina do Jordão, e partiu Ló para o oriente, e apartaram-se um do outro.
12 Habitou Abrão na terra de Canaã e Ló habitou nas cidades da campina, e armou as suas tendas até Sodoma.
13 Ora, eram maus os homens de Sodoma, e grandes pecadores contra o Senhor.
14 E disse o Senhor a Abrão, depois que Ló se apartou dele: Levanta agora os teus olhos, e olha desde o lugar onde estás, para o lado do norte, e do sul, e do oriente, e do ocidente;
15 Porque toda esta terra que vês, te hei de dar a ti, e à tua descendência, para sempre.
16 E farei a tua descendência como o pó da terra; de maneira que se alguém puder contar o pó da terra, também a tua descendência será contada.
17 Levanta-te, percorre essa terra, no seu comprimento e na sua largura; porque a ti a darei.
18 E Abrão mudou as suas tendas, e foi, e habitou nos carvalhais de Manre, que estão junto a Hebrom; e edificou ali um altar ao Senhor."""
imagens = gerar_imagens_texto(texto)

# Salvar as imagens na pasta imagens3
for i, imagem in enumerate(imagens):
    imagem.save(f"genesis2/imagem_{i}.png")