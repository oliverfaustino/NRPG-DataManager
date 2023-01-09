from modulos.utils import *

from modulos.updater import *

from datetime import datetime

# para mostrar o dia e tempo de atualização
tempo = datetime.now()

#######################################################################
""" 
sistemas.py é o módulo principal responsável pelos sistemas do rpg quais estão integrados com o banco de dados: lista de armas ocupadas, bijuus, reencarnação e outros. É aqui que as funções trabalham seus planos(os nomes são sugestivos) de análise dos valores ocupados e quais são eles.
"""
#######################################################################

"""PLAYERS"""

def sistema_check_in():
    sistema_check_in = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ C̶h̶e̶c̶k̶ I̶n̶  ° -🚻』
    →: O que é "Check In"?

          Para alguns que já leram o sistema /check in, sabem muito bem o que isso é. Para quem não conhece, dê uma lida, basta usar o comando /check in no off. Sem mais delongas, abaixo está a atualização dos Check In, com id, nome e os pontos dos determinados player. Além do mais, agora há a tabela de status, onde mostra se o player é considerado ON ou OFF. Para ser considerado ON, é necessário ter tido alguma interação com o On do RPG, ou ganhar pontos, seja Check In ou Missão:

{select('select id_player, nome, check_in, status from player order by check_in desc, status desc, id_player asc')}'''
    print(sistema_check_in)
    copiar(sistema_check_in)
    return

def sistema_recrutamento():
    sistema_recrutamento = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ R̶e̶c̶r̶u̶t̶a̶m̶e̶n̶t̶o̶  ° -🚻』
    →: O que é "Recrutamento"?

          Recrutamento, nada mais é que a relação de um player com outro: "quem trouxe quem para o rpg". Essa informação é importante para se dar prêmios e check in, também para confirmar a validez de alguns eventos de recrutamento. Então, caso algo esteja de errado, avise. Caso esteja vendo para confirmar algo num evento de recrutamento, enteda que só é contabilizado players que são ONs:

{select('select id_player, nome, recrutador, status from player order by id_player asc')}'''
    print(sistema_recrutamento)
    copiar(sistema_recrutamento)
    return

"""PERSONAGENS"""

def sistema_nome(): 
    sistema_nome = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ N̶o̶m̶e̶s̶  ° -🚻』

       →: O que são "Nomes de PP"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem os Nomes de PPs. Os Nomes de PPs, são simplesmente os nomes que damos aos nossos personagens. Abaixo estará listado os nomes ocupados:

{select('select nome FROM pp ORDER BY nome ASC;')}'''
    print(sistema_nome)
    copiar(sistema_nome)
    return

def sistema_aparencia(): 
    sistema_aparencia = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ A̶p̶a̶r̶ê̶n̶c̶i̶a̶  ° -🚻』

       →: O que é "Aparência"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem as aparências personalizadas. As aparências, são simplesmente o visual que escolhemos para nossos personagens. Ser aparência do madara, te dá apenas aquele visual e não seus poderes! Seja coerente nas escolhas, pois determinados clãs têm uma característica única de aparência, respeite-as! Abaixo estará listado os aparências ocupadas:

{select("select id_pp, nome as nome_do_personagem, aparencia as aparência_em_uso FROM pp where aparencia <> '0' ORDER BY aparencia ASC;")}'''
    print(sistema_aparencia)
    copiar(sistema_aparencia)
    return

def sistema_patentes():
    sistema_patentes = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ P̶a̶t̶e̶n̶t̶e̶s̶ ° -🚻』
    →: O que é "Patente"?

          Cada personagem evolui de acordo com o seu esforço, as vezes por sorte... A patente não define o quão forte você é. Veja abaixou os personagems e suas patentes, além do mais, verá o quanto de pontos de missão seu personagem tem. Caso não saiba o que é pontos de missão, *veja no /missão* (se alguma estiver errada, tratar com os adms para futura atualização):

