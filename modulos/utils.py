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

----- ----- >> Sistema << ------ -----
    
    Digite 0 para encerrar o programa.

---- ---- >> Atualizações << ---- ----
    Personagem:
        Digite 1 para mostrar os Nomes ocupados;
        Digite 2 para mostrar as Aparências ocupadas;
        Digite 3 para mostrar os Registros ninja ocupados;       
        Digite 4 para mostrar as Bases ocupadas;
        Digite 5 para mostrar os Clãs ocupados;
        Digite 6 para mostrar a Ficha de Criação.

    Itens/NPC:
        Digite 7 para mostrar as Invocações ocupadas * em desenvolvimento * ;
        Digite 8 para mostrar as Armas ocupadas * em desenvolvimento * .

----- ------ >> Adições << ------ -----
    Digite 8 para fazer um INSERTO INTO arma * em desenvolvimento * ;
    Digite 9 para fazer um INSERT INTO invo * em desenvolvimento * ;
    Digite 10 para adicionar um novo player;
    Digite 11 para adicionar um novo personagem.
'''))
            if query == 0:
                sys.exit('\nConexão encerrada!')

            elif query == 1:
                analise_operacao = True
                select('select nome as nomes_de_personagem_em_uso FROM pp ORDER BY nome ASC;')

            elif query == 2:
                analise_operacao = True
                select('select aparencia as aparências_em_uso FROM pp ORDER BY aparencia ASC;')

            elif query == 3:
                analise_operacao = True
                select('select registro_ninja as registro_ninjas_ocupados from pp order by registro_ninja asc')

            elif query == 4: # select base
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
            elif query == 5: # select clã
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
            if query == 6:
                analise_operacao = True
                sistema_ficha = print('''『🗃️- ° } F̶i̶c̶h̶a̶ P̶e̶r̶s̶o̶n̶a̶g̶e̶m̶ { ° -🗃️』
   
       →: Identificação de Player
 ╘ N̶o̶m̶e̶ o̶u̶ N̶i̶c̶k̶ ↝: 
 ╘ N̶ú̶m̶e̶r̶o̶ T̶e̶l̶e̶f̶o̶n̶e̶ ↝: 
 ╘ R̶e̶c̶r̶u̶t̶a̶d̶o̶ P̶o̶r̶.̶.̶.̶ ↝:

       →: Identificação De Personagem
 ╘ N̶o̶m̶e̶ ↝: 
 ╘ A̶p̶a̶r̶ê̶n̶c̶i̶a̶ ↝:
 ╘ I̶d̶a̶d̶e̶ (̶A̶t̶é̶ 1̶3̶)̶ ↝:  
 ╘ S̶e̶x̶o̶ ↝: 
 ╘ T̶i̶p̶o̶ S̶a̶n̶g̶u̶í̶n̶e̶o̶ ↝: use o comando /rollsangue 

       →: Dados 
 ╘ B̶a̶s̶e̶ (̶1̶)̶ ↝:
 ╘ C̶l̶ã̶ (̶A̶t̶é̶ 2)̶ ↝: 
 ╘ E̶l̶e̶m̶e̶n̶t̶o̶ I̶n̶i̶c̶i̶a̶s̶(̶1̶)̶ ↝:
 ╘ ̶S̶h̶i̶n̶o̶b̶i / ̶N̶u̶k̶k̶e̶n̶i̶n / A̶n̶d̶a̶r̶i̶l̶h̶o̶ ↝: 
 ╘ ̶R̶e̶g̶i̶s̶t̶r̶o̶ N̶i̶n̶j̶a̶ ↝:
 ╘ D̶a̶t̶a̶ d̶e̶ C̶r̶i̶a̶ç̶ã̶o̶ ↝:''')
                try:
                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
                    if copiar == 1:
                        pyperclip.copy(sistema_ficha)
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
      
            else:
                print('O valor não corresponde. Tente novamente')
                analise_operacao = False             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
            analise_operacao = False  
    return analise_operacao