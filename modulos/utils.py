from datetime import datetime
import sys
import pyperclip
from modulos.cores import *
from modulos.select import *
from modulos.commit import *
from modulos.updater import *

import os

tempo = datetime.now()

#imput sobre query
def query(): 
    analise_operacao = False 
    while analise_operacao == False:
        try:
            query = int(input(f'''\nQuais operações deseja fazer? 
Atualizações;
    Digite \033[33m1 para mostrar os Nomes ocupados;
    Digite 2 para mostrar as Aparências ocupadas;
    Digite 3 para mostrar os Registros ninja ocupados;       
    Digite 4 para mostrar as Bases ocupadas;
    Digite 5 para mostrar os Clãs ocupados;

    Digite 6 para mostrar as Invocações ocupadas;
    Digite 7 para mostrar as Armas ocupadas;


Adições;
    Digite 6 para fazer um 'INSERTO INTO arma;'
    Digite 7 para fazer um 'INSERT INTO invo;'
    Digite 8 para adicionar um novo player;'
    Digite 9 para adicionar um novo personagem;'

    Digite 0 para encerrar o programa.
'''))
            if query == 0:
                sys.exit('\nConexão encerrada!')
            elif query == 1:
                analise_operacao = True
                select('select * FROM arma;')
            elif query == 2:
                analise_operacao = True
                select('select * FROM invo;')
            elif query == 3:
                analise_operacao = True
                select('select * FROM player;')
            elif query == 4:
                analise_operacao = True
                select('select * FROM pp;')
            if query == 6:
                analise_operacao = True
                sistema_invo= f'''『💮- °  K̶u̶c̶h̶i̶y̶o̶s̶e̶ n̶o̶ J̶u̶t̶s̶u̶  °💮 -』

       →: Abordagem
╘ A Técnica de Invocação é um ninjutsu de espaço-tempo que permite que o invocador transporte animais ou pessoas através de longas distâncias instantaneamente através do sangue do usuário. Antes que uma invocação animal possa ser executada, o invocador candidato deve primeiro assinar um contrato com uma determinada espécie. O contrato vem na forma de um pergaminho ESSE PERGAMINHO DEVE SER COMPRADO NO SISTEMA DE LOJA [use o comando /loja para ver sobre o pergaminho de contrato e o pergaminho de invocação], no qual o contratante usa seu próprio sangue para assinar o seu nome e colocar suas impressões digitais e, uma vez assinado, é válido mesmo após a morte dos contratantes, desde que o contrato em si permaneça intacto. Para executar um contrato com um animal ou entidade, basta você ir até eles -de alguma forma- assinar contrato com a criatura, seja por convencê-la de ser sua aliada, ou envolvendo-se em uma batalha. Requer ser Chunnin (para as invocações não narradas, deve-se realizar uma cena de 40 linhas pegando-a). É importante lembra que não listamos todas as invocações presentes no anime, apenas as mais comuns. Caso a desejada não esteja na tabela, peça para um administrador colocar-a. PARA SABER SOBRE COMO ADQUIRIR AS INVOCAÇÕES DE PAIN, VEJA NO /Npc.

● ━━━━━━━
🐸 Kuchiyose Sapos
● ━━━━━━━
       →: Sapos
╘ {atualizacao_invo(nome='Gamakichi', id= '1')} 
╘ {atualizacao_invo(nome='Gamahiro', id= '2')} 
╘ {atualizacao_invo(nome='Gamabunta', id= '3')} 
╘ {atualizacao_invo(nome='Fukasaku', id= '4')} 
╘ {atualizacao_invo(nome='Gamaden', id= '5')}
╘ {atualizacao_invo(nome='Gamagoro', id= '6')}
╘ {atualizacao_invo(nome='Shima', id= '7')}
╘ {atualizacao_invo(nome='Gamaken', id= '8')}
╘ {atualizacao_invo(nome='Gamaraki', id= '9')}
╘ {atualizacao_invo(nome='Gamatama', id= '10')}
╘ {atualizacao_invo(nome='Gamatatsu', id= '74')}
╘ {atualizacao_invo(nome='Sapo Gigante Comum', id= '11')}
╘ {atualizacao_invo(nome='Sapo Gigante Comum', id= '111')}
╘ {atualizacao_invo(nome='Contrato Mestre Dos Sapos', id= '12')} 
● ━━━━━━━
🦈 Kuchiyose Tubarões
● ━━━━━━━
       →: Tubarões
╘ {atualizacao_invo(nome='Tubarões', id= '13')} 
╘ {atualizacao_invo(nome='Tubarões', id= '133')} 
● ━━━━━━━
🐶 Kuchiyose Cães 
● ━━━━━━━
       →: Cães
╘ {atualizacao_invo(nome='Bull', id= '14')} 
╘ {atualizacao_invo(nome='Tsuiga', id= '15')} 
╘ {atualizacao_invo(nome='Pakkun', id= '16')} 
╘ {atualizacao_invo(nome='Urushi', id= '17')} 
╘ {atualizacao_invo(nome='Shiba', id= '18')} 
╘ {atualizacao_invo(nome='Bisuke', id= '19')} 
╘ {atualizacao_invo(nome='Akino', id= '199')} 
╘ {atualizacao_invo(nome='Cães de Ni', id= '20')}
╘ {atualizacao_invo(nome='Cão de Guarda', id= '21')}
╘ {atualizacao_invo(nome='Ninken Comum', id= '22')}
╘ {atualizacao_invo(nome='Ninken Comum', id= '222')} 
● ━━━━━━━
🐚 Kuchiyose Mariscos
● ━━━━━━━
       →: Mariscos
╘ Ouhamaguri: 
╘ Rei Concha: 
╘ Marisco Comum ( pode-se ter até 2 invocadores ): 
● ━━━━━━━
🐍 Kuchiyose Cobras
● ━━━━━━━
       →: Cobras
╘ Cobras Comum ( pode-se ter até 2 invocadores ):
╘ Kyodaija:
╘ Cobra Gigante Comum ( pode-se ter até 2 invocadores ):
╘ Manda: 
╘ Aoda: 
╘ Garaga:
╘ Manda 2: 
╘ Serpente de 3 cabeças:
╘ Contrato Mestre:
● ━━━━━━━
🐒 Kuchiyose Macacos
● ━━━━━━━
       →: Macacos
╘ Onbaa:
╘ Saru:
╘ Enra: 
╘ Enma:
╘ Macaco Comum ( pode-se ter até 2 invocadores ): 
● ━━━━━━━
🐢 Kuchiyose Tartarugas
● ━━━━━━━
       →: Tartarugas
╘ Ninkame:
╘ Tartaruga Comum ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🐌 Kuchuyise Lesmas
● ━━━━━━━
       →: Lesmas
╘ Katsuyu: 
╘ Lesma Gigante ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🐰 Kuchiyose Fuinhas
● ━━━━━━━
       →: Fuinhas
╘ Kamatari: 
╘ Fuinha Comum ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🐘 Kuchiyose Anta-Elefante
● ━━━━━━━
       →: Anta-Elefante
╘ Baku: 
╘ Anta-Elefante ( pode-se ter até 2 invocadores ): 
● ━━━━━━━
🦅 Kuchiyose Falcões
● ━━━━━━━
       →: Falcões
╘Falcão Comum ( pode-se ter até 2 invocadores ): 
╘ Garuda: 
╘ Águia Gigante: 
● ━━━━━━━
🕊 Kuchiyose Corvos
● ━━━━━━━
       →: Corvos
╘ Corvos Comum ( pode-se ter até 2 invocadores ): 
● ━━━━━━━
🕷 Kuchiyose Aranhas
● ━━━━━━━
       →: Aranhas
╘ Kyodaigumo: 
╘ Aranha Comum ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🦎 Salamandras
● ━━━━━━━
       →: Salamandras
╘ Ibuse: 
╘ Salamandra Comum ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🐟 Kuchiyose Piranhas
● ━━━━━━━
       →: Piranhas
╘ Cardume de Piranhas (15 piranhas. Pode-se ter até 2 invocadores ):
● ━━━━━━━
🦝 Kuchyose Guaxinim
● ━━━━━━━
       →: Guaxinim
╘ Ponta:
╘ Guaxinim Comum ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🐺 Kuchyose Lobos
● ━━━━━━━
       →: Lobos
╘Lobos Comuns ( pode-se ter até 2 invocadores ):
● ━━━━━━━
🗿 Kuchiyose Golem da Prisão de Terra
● ━━━━━━━
       →: Golem da Prisão de Terra
╘ Golem da Prisão de Terra:
● ━━━━━━━
🦟Kuchiyose Inseto gigante
● ━━━━━━━
       →: Insetos
╘ Inseto Gigante:
╘ Abelha Gigante:
● ━━━━━━━
⛩️ Rashōmon
● ━━━━━━━
       →: Rashomon
╘ Rashōmon Quíntuplo: 
╘ Rashōmon Triplo:
╘ Rashōmon:
● ━━━━━━━
🦎Kuchiyose de Camaleão
● ━━━━━━━
       →: Camaleão
╘Shiromari:
╘Camaleão Comum ( pode-se ter até 2 invocadores ): 
● ━━━━━━━
       →: 🐾Invocações Gigante do Caminho Animal
● ━━━━━━━
╘ Yatagarasu:
╘ Quimera Gigante: 
╘ Camaleão Gigante:
╘ Panda Gigante:
╘ Touro Gigante:
╘ Rinoceronte Gigante:
╘ Crustáceo Gigante:
╘ Centopeia Gigante:
● ━━━━━━━

       →: Criação de Invocação
╘ A quantia de animais presente no mundo de Naruto nos permite amplas coisas para abusar de nossa criatividade. Já que nos encontramos num RPG de criação, o sistema para poder criar uma Invocação. Embora a liberdade, não será tão simples e poucos terão a oportunidade de ter uma invocação criada, diversos obstáculos serão apresentados para o corajoso no qual almeja tal poderio. Um deles é a criatividade para criar um animal. No sistema haverá uma ficha especial para se criar o animal desejado, basta digitar /Ficha Invocação que terá em mãos a ficha necessária para realizar a criação. Já tem a ficha? Já fez sua invocação com os mais detalhes possíveis? Levou em conta de que sua invocação não pode copiar e ter muita semelhança com a habilidade de uma invocação já existente no anime? Agora, o próximo passo é enviar para qualquer ADM e esperar confirmação, tenha em mente o senso para criar algo lógico e que tenha algum sentido: a maioria das regras de criação de jutsu e armas se aplicam para invocações. Se sua invocação for negada, terá que refazer os pontos e mandar para aprovação de novo. Se for reprovado de novo, infelizmente terá que largar aquela ideia e partir para uma nova invocação caso tenha ainda o desejo de ter uma invocação personalizável. Com sua invocação aprovada, o maior problema irá surgir para ti: ir até a Ilha Tartaruga ou a Ilha das Invocações ( Na Ilha da Tartaruga você poderá haver animais racionais nos quais podem até falar e pensar por si só, enquanto na ilha das invocações pode haver animais mistos, embora são irracionais e serão fieis apenas à seus donos e semelhantes )e lutar com sua respectiva invocação, mas tenha em mente que não será algo fácil e poderá ocorrer muitas coisas indesejadas... Leve em conta de que você poder não ser o único a pensar numa tal invocação: caso algum player tenha a mesma ideia que você, ambos terão ambas invocações aprovadas, contudo, aquele que conseguir ir na Ilha Genbu (Ilha Tartaruga) e pegar a invocação primeiro, será o dono dela enquanto o outro terá sua invocação anulada por já ter um dono. Em suma é apenas isso: criar, ser aprovado e ir buscar. Um personagem só pode ter uma invocação personalizada.
● ━━━━━━━'''
                print(sistema_invo)
                try:
                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
                    if copiar == 1:
                        pyperclip.copy(sistema_base)
                        print('\nCopiado com sucesso!')
        
                    else:
                        pass
        
                except ValueError:
                    pass
            elif query == 7:
                analise_operacao = True
                commit_invo()
            elif query == 8:
                analise_operacao = True
                commit_player()
            elif query == 9:
                analise_operacao = True
                commit_pp()
            elif query == 40: # select aparencia
                analise_operacao = True
                select('select aparencia as aparências_em_uso FROM pp ORDER BY aparencia ASC;')
            elif query == 41: # select nome
                analise_operacao = True
                select('select nome as nomes_de_personagem_em_uso FROM pp ORDER BY nome ASC;')
            elif query == 42: # select base
                analise_operacao = True
                sistema_base = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ B̶a̶s̶e̶s̶  ° -🚻』

       →: O que são "Bases"?

  As Bases são a forma em que o RPG trabalha. A funcionalidade dela é dar ao seu personagem coisas únicas, que só tal personagem representou. Veja os exemplo a seguir para mais detalhes:

       →: Base Obito
  Sendo um membro do clã Uchiha -para adquirir o Sharingan- e sendo base Obito, seu personagem ao despertar seu Mangekyou Sharinga, terá o Douryuko -habilidade ocular- dos olhos do Obito, Kamui.

       →: Base Kushina
  Sendo um membro Puro do clã Uzumaki -para ter sangue puro do clã- e sendo base Kushina, seu personagem ao chegar em Jounnin terá as habilidades expressada por Kushina, o Kongo Fuusa -Correntes Adamantinas-.

        →: Conclusão
  Diversas bases e diversos clãs se combinado sabiamente podem te dar diversas vantagem. Enfim... Abaixo, estará listado todas as bases ocupadas, marcadas com um X, ou seja, quaisquer personagens que não estejam na lista, estão livres para uso. Bom proveito.