{select('select pp.id_pp, pp.nome, p.nome as patente, pontos_missao from pp, patente p where pp.id_patente = p.id_patente order by pontos_missao desc, pp.id_pp asc')}          
'''
    print(sistema_patentes)
    copiar(sistema_patentes)
    return

def sistema_elementos():
        sistema_elementos = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ E̶l̶e̶m̶e̶n̶t̶o̶s̶ ° -🚻』
    →: O que é "Elemento"?

          Assim como no anime, os elementos simplesmente é a transformação da natureza que seu personagem domina. A cada patente ganha-se 1 novo elemento (contabilizado apenas de chunnin para frente. Virar gennin não dá um elemento novo.) Veja abaixou os personagems e seus elementos (se algum estiver errado, tratar com os adms para futura atualização):

{select('select pp.id_pp, pp.nome, e1.nome as e_1, e2.nome as e_2, e3.nome e_3, e4.nome e_4, e5.nome e_5 from pp inner join elemento as e1 on pp.id_elemento_1 = e1.id_elemento inner join elemento as e2 on pp.id_elemento_2 = e2.id_elemento inner join elemento as e3 on pp.id_elemento_3 = e3.id_elemento inner join elemento as e4 on pp.id_elemento_4 = e4.id_elemento inner join elemento as e5 on pp.id_elemento_5 = e5.id_elemento order by pp.id_pp asc')}          
'''
        print(sistema_elementos)
        copiar(sistema_elementos)
        return


"""IMPORTANTES PARA CRIÇÃO DE PERSONAGEM"""

def sistema_base():
       # variável que armazenará as bases e seus slots máximos, para depois ser buscada dentro do database, para então ser limpa no sistema_base e transformada na lista de base
       """base_lista = f'''
{update_base('3° Raikage', 2)}, {update_base('4° Raikage', 1)}, {update_base('Amado', 1)}, {update_base('Boruto', 1)}{update_base('Code', 1)}, {update_base('Darui', 3)}, {update_base('Deepa', 3)}, {update_base('Deidara', 3)}, {update_base('Gaara', 3)}, {update_base('Gengetsu', 3)}, {update_base('Haku', 3)}, {update_base('Hashirama', 1)}, {update_base('Hiruko', 1)}, {update_base('Hiruzen', 2)}, {update_base('Itachi', 2)},{update_base('Jiga', 3)}, {update_base('Jigen', 1)}, {update_base('Jiraya', 3)}, {update_base('Juugo', 3)}, {update_base('Kabuto', 1)}, {update_base('Kahyo', 3)}, {update_base('Karin', 2)}, {update_base('Kashin Koji', 2)}, {update_base('Kakashi', 2)}, {update_base('Kakuzu', 3)}, {update_base('Kawaki', 1)}, {update_base('Kidoumaru', 3)}, {update_base('Kisame', 3)}, {update_base('Konan', 3)}, {update_base('Madara', 5)}, {update_base('Maito Guy', 2)}, {update_base('Mei Terumi', 2)}, {update_base('Minato', 2)}, {update_base('Muu', 2)}, {update_base('Naruto', 3)}, {update_base('Neji', 5)}, {update_base('Obito', 1)}, {update_base('Orochimaru', 1)}, {update_base('Ranmaru', 3)}, {update_base('Sakon', 3)}, {update_base('Sasori', 2)}, {update_base('Sasuke', 2)}, {update_base('Seikei', 3)}, {update_base('Shin Uchiha', 1)}, {update_base('Shinno', 1)}, {update_base('Shiranami', 1)}, {update_base('Shisui', 1)}, {update_base('Shojoji', 3)}, {update_base('Suigetsu', 5)}, {update_base('Tobirama', 1)}, {update_base('Torune', 3)}, {update_base('Tsunade', 2)}, {update_base('Utakata', 3)}, {update_base('Yakumo', 2)}'''"""

       # limpa a string base
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
_sua base pode não estar listada aqui e está tudo bem, basta avisar um adm para que ela seja adicionada :)_

