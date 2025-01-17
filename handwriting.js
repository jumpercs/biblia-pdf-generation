const handwritten = require('handwritten.js')
const fs = require('fs')
const rawtext = `Livro: Gênesis
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
`
handwritten(rawtext).then((converted) => {
    converted.pipe(fs.createWriteStream('output_genesis.pdf'))
})