Atualizada no dia {(tempo.strftime('%d/%m/%Y %H:%M'))}

『🚹- °  L̶i̶s̶t̶a̶ d̶e̶ B̶a̶s̶e̶s̶  ° -🚹』

『❌』> {atualizacao_base('3° Raikage', 2)}
『❌』> {atualizacao_base('4° Raikage', 1)}
『❌』> {atualizacao_base('Amado', 1)}
『❌』> {atualizacao_base('Boruto', 1)}
『❌』> {atualizacao_base('Code', 1)}
『❌』> {atualizacao_base('Darui', 3)}
『❌』> {atualizacao_base('Deidara', 3)}
『❌』> {atualizacao_base('Gaara', 3)}
『❌』> {atualizacao_base('Haku', 3)}
『❌』> {atualizacao_base('Hashirama', 1)}
『❌』> {atualizacao_base('Hiruko', 1)}
『❌』> {atualizacao_base('Itachi', 2)}
『❌』> {atualizacao_base('Jigen', 1)}
『❌』> {atualizacao_base('Jiraya', 3)}
『❌』> {atualizacao_base('Juugo', 3)}
『❌』> {atualizacao_base('Kabuto', 1)}
『❌』> {atualizacao_base('Kahyo', 2)}
『❌』> {atualizacao_base('Karin', 2)}
『❌』> {atualizacao_base('Kashin Koji', 2)}
『❌』> {atualizacao_base('Kakashi', 2)}
『❌』> {atualizacao_base('Kawaki', 1)}
『❌』> {atualizacao_base('Kidoumaru', 3)}
『❌』> {atualizacao_base('Madara', 5)}
『❌』> {atualizacao_base('Mei Terumi', 2)}
『❌』> {atualizacao_base('Minato', 2)}
『❌』> {atualizacao_base('Neji', 5)}
『❌』> {atualizacao_base('Obito', 1)}
『❌』> {atualizacao_base('Orochimaru', 1)} 
『❌』> {atualizacao_base('Ranmaru', 3)}
『❌』> {atualizacao_base('Sakon', 3)}
『❌』> {atualizacao_base('Sasori', 1)}
『❌』> {atualizacao_base('Sasuke', 3)}
『❌』> {atualizacao_base('Shin Uchiha', 1)}
『❌』> {atualizacao_base('Shinno', 1)}
『❌』> {atualizacao_base('Shisui', 1)}
『❌』> {atualizacao_base('Shojoji', 3)}
『❌』> {atualizacao_base('Tobirama', 1)}
『❌』> {atualizacao_base('Tsunade', 2)}
『❌』> {atualizacao_base('Utakata', 3)}
『❌』> {atualizacao_base('Yakumo', 2)}
'''
                print(sistema_base)
                try:
                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
                    if copiar == 1:
                        pyperclip.copy(sistema_base)
                        print('\nCopiado com sucesso!')
        
                    else:
                        pass
        
                except ValueError:
                    pass
    
            elif query == 43: # select clã
                analise_operacao = True
                sistema_cla = """『🍃- °  Clãs, Familia, Grupos  ° -🍃』

 ● ━━━━━━━
『🍃- °  Clãs  ° -🍃』
● ━━━━━━━
→: {}

 Tem: Kinkaichu
 Pode-se Ter: Insetos Venenosos
 Tem: Maestria em Ninjutsu
 Tem: Controle de Chakra
● ━━━━━━━
→: {}

 Gennin: Baika no Jutsu
 Tem: Força Elevada
 Tem: Chakra Elevado
 Tem: Resistência Grandiosa
 Chunnin: Elemento Yang
● ━━━━━━━ 
→: {}

 Pode-se Ter: Talento em Fuinjutsu
 Tem: Longevidade
 Tem: Resistência
 Tem: Chakra Grande
 Tem: Vitalidade
● ━━━━━━━
→: {}

 Pode-se Ter: Conhecimento Cientifico
 Pode Ser: Prodigio
 Gennin: Shintenshin no Jutsu
 Chunnin: Elemento Yin
 Tem: Manejo de Chakra
 Tem: Sensorial
● ━━━━━━━
→: {}

 Pode-se Ter: Conhecimento Cientifico
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Gennin: Kagemane no Jutsu
 Chunnin: Elemento Yin
 Tem: Controle de Emoções
● ━━━━━━━
→: {}
  
 Pode-se Ter: 1 à 3 Cães 
 Pode-se Ter: Olfato Aguçado 
 Pode Ser: Mestre Taijutsu 
 Gennin: Cão Companheiro
 Tem: Agilidade Grandiosa
● ━━━━━━━ 
→: {}

 Tem: Controle de Chakra
 Tem: Maiores Chances de Ser Pseudo-Jinchuriki
 Tem: Chakra Elevado
 Tem: Total Compatibilidade Com Armas do Rikkudou
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Chunnin: Elemento Yang
 Tem: Dotes em Suiton e Doton
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Genialidade
 Pode-se Ter: Dotes em Genjutsu
 Pode Ser: Prodigio
 Chunnin: Elemento Yin
 Tem: Sharingan
 Tem: Dotes em Katon
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Tem: Manejo de Chakra
 Tem: Velocidade Grandiosa
 Tem: Byakugan
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Afinidade Elemental
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Pode-se Ter: Habilidade em Invocações
 Tem: Dois Elementos Iniciais
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Kekkei Genkai do Clã
 Chunnin: Elemento Yin
 Tem: Auto-Controle Mental
● ━━━━━━━ 
→: {}
 
 Chunnin: Kekkei Genkai Fumaça
 Tem: Chakra Grande
 Tem: Resistência
 Tem: Velocidade Grande
 Tem: Estabilidade da Kekkei Genkai
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Maestria em Ninjutsu
  Jounnin R/S: Kinjutsu; Dohatsuten
  Jounnin R/A: Kinjutsu; Tsuchigumoryu: Kinseijutsu Kaiho: Tenchi Kaibyaku
 Tem: Chakra Grande
 Tem: Dotes em Kinjutsu
 Tem: Grande Destreza
● ━━━━━━━
→: {} 

 Pode Ser: Prodigio
 Chunnin: Shikotsumyaku
 Tem: Manejo de Chakra
 Tem: Imunidade a Dor
 Tem: Habilidade em Taijutsu
● ━━━━━━━

→: {}
 
 Tem: DNA Tubarão
 Tem: Chakra Grandioso
 Tem: Força Apurada
 Tem: Dotes em Suiton
● ━━━━━━━ 
→: {}
 
 Pode Ser: Prodigio
 Jounnin: Hiden; Suika
 Tem: Dotes em Suiton
 Tem: Chakra Grande
 Tem: Manejo de Chakra
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Simbiose; Abelha
 Pode-se Ter: Simbiose; Vespas
 Pode-se Ter: Simbiose; Abelhas Venenosas
 Pode Ser: Prodigio
 Tem: Chakra Grande
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Genialidade
 Chunnin: Jiton
 Tem: Manejo de Chakra
 Tem: Dotes em Doton e Fuuton
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Conhecimento Cientifico
 Pode Ser: Ferreiro
 Jounnin: Dotes em Veneno
 Tem: Manejo de Marionetes
● ━━━━━━━ 
→: {}
 
 Tem: Chakra Grande
 Tem: Leque Gigante
 Tem: Kuchiyose: Kamaitachi
 Tem: Dotes em Fuuton
 Tem: Manejo de Chakra
 Tem: Habilidades em Bukijutsu
● ━━━━━━━ 
→: {}
 
 Jounnin: Ranton
 Tem: Dotes em Raiton e Suiton
 Tem: Chakra Grande
 Tem: Habilidades em Bukijutsu
● ━━━━━━━ 
→: {}
 
 Chunnin: Elemento Yin
 Tem: Ketsuryuugan
 Tem: Dotes e Suiton
 Tem: Habilidades em Genjutsu Ocular
● ━━━━━━━ 
→: {}
 
 Tem: Absorção Passiva de Energia Natural
 Tem: Força Apurada
 Tem: Resistência
 Tem: Velocidade Grande
 Tem: Senninka
● ━━━━━━━ 
→: {}

 Pode-se Ter: Hyoton
 Tem: Genialidade
 Tem: Dotes em Fuuton e Suiton
 Tem: Destreza Anormal
● ━━━━━━━ 
→: {}

 Pode Ser: Prodigio
 Jounnin: Prisão Celestial
 Tem: Chakra Elevado
 Tem: Dotes em Fuinjutsu
 Tem: Afinidade Em Katon
● ━━━━━━━
→: {}

 Pode-se Ter: Genjutsu Auditivo
 Pode-se Ter: Genialidade
 Tem: Dotes em Genjutsu
 Chunnin: Elemento Yin
 Tem: Controle de Chakra
 Tem: Manejo de Chakra
● ━━━━━━━ 
→:{}

 Pode Ser: Prodigio
 Tem: Chakra Razoavel
 Tem: Fios de Chakra Melhorados
 Jounnin E/A: Jubaku Mandara
 Jounnin E/A: Kagero Ninpo: Utakata
● ━━━━━━━""".format(atualizacao_cla('Aburame', 10), atualizacao_cla('Akimichi', 10), atualizacao_cla('Uzumaki', 15), atualizacao_cla('Yamanaka', 10), atualizacao_cla('Nara', 10), atualizacao_cla('Inuzuka', 10),atualizacao_cla('Hagoromo', 10), atualizacao_cla('Senju', 10), atualizacao_cla('Uchiha', 20), atualizacao_cla('Hyuuga', 20), atualizacao_cla('Saturobi', 10), atualizacao_cla('Kurama', 5), atualizacao_cla('Iburi', 10), atualizacao_cla('Tsuchigumo', 5), atualizacao_cla('Kaguya', 10),atualizacao_cla('Hoshigaki', 10), atualizacao_cla('Hozuki', 10), atualizacao_cla('Kamizuru', 10), atualizacao_cla('Kazekage', 10), atualizacao_cla('Akasuna', 10), atualizacao_cla('Kamaitachi', 10), atualizacao_cla('Yotsuki', 10), atualizacao_cla('Chinoike', 10), atualizacao_cla('Juugo', 10), atualizacao_cla('Yuki', 10),atualizacao_cla('Prisão Celestial', 10), atualizacao_cla('Shiin', 10), atualizacao_cla('Fuuma', 10))
                sistema_familia = '''● ━━━━━━━ 