{update_base('3° Raikage', 1)},
{update_base('4° Raikage', 2)}, 
{update_base('Amado', 1)}, 
{update_base('Ameyuki', 3)}, 
{update_base('Boruto', 1)},
{update_base('Code', 1)}, 
{update_base('Darui', 3)}, 
{update_base('Deepa', 3)}, 
{update_base('Deidara', 3)}, 
{update_base('Fuushin', 2)}, 
{update_base('Gaara', 3)}, 
{update_base('Gengetsu', 3)}, 
{update_base('Gengo', 3)}, 
{update_base('Haku', 3)}, 
{update_base('Hashirama', 1)}, 
{update_base('Hiruko', 1)}, 
{update_base('Hiruzen', 2)}, 
{update_base('Itachi', 2)}, 
{update_base('Jiga', 3)}, 
{update_base('Jigen', 1)}, 
{update_base('Jiraya', 3)}, 
{update_base('Juugo', 3)}, 
{update_base('Kabuto', 1)}, 
{update_base('Kahyo', 2)}, 
{update_base('Karin', 2)}, 
{update_base('Kashin Koji', 2)}, 
{update_base('Kakashi', 2)}, 
{update_base('Kakuzu', 3)}, 
{update_base('Kawaki', 1)}, 
{update_base('Kidoumaru', 3)}, 
{update_base('Kisame', 3)}, 
{update_base('Konan', 3)}, 
{update_base('Konohamaru', 3)}, 
{update_base('Kurenai', 4)}, 
{update_base('Kurotsuchi', 3)}, 
{update_base('Kushina', 3)}, 
{update_base('Naruto', 2)}, 
{update_base('Madara', 5)}, 
{update_base('Maito Guy', 2)}, 
{update_base('Mei Terumi', 2)}, 
{update_base('Minato', 2)}, 
{update_base('Mitsuki', 2)}, 
{update_base('Muu', 2)}, 
{update_base('Neji', 5)}, 
{update_base('Obito', 1)}, 
{update_base('Orochimaru', 1)},
{update_base('Ranmaru', 3)},
{update_base('Rock Lee', 2)},  
{update_base('Sakon', 3)},
{update_base('Sakura', 2)}
{update_base('Sarada', 3)}, 
{update_base('Sasori', 2)}, 
{update_base('Sasuke', 2)}, 
{update_base('Seikei', 3)}, 
{update_base('Seimei', 3)}, 
{update_base('Shin Uchiha', 1)}, 
{update_base('Shinnou', 3)}, 
{update_base('Shiranami', 1)},
{update_base('Shisui', 1)}, 
{update_base('Shira.', 3)}, 
{update_base('Shojoji', 3)}, 
{update_base('Suigetsu', 5)}, 
{update_base('Tobirama', 1)}, 
{update_base('Torune', 3)}, 
{update_base('Tsunade', 2)}, 
{update_base('Utakata', 3)}, 
{update_base('Yakumo', 2)}
{update_base('Yome', 3)}
{update_base('Yomi', 3)}
'''
       print(sistema_base)
       copiar(sistema_base)
       return

def sistema_cla():
        
        cla = """『🍃- °  Clãs, Familia, Grupos  ° -🍃』
    
    Atualizada no dia {}

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
    ● ━━━━━━━""".format(tempo.strftime('%d/%m/%Y %H:%M'), update_cla('Aburame', 10), update_cla('Akimichi', 10), update_cla('Uzumaki', 15), update_cla('Yamanaka', 10), update_cla('Nara', 10), update_cla('Inuzuka', 10),update_cla('Hagoromo', 10), update_cla('Senju', 10), update_cla('Uchiha', 20), update_cla('Hyuuga', 20), update_cla('Saturobi', 10), update_cla('Kurama', 5), update_cla('Iburi', 10), update_cla('Tsuchigumo', 5), update_cla('Kaguya', 10),update_cla('Hoshigaki', 10), update_cla('Hozuki', 10), update_cla('Kamizuru', 10), update_cla('Kazekage', 10), update_cla('Akasuna', 10), update_cla('Kamaitachi', 10), update_cla('Yotsuki', 10), update_cla('Chinoike', 10), update_cla('Juugo', 10), update_cla('Yuki', 10),update_cla('Prisão Celestial', 10), update_cla('Shiin', 10), update_cla('Fuuma', 10))

        familia = '''● ━━━━━━━ 
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
    ● ━━━━━━━'''.format(update_cla('Yome', 10), update_cla('Namikaze', 10), update_cla('Ranmaru', 10), update_cla('Guren', 10), update_cla('Karatachi', 10), update_cla('Otenki', 10), update_cla('Sakon e Ukon', 10), update_cla('Kumotami', 10), update_cla('Pakura', 10), update_cla('Bakurei', 10), update_cla('Haruno', 10), update_cla('Hatake', 10), update_cla('Maito', 5), update_cla('Lee', 5), update_cla('Terumi', 10), update_cla('Rinji', 10), update_cla('Ameyuki', 10), update_cla('Izuno', 10))

        grupo = '''● ━━━━━━━ 
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
    ● ━━━━━━━ '''.format(update_cla('Jashinista', 5), update_cla('Samurai', 5), update_cla('Nokizaru', 5))

        sistema_cla = cla + familia + grupo
        
        print(sistema_cla)
        copiar(sistema_cla)
        return


"""ITENS"""

def sistema_arma():
    sistema_arma = f'''『🗡️- °  L̶i̶s̶t̶a̶ d̶e̶ I̶t̶e̶n̶s̶,̶ A̶r̶m̶a̶s̶ e̶ A̶r̶m̶a̶m̶e̶n̶t̶o̶s̶  °🏹 -』

       →: Abordagem
