from modulos.utils import *
from sistemas_rpg.base import *
from sistemas_rpg.cla import *

# função para mostrar junto ao sistema os nomes dos personagens
def sistema_nome(): 
    sistema_nome = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ N̶o̶m̶e̶s̶  ° -🚻』

       →: O que são "Nomes de PP"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem os Nomes de PPs. Os Nomes de PPs, são simplesmente os nomes que damos aos nossos personagens. Abaixo estará listado os nomes ocupados:

{select('select nome FROM pp ORDER BY nome ASC;')}'''
    print(sistema_nome)
    copiar(sistema_nome)
    return



# função para mostrar junto ao sistema as aparências dos personagens
def sistema_aparencia(): 
    sistema_aparencia = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ A̶p̶a̶r̶ê̶n̶c̶i̶a̶  ° -🚻』

       →: O que é "Aparência"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem as aparências personalizadas. As aparências, são simplesmente o visual que escolhemos para nossos personagens. Ser aparência do madara, te dá apenas aquele visual e não seus poderes! Seja coerente nas escolhas, pois determinados clãs têm uma característica única de aparência, respeite-as! Abaixo estará listado os aparências ocupadas:

{select('select id_pp, nome as nome_do_personagem, aparencia as aparência_em_uso FROM pp ORDER BY aparencia ASC;')}'''
    print(sistema_aparencia)
    copiar(sistema_aparencia)
    return



 # função para mostrar junto ao sistema o check in de cada personagem
def sistema_check_in():
    sistema_check_in = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ C̶h̶e̶c̶k̶ I̶n̶  ° -🚻』
    →: O que é "Check In"?

          Para alguns que já leram o sistema /check in, sabem muito bem o que isso é. Para quem não conhece, dê uma lida, basta usar o comando /check in no off. Sem mais delongas, abaixo está a atualização dos Check In, com id, nome e os pontos dos determinados player (players com 0 de check in não aparecem):

{select('select id_player, check_in, nome from player where check_in <> 0 order by check_in desc')}'''
    return



 # função parar mostrar junto ao sistema a patente de cada peronagem
def sistema_patentes():
    sistema_patentes = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ P̶a̶t̶e̶n̶t̶e̶s̶ ° -🚻』
    →: O que é "Patente"?

          Cada personagem evolui de acordo com o seu esforço, as vezes por sorte... A patente não define o quão forte você é. Veja abaixou os personagems e suas patentes (se alguma estiver errada, tratar com os adms para futura atualização):

{select('select pp.id_pp, pp.nome, p.nome as patente from pp, patente p where pp.id_patente = p.id_patente order by pp.id_pp asc')}          
'''
    print(sistema_patentes)
    copiar(sistema_patentes)
    return



 # função parar mostrar junto ao sistema o elkemento de cada peronagem
def sistema_elementos():
        sistema_elementos = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ E̶l̶e̶m̶e̶n̶t̶o̶s̶ ° -🚻』
    →: O que é "Elemento"?

          Assim como no anime, os elementos simplesmente é a transformação da natureza que seu personagem domina. A cada patente ganha-se 1 novo elemento (contabilizado apenas de chunnin para frente. Virar gennin não dá um elemento novo.) Veja abaixou os personagems e seus elementos (se algum estiver errado, tratar com os adms para futura atualização):

{select('select pp.id_pp, pp.nome, e1.nome as e_1, e2.nome as e_2, e3.nome e_3, e4.nome e_4, e5.nome e_5 from pp inner join elemento as e1 on pp.id_elemento_1 = e1.id_elemento inner join elemento as e2 on pp.id_elemento_2 = e2.id_elemento inner join elemento as e3 on pp.id_elemento_3 = e3.id_elemento inner join elemento as e4 on pp.id_elemento_4 = e4.id_elemento inner join elemento as e5 on pp.id_elemento_5 = e5.id_elemento order by pp.id_pp asc')}          
'''
        print(sistema_elementos)
        copiar(sistema_elementos)
        return



# armazena o sistema de bases adicional à lista de bases
def sistema_base():
        # limpa a string base
        base_limpa = base_lista.replace('None','').replace(', ','').replace('『', '\n')
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

{base_limpa}
'''
        print(sistema_base)
        copiar(sistema_base)
        return



# armazena as informações do clã adicional à lista de de clãs
def sistema_cla():
        sistema_cla = cla + familia + grupo
        
        print(sistema_cla)
        copiar(sistema_cla)
        return