『🍃- °  Familias  ° -🍃』

● ━━━━━━━ 
→: {}

  Pode-se Ter O Olhos Noturno
 Tem: Velocidade Apurada
 Tem: Manejo de Chakra
 Tem: Agilidade Apurada
● ━━━━━━━ 
→: {}

 Tem: Velocidade Apurada
 Tem: Resistência
 Tem: Manejo de Chakra
 Tem: Chakra Razoavel
● ━━━━━━━ 
→: {}
 
  Pode-se Ter: Akagan
 Tem: Dotes em Genjutsu 
 Tem: Manejo de Chakra
 Tem: Chakra Razoavel
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Shouton
 Pode Ser: Prodigio
 Tem: Destreza Anormal
 Tem: Manejo de Chakra
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Jounnin E/S: Suiton: Mizukagami no Jutsu
 Tem: Chakra Razoavel Alto
 Tem: Dotes em Kenjutsu
● ━━━━━━━ 
→: {}
 
 Chunnin: Controle Temporal
 Tem: Habilidade Elemental
 Tem: Manejo de Chakra
 Tem: Dotes em Ninjutsu
● ━━━━━━━ 
→: {}

 Pode-se Ter: Kekkei Genkai de Sakon e Ukon
 Pode Ser: Prodigio
 Tem: Velocidade Apurada
 Tem: Força Grandiosa
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Teia Dourada
 Pode Ser: Prodigio
 Tem: DNA de Aranha
 Tem: Resistência
 Tem: Kuchiyose: Kyodaigumo
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Shakuton
 Pode Ser: Prodigio
 Tem: Dotes em Katon e Fuuton
 Tem: Agilidade Grandiosa
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Bakuton
 Pode Ser: Prodigio
 Tem: Manejo de Chakra
 Tem: Dotes em Doton e Raiton
 Tem: Resistência