╘ Nesta tabela, veremos as  I̶t̶e̶n̶s̶,̶ A̶r̶m̶a̶s̶ e̶ A̶r̶m̶a̶m̶e̶n̶t̶o̶s̶ especiais e seus respectivos donos. Está listado aqui apenas as armas que possuem algum dono: o mundo de Naruto é vasto, seria desnecessário listar as armas sem dono. _Lembrando que nosso RPG não é limitante_, se você quer e tem lógica, *você pode!* então mesmo que não tenhamos colocado a arma aqui, você pode adquirir-la. *Tudo é aceito, menos coisas fruto de Jogo.*

╘ Os itens, armas e armamentos que não tem um dono podem ser adquiridas tanto em eventos quanto na força bruta *[ leia mais sobre no /npc ]*

╘ Não trabalhe on com off através dessas tabelas do RPG. Você (player) pode até saber, mas Você (seu personagem) jamais saberá disso no puro "do nada".

● ━━━━━━━

*Atualizada no dia* {(tempo.strftime('%d/%m/%Y %H:%M'))}

{select('select a.id_arma, a.nome as Arma, pp.nome as Usuário from arma as a inner join pp on a.id_pp = pp.id_pp order by a.id_arma asc')}          
'''
    print(sistema_arma)
    copiar(sistema_arma)
    return


"""NPC's"""

def sistema_reen():
    sistema_reen = f'''『🗡️- °  L̶i̶s̶t̶a̶ d̶e̶ R̶e̶e̶n̶c̶a̶r̶n̶a̶ç̶õ̶e̶s̶ e̶ R̶e̶e̶n̶c̶a̶r̶n̶a̶d̶o̶s̶ °🏹 -』

       →: Abordagem
╘ Nesta tabela, veremos as Reencarnações especiais e seus respectivos "donos". Diferente de algumas outras tabelas, aqui está listado até mesmo a que não possuem dono, por quê? Pois reencarnações não funciona como arma, por exemplo: quero e vou atrás. Felizmente ou infelizmente as reencarnações são decididas por sorteios e também o RPG optou por trazer algumas reencarnações não mostradas no anime, mas que pela lógica Otsutsuki elas poderiam sim existir.

╘ Para entender melhor o sistema de Reencarnação *[ leia mais sobre no /reen ]*

╘ Não trabalhe on com off através dessas tabelas do RPG. Você (player) pode até saber, mas Você (seu personagem) jamais saberá disso no puro "do nada".

● ━━━━━━━

*Atualizada no dia* {(tempo.strftime('%d/%m/%Y %H:%M'))}

{select('select r.id_reen,r.nome as Reencarnado, pp.id_pp ,pp.nome as Reencarnação from reen as r left join pp on pp.id_pp = r.id_pp order by r.id_reen')}          
'''
    print(sistema_reen)
    copiar(sistema_reen)
    return

def sistema_bijuu():
    sistema_bijuu = f'''『🗡️- °  L̶i̶s̶t̶a̶ d̶e̶ B̶i̶j̶u̶u̶ e̶ J̶i̶n̶c̶h̶u̶u̶r̶i̶k̶i̶s̶ °🏹 -』

       →: Abordagem
╘ Nesta tabela, veremos as Bijuus e seus respectivos Jinchuurikis. Diferente de algumas outras tabelas, aqui está listado até mesmo a que não possuem Jinchuuriki, por quê? Mesmo que Bijuus funcionam como arma: quero! e vou atrás! O RPG optou por trazer alguns Bichos que não são Bijuus mas encaixariam muito bem no papel.

╘ Para entender melhor o sistema de Bijuus e essas "Bijuus que não são Bijuus" *[ leia mais sobre no /bijuu ]*

╘ Não trabalhe on com off através dessas tabelas do RPG. Você (player) pode até saber, mas Você (seu personagem) jamais saberá disso no puro "do nada".

● ━━━━━━━

*Atualizada no dia* {(tempo.strftime('%d/%m/%Y %H:%M'))}

{select('select b.id_bijuu, b.nome as Bijuu, pp.id_pp ,pp.nome as Jinchuuriki from bijuu as b left join pp on pp.id_pp = b.id_pp order by b.id_bijuu')}          
'''
    print(sistema_bijuu)
    copiar(sistema_bijuu)
    return

def sistema_invo():
    sistema_invo= f'''『💮- °  K̶u̶c̶h̶i̶y̶o̶s̶e̶ n̶o̶ J̶u̶t̶s̶u̶  °💮 -』

       *→: Abordagem*
╘ Invocações são um poder interessante para auxiliar a luta de um ninja e comumente é um interesse da grande massa. Para se conseguir uma invocação, primeiro *deve-se ser Chunnin*, pois é nessa patente *(ou acima dela)* que se têm o *Ticket de Arma* dos *Pergaminho de Invocação* e *Pergaminho de Contrato*, quais serão necessários. Seguido, é necessário *-de alguma forma-* conseguir chegar até sua invocação _(acho que não precisamos ressaltar a necessidade de coerência no enredo, ausência de metagame e tudo mais)_ . Por fim, consegui *-de alguma forma-* assinar o contrato com essa invocação, seja na base da porrada, seja na base do discurso, seja da forma que achar que funcione, e pronto! *És um invocador :)*

       *→: Invocação Narrada e não Narrada*
╘ As invocações que você verá abaixo são divididas em Narrada e não Narrada, ou Auto Narrada. As invocações *Autonarradas*, são aquelas que você pode, dentro de uma cena de *40 linhas* descrever como conseguiu aquela invocação, isso pois o anime não nos deixa claro como que funciona para ter aquele invocação, exemplo: *o Garuda, o Ouhamaguri, etc*. O contrário acontece com as invocações que sabemos como funciona para adquirir-las, por exemplo: *os sapos e as cobras*. Com essas invocações a necessidade de *narração é obrigatório*, então se tornará toda aquela jornada de viajar até o local da invocação *[use o comando /viagem para saber mais]* e ter toda aquela narração feita por alguém capacitado.

       *→: Contrato Mestre*
╘ Com os tipos as espécies que possuem *mais de 2 invocações*, há a possibilidade de fazer assinatura num *Contrato Mestre* com elas. Para conseguir um contrato mestre com essas invocações, basta convencer *-de alguma forma-* o líder dessas invocações e assinar o contrato. Sabemos que um Ninja com *Contrato Mestre* pode invocar qualquer uma daquelas invocações mesmo sem ter um contrato direto com elas, no *RPG* é igual, porém, isso *não exclui* a possibilidade de alguém ir lá e fazer contrato com uma das invocações e caso isso aconteça, *você não poderá mais invocar-la*. Algumas invocações *autonarradas* podem possuir *contrato mestre* e nesse caso, o *contrato mestre* não é autonarrado também, mas sim é de *autoenredo*. O player pode simplesmente ditar o enredo ideal para ir conseguir aquele contrato, ou seja, ele pode citar onde ele deve ir para encontrar esse invocações, a partir daí é quanto há uma narração como qualquer outra.

       *→: Invocações Comuns*
╘ A fim de trazer maior número de invocações e uma liberdade legal para os players, existe as *invocações comuns*, que fazem parte da espécie, porém *não são canônicas* na obra mas óbvias que existem por aí mundo a fora, já que a espécie em si não é apenas daqueles animais que são invocados. Sendo assim, as *invocações comuns* podem ser uma opção para o player. Essas invocações não fogem do padrão, não têm poderes extras e nem qualidades a mais, a única diferença é poder ter uma *aparência customizável*, mas nada além da própria espécie. *As invocações comuns não contam no Contrato Mestre.*

       *→: Lista de Invocações.*
╘ Caso a invocação que deseja não esteja ali abaixo e é existente na obra, só contactar para o conserto. 

Atualizada no dia {(tempo.strftime('%d/%m/%Y %H:%M'))}

● ━━━━━━━
🐸 Kuchiyose Sapos
● ━━━━━━━
       →: Sapos