● ━━━━━━━  
→: {}

 Pode-se Ter: Conhecimento Cientifico
 Chunnin: Yin
 Jounnin: Yang
 Tem: Manejo de Chakra
 Tem: Resistência
 Tem: Força Grandiosa
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Maestria em Ninjutsu
 Pode-se Ter: Genialidade
 Pode Ser: Prodigio
 Tem: Dotes Elementais
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Hashomon
 Pode-se Ter: Força Grandiosa
 Pode-se Ter: Velocidade Apurada
 Pode-se Ter: Resistência
 Pode-se Ter: Agilidade Grandiosa
 Tem: Dedicação
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Hashomon
 Pode-se Ter: Força Grandiosa
 Pode-se Ter: Velocidade Apurada
 Pode-se Ter: Resistência
 Pode-se Ter: Agilidade  Grandiosa
 Tem: Dedicação
Incapacitado de utilizar ninjutsu ou genjutsu
● ━━━━━━━ 
→: {}
 
 Pode-se Ter: Futton
 Pode-se Ter: Yoton 
 Pode Ser: Prodigio
 Tem: Chakra Elevado
 Tem: Controle de Chakra
● ━━━━━━━ 
→: {}
 
 Tem: Doujutsu; Predição
 Tem: Manejo com Chakra
 Tem: Chakra Razoavel
 Tem: Auto-Controle