╘ {update_invo(nome='Gamakichi', id= '1.0')} 
╘ {update_invo(nome='Gamahiro', id= '1.1')} 
╘ {update_invo(nome='Gamabunta', id= '1.2')} 
╘ {update_invo(nome='Fukasaku', id= '1.3')} 
╘ {update_invo(nome='Gamaden', id= '1.4')}
╘ {update_invo(nome='Gamagoro', id= '1.5')}
╘ {update_invo(nome='Shima', id= '1.6')}
╘ {update_invo(nome='Gamaken', id= '1.7')}
╘ {update_invo(nome='Gamaraki', id= '1.8')}
╘ {update_invo(nome='Gamatama', id= '1.9')}
╘ {update_invo(nome='Gamatatsu', id= '2.0')}
╘ {update_invo(nome='Sapo Gigante Comum', id= '2.1')}
╘ {update_invo(nome='Sapo Gigante Comum', id= '2.2')}
╘ {update_invo(nome='Contrato Mestre Dos Sapos', id= '2.3')} 
● ━━━━━━━
🦈 Kuchiyose Tubarões
● ━━━━━━━
       →: Tubarões
╘ {update_invo(nome='Tubarões', id= '3.0')} 
╘ {update_invo(nome='Tubarões', id= '3.1')} 
● ━━━━━━━
🐶 Kuchiyose Cães 
● ━━━━━━━
       →: Cães
╘ {update_invo(nome='Bull', id= '4.0')} 
╘ {update_invo(nome='Tsuiga', id= '4.1')} 
╘ {update_invo(nome='Pakkun', id= '4.2')} 
╘ {update_invo(nome='Urushi', id= '4.3')} 
╘ {update_invo(nome='Shiba', id= '4.4')} 
╘ {update_invo(nome='Bisuke', id= '4.5')} 
╘ {update_invo(nome='Akino', id= '4.6')} 
╘ {update_invo(nome='Cão Ninja Comum', id= '4.7')}
╘ {update_invo(nome='Cão Ninja Comum', id= '4.8')}
╘ {update_invo(nome='Contrato Mestre dos Cães', id= '4.9')}
╘ {update_invo(nome='Cães de Ni', id= '5.0')}
╘ {update_invo(nome='Cão de Guarda', id= '6.0')}
 
● ━━━━━━━
🐚 Kuchiyose Mariscos
● ━━━━━━━
       →: Mariscos
╘ {update_invo(nome='Ouhamaguri', id= '7.0')}
╘ {update_invo(nome='Rei Concha', id= '7.1')} 
╘ {update_invo(nome='Marisco Comum', id= '7.2')}
╘ {update_invo(nome='Marisco Comum', id= '7.3')}  
● ━━━━━━━
🐍 Kuchiyose Cobras
● ━━━━━━━
       →: Cobras
╘ {update_invo(nome='Manda', id= '8.0')} 
╘ {update_invo(nome='Aoda', id= '8.1')} 
╘ {update_invo(nome='Garaga', id= '8.2')} 
╘ {update_invo(nome='Manda 2', id= '8.3')} 
╘ {update_invo(nome='Cobra Gigante Comum', id= '8.4')}
╘ {update_invo(nome='Cobra Gigante Comum', id= '8.5')}
╘ {update_invo(nome='Cobras Comum', id= '8.6')}
╘ {update_invo(nome='Cobras Comum', id= '8.7')}
╘ {update_invo(nome='Contrato Meste', id= '8.8')}
● ━━━━━━━
🐒 Kuchiyose Macacos
● ━━━━━━━
       →: Macacos
╘ {update_invo(nome='Rei Macaco: Enma', id= '9.0')}
╘ {update_invo(nome='Enra', id= '9.1')}
╘ {update_invo(nome='Macaco Comum', id= '9.2')} 
╘ {update_invo(nome='Macaco Comum', id= '9.3')}
● ━━━━━━━
🐢 Kuchiyose Tartarugas
● ━━━━━━━
       →: Tartarugas
╘ {update_invo(nome='Ninkame', id= '10.0')}
╘ {update_invo(nome='Tartaruga Comum', id= '10.1')}
╘ {update_invo(nome='Tartaruga Comum', id= '10.2')}
● ━━━━━━━
🐌 Kuchuyise Lesmas
● ━━━━━━━
       →: Lesmas
╘ {update_invo(nome='Katsuyu', id= '11.0')}
╘ {update_invo(nome='Lesma Gigante Comum', id= '11.1')}
╘ {update_invo(nome='lesma Gigante Comum', id= '11.2')}
● ━━━━━━━
🐰 Kuchiyose Fuinhas
● ━━━━━━━
       →: Fuinhas
╘ {update_invo(nome='Kamatari', id= '12.0')}
╘ {update_invo(nome='Fuinha Comum', id= '12.1')}
╘ {update_invo(nome='Fuinha Comum', id= '12.2')}
● ━━━━━━━
🐘 Kuchiyose Anta-Elefante
● ━━━━━━━
       →: Anta-Elefante
╘ {update_invo(nome='Baku', id= '13.0')}
╘ {update_invo(nome='Anta-Elefante Comum', id= '13.1')}
╘ {update_invo(nome='Anta-Elefante Comum', id= '13.2')}
● ━━━━━━━
🦅 Kuchiyose Falcões
● ━━━━━━━
       →: Falcões
╘ {update_invo(nome='Garuda', id= '14.0')}
╘ {update_invo(nome='Águia Gigante', id= '14.1')}
╘ {update_invo(nome='Falcão Gigante Comum', id= '14.2')}
╘ {update_invo(nome='Falcão Gigante Comum', id= '14.3')}
● ━━━━━━━
🕊 Kuchiyose Corvos
● ━━━━━━━
       →: Corvos
╘ {update_invo(nome='Corvos', id= '15.0')}
╘ {update_invo(nome='Corvos', id= '15.1')}
● ━━━━━━━
🕷 Kuchiyose Aranhas
● ━━━━━━━
       →: Aranhas
╘ {update_invo(nome='Kyodaigumo', id= '16.0')} 
╘ {update_invo(nome='Aranha Gigante Comum', id= '16.1')}
╘ {update_invo(nome='Aranha Gigante Comum', id= '16.2')}
● ━━━━━━━
🦎 Salamandras
● ━━━━━━━
       →: Salamandras
╘ {update_invo(nome='Ibuse', id= '17.0')} 
╘ {update_invo(nome='Salamandra Comum', id= '17.1')}
╘ {update_invo(nome='Salamandra Comum', id= '17.2')}
● ━━━━━━━
🐟 Kuchiyose Piranhas
● ━━━━━━━
       →: Piranhas
╘ {update_invo(nome='Piranhas', id= '18.0')}
╘ {update_invo(nome='Piranhas', id= '18.1')}
● ━━━━━━━
🦝 Kuchyose Guaxinim
● ━━━━━━━
       →: Guaxinim
╘ {update_invo(nome='Ponta', id= '19.0')}
╘ {update_invo(nome='Guaxinim Comum', id= '19.1')}
╘ {update_invo(nome='Guaxinim Comum', id= '19.2')}
● ━━━━━━━
🗿 Kuchiyose Golem da Prisão de Terra
● ━━━━━━━
       →: Golem da Prisão de Terra
╘ {update_invo(nome='Golem da Prisão de Terra', id= '20.0')}
╘ {update_invo(nome='Golem da Prisão de Terra', id= '20.1')}
● ━━━━━━━
🦟Kuchiyose Inseto gigante
● ━━━━━━━
       →: Insetos
╘ {update_invo(nome='Inseto Gigante', id= '21.0')}
╘ {update_invo(nome='Inseto Gigante', id= '21.1')}
╘ {update_invo(nome='Abelha Gigante', id= '21.2')}
╘ {update_invo(nome='Abelha Gigante', id= '21.3')}
● ━━━━━━━
⛩️ Rashōmon
● ━━━━━━━
       →: Rashomon
╘ {update_invo(nome='Rashōmon Quíntuplo', id= '22.0')}
╘ {update_invo(nome='Rashōmon Triplo', id= '22.1')}
╘ {update_invo(nome='Rashōmon', id= '22.2')}
● ━━━━━━━
🦎Kuchiyose de Camaleão
● ━━━━━━━
       →: Camaleão
╘ {update_invo(nome='Shiromari', id= '23.0')}
╘ {update_invo(nome='Camaleão Comum', id= '23.1')}
╘ {update_invo(nome='Camaleão Comum', id= '23.2')}
● ━━━━━━━
       *→: Invocações do Caminho Animal de Pain*
╘ Também dentro do nível de possibilidade dos Players, as invocações de pain também é uma realidade. Para isso, basta respeitar o sistema de viagem *[leia o /viagem para mais informações]* e ir encontrar-las. Dessas, é importante lembrar que cada uma irá residir em seu habitat natural de vivência biológica, exemplo; Os pássaros gigantes irão viver nos altos das mais intensas montanhas, pelo fato de pássaros de grande porte biologicamente residirem em locais altos, assim, os ninja determinado a encarar essas criaturas, terá também que lidar com as dificuldades do local que elas habitam, sendo esses, sempre descrito pelo narrador. 

       →: 🐾Invocações Gigante do Caminho Animal
● ━━━━━━━
╘ {update_invo(nome='Yatagarasu', id= '24.0')}
╘ {update_invo(nome='Quimera Gigante', id= '24.1')}
╘ {update_invo(nome='Camaleão Gigante', id= '24.2')}
╘ {update_invo(nome='Panda Gigante', id= '24.3')}
╘ {update_invo(nome='Touro Gigante', id= '24.4')}
╘ {update_invo(nome='Rinoceronte Gigante', id= '24.5')}
╘ {update_invo(nome='Crustáceo Gigante', id= '24.6')}
╘ {update_invo(nome='Centopeia Gigante', id= '24.7')}
╘ {update_invo(nome='Contrato Mestre d/Invo de Pain', id= '24.8')}
● ━━━━━━━
       →: Nue, o Yokai
╘ No caso do Nue, as coisas são diferentes... Não é possível, de certa forma, ir buscar-la como se fosse uma invocação comum, no seu caso há duas formas de conseguir o Nue e infelizmente ambas dependerão de situações 3° no RPG. Não é possível, de acordo com a lógica do Anime, um Player comum conseguir ir BUSCAR o Nue, já que ele é fruto de uma criação, pipipi popopo. Para se conseguir o Nue, ou é em premiações de nível Bom, ou em eventos especiais onde a gente dá spanw no Nue em algum local e quem conseguir derrotar-lo vira o seu invocador.
       
       →: 🐾Invocações de Yokai
● ━━━━━━━
╘ {update_invo(nome='Nue', id= '25.0')}
● ━━━━━━━

       *→: Criação de Invocação*
╘ A quantia de animais presente no mundo de Naruto nos permite amplas coisas para abusar de nossa criatividade. Já que nos encontramos num RPG de criação, há também um sistema para poder criar uma Invocação. Embora a liberdade, não será tão simples e poucos terão a oportunidade de ter uma invocação criada: diversos obstáculos serão apresentados até se conseguir uma invocação criada. Um deles é a criatividade para criar um animal. No sistema de criação *[use o /criação para saber mais]* haverá uma ficha especial para se criar o animal desejado, basta digitar */Ficha Invocação* que terá em mãos a ficha necessária para realizar a criação de invocação. 

╘ *Já tem a ficha? Já fez sua invocação com os mais detalhes possíveis? Levou em conta de que sua invocação não pode copiar e ter muita semelhança com a habilidade de uma invocação já existente no anime?* Agora, o próximo passo é enviar para qualquer "ADM" e esperar confirmação, tenha em mente o senso para criar algo lógico e que tenha algum sentido: *as regras de criação de jutsu e armas se aplicam para invocações.* Se sua invocação for negada, terá que refazer os pontos e mandar para aprovação de novo, se for reprovado de novo, infelizmente terá que largar aquela ideia e partir para uma nova invocação caso tenha ainda o desejo de ter uma invocação personalizável. 

╘ Com sua invocação aprovada, o maior problema irá surgir para ti: *ir até a Ilha Tartaruga ou a Ilha das Invocações* Fique atento sobre isso, pois dependendo do jeito que sua invocação foi criada, ela será spawnada na *ilha da invocação*, ou na *ilha tartaruga*. Na Ilha da Tartaruga Spawna as *Invocações Racionais*, que Pensam e Falam por si só; Na Ilha das Invocações Spawna as *Invocações com Misturas genéticas*, "irracionais",mesmo irracionais, é claro que caso consiga ela, elas serão fieis apenas seus donos e semelhantes. 

╘ *Conseguiu dar um jeito de ir até a Ilha da Tartaruga ou a Ilha das Invocações?* Certo, agora está na hora de lutar com sua respectiva invocação, mas tenha em mente que não será algo fácil e poderá ocorrer muitas coisas indesejadas. Nesse sistema, *é impossível tentar pegar a invocação no discurso no jutsu*, claro, se o ninja for dotado de poderes que façam isso facilmente _(Kotoamatsukami, por exemplo)_ as coisas serão diferentes. 

╘ Leve em conta de que você poder não ser o único a pensar numa tal invocação: caso algum player tenha a mesma ideia que você, ambos terão ambas invocações aprovadas, contudo, aquele que conseguir pegar a invocação primeiro será o dono dela enquanto o outro terá sua invocação anulada por já ter um dono. Em suma é apenas isso: criar, ser aprovado e ir buscar. Um personagem só pode ter uma invocação criada.
● ━━━━━━━'''
    print(sistema_invo)
    copiar(sistema_invo)
    return