● ━━━━━━━ 
→:{}

 Pode Ser: Controle de Morcegos
 Tem: Agilidade Apurada
 Tem: Velocidade Apurada
 Tem: Auto Controle
● ━━━━━━━ 
→: {}
 
 Tem: Deiton
 Tem: Manejo com Chakra
 Tem: Chakra Grande
 Tem: Dotes em Doton
 Tem: Dotes em Suiton
 Tem: Auto-Controle
● ━━━━━━━
→: {}
 
 Tem: Arte Ninja: Capa de Gato
 Tem: Manejo com Chakra
 Tem: Agilidade Apurada
 Tem: Velocidade Apurada
 Tem: Dotes em Suiton
● ━━━━━━━'''.format(atualizacao_cla('Yome', 10), atualizacao_cla('Namikaze', 10), atualizacao_cla('Ranmaru', 10), atualizacao_cla('Guren', 10), atualizacao_cla('Karatachi', 10), atualizacao_cla('Otenki', 10), atualizacao_cla('Sakon e Ukon', 10), atualizacao_cla('Kumotami', 10), atualizacao_cla('Pakura', 10), atualizacao_cla('Bakurei', 10), atualizacao_cla('Haruno', 10), atualizacao_cla('Hatake', 10), atualizacao_cla('Maito', 5), atualizacao_cla('Lee', 5), atualizacao_cla('Terumi', 10), atualizacao_cla('Shion', 5), atualizacao_cla('Rinji', 10), atualizacao_cla('Ameyuki', 10), atualizacao_cla('Izuno', 10))
                sistema_grupo = '''● ━━━━━━━ 
『🍃- °   Grupos  ° -🍃』

● ━━━━━━━
→: {}

 Pode-se Ter: Imortalidade
 Tem: Resistência à Dor
 Tem: Destreza Anormal
● ━━━━━━━
 →: {}
 
 Pode-se Ter: Uma à quatro Katanas
 Pode Ser: Prodigio
 Tem: Resistência
 Tem: Velocidade Apurada
 Tem: Força Grande
 Tem: Agilidade Grandiosa
 Tem: Auto-Controle
● ━━━━━━━ 
→: {}
 Gennin: Camuflagem
 Jounnin: Bakuretsuchu
 Tem: Manejo de Chakra
 Tem: Dotes em Infiltração
 Tem: Auto-Controle
● ━━━━━━━ '''.format(atualizacao_cla('Jashinista', 5), atualizacao_cla('Samurai', 5), atualizacao_cla('Nokizaru', 5))
                sistema_cla_all = sistema_cla + sistema_familia + sistema_grupo
                print(sistema_cla_all)
                try:
                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
                    if copiar == 1:
                        pyperclip.copy(sistema_cla_all)
                        print('''
Copiado com sucesso!
''')
        
                    else:
                        print("")
        
                except ValueError:
                    print("")
    

            elif query == 44: # registro ninja select
                analise_operacao = True
                registro_ninja = str(select('select registro_ninja as registro_ninjas_ocupados from pp order by registro_ninja asc'))
                try:
                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
                    if copiar == 1:
                        pyperclip.copy(registro_ninja)
                        print('''
Copiado com sucesso!
''')
                    else:
                        print("")
        
                except ValueError:
                    print("")
      
            else:
                print('O valor não corresponde. Tente novamente')
                analise_operacao = False             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
            analise_operacao = False  
    return analise_operacao

"""#Query
def select(sql):
    try:
        df = str(pd.read_sql_query(sql, con=engine))
        print(df)
        try:
            copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
            if copiar == 1:
                pyperclip.copy(df)
                print('''
Copiado com sucesso!
''')
            else:
                pass

        except ValueError:
            pass
    finally:
        pass
    return df"""