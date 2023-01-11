from modulos.utils import *

def sistema_nome(): # função para mostrar junto ao sistema os nomes dos personagens
    sistema_nome = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ N̶o̶m̶e̶s̶  ° -🚻』

       →: O que são "Nomes de PP"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem os Nomes de PPs. Os Nomes de PPs, são simplesmente os nomes que damos aos nossos personagens. Abaixo estará listado os nomes ocupados:

{select('select nome FROM pp ORDER BY nome ASC;')}'''
    print(sistema_nome)
    copiar(sistema_nome)
    return



def sistema_aparencia(): # função para mostrar junto ao sistema as aparências dos personagens
    sistema_aparencia = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ A̶p̶a̶r̶ê̶n̶c̶i̶a̶  ° -🚻』

       →: O que é "Aparência"?

          Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem as aparências personalizadas. As aparências, são simplesmente o visual que escolhemos para nossos personagens. Ser aparência do madara, te dá apenas aquele visual e não seus poderes! Seja coerente nas escolhas, pois determinados clãs têm uma característica única de aparência, respeite-as! Abaixo estará listado os aparências ocupadas:

{select('select id_pp, nome as nome_do_personagem, aparencia as aparência_em_uso FROM pp ORDER BY aparencia ASC;')}'''
    print(sistema_aparencia)
    copiar(sistema_aparencia)
    return

def sistema_check_in(): # função para mostrar junto ao sistema o check in de cada personagem
    sistema_check_in = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ C̶h̶e̶c̶k̶ I̶n̶  ° -🚻』
    →: O que é "Check In"?

          Para alguns que já leram o sistema /check in, sabem muito bem o que isso é. Para quem não conhece, dê uma lida, basta usar o comando /check in no off. Sem mais delongas, abaixo está a atualização dos Check In, com id, nome e os pontos dos determinados player (players com 0 de check in não aparecem):

{select('select id_player, check_in, nome from player where check_in <> 0 order by check_in desc')}'''
    print(sistema_check_in)
    copiar(sistema_check_in)
    return

def sistema_patentes(): # função parar mostrar junto ao sistema a patente de cada peronagem
    sistema_patentes = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ P̶a̶t̶e̶n̶t̶e̶s̶ ° -🚻』
    →: O que é "Patente"?

          Cada personagem evolui de acordo com o seu esforço, as vezes por sorte... A patente não define o quão forte você é. Veja abaixou os personagems e suas patentes (se alguma estiver errada, tratar com os adms para futura atualização):
{select('select pp.id_pp, pp.nome, p.nome as patente from pp, patente p where pp.id_patente = p.id_patente order by pp.id_pp asc')}          
'''
    print(sistema_patentes)
    copiar(sistema_patentes)
    return

def sistema_elementos(): # função parar mostrar junto ao sistema o elkemento de cada peronagem
        sistema_elementos = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ E̶l̶e̶m̶e̶n̶t̶o̶s̶ ° -🚻』
    →: O que é "Elemento"?

          Assim como no anime, os elementos simplesmente é a transformação da natureza que seu personagem domina. A cada patente ganha-se 1 novo elemento (contabilizado apenas de chunnin para frente. Virar gennin não dá um elemento novo.) Veja abaixou os personagems e seus elementos (se algum estiver errado, tratar com os adms para futura atualização):
{select('select pp.id_pp, pp.nome, e1.nome as elemento_1, e2.nome as e_2, e3.nome e_3, e4.nome e_4, e5.nome e_5 from pp inner join elemento as e1 on pp.id_elemento_1 = e1.id_elemento inner join elemento as e2 on pp.id_elemento_2 = e2.id_elemento inner join elemento as e3 on pp.id_elemento_3 = e3.id_elemento inner join elemento as e4 on pp.id_elemento_4 = e4.id_elemento inner join elemento as e5 on pp.id_elemento_5 = e5.id_elemento order by pp.id_pp asc')}          
'''
        print(sistema_elementos)
        copiar(sistema_elementos)
        return

def ficha():
    ficha = print('''
''')
    
    try:
        copiar = int(input('\nDeseja copiar para área de transferência? "1" para sim e qualquer tecla para não\nR: '))
        if copiar == 1:
            pyperclip.copy(ficha)
            print('\nCopiado com sucesso!')
        
        else:
            pass
        
    except ValueError:
        pass


'''『✅- ° } C̶h̶e̶c̶k̶ I̶n̶ { ° -✅』

● ━━━━━━━
       *→: Abordagem*
╘ É uma variação dos prêmios, que assim como, recompensa o player por um determinado esforço. Dessa vez, os players são recompensados por serem ons e interagir com o rpg em um todo.

● ━━━━━━━
       *→: Funcionamento*
╘ Sendo um bônus para incentivar os players de serem on, participar dos eventos em pretensão de só vencer, deixar de fazer algo porque acha que é perda de tempo, o Check In tentará mudar isso. Tudo que seja relacionado com o RPG gera uma bonificação. Com os pontos em Check In, pode-se acumular iguais os prêmios e uma determinada quantia de Check In dá uma quantia de pontos e o Player pode até alcançar um prêmio de Nível Super Bom, apenas sendo on no RPG. Cada coisa ou evento lhe dá uma quantia de pontos diferente, que irá definir. Veja abaixo: 

*Base:* 
5 linhas = 0.25
10 linhas = 0.5
50 linhas = 2.5 ponto
100 linhas = 5 pontos
500 linhas = 25 pontos
*Eventos*
*Participar de qualquer tipo de evento* = 1 pontos. Participar, é ao menos tentar jogar. Entrar no evento e não fazer nada, não lhe dará pontos de Check In. Sua colocação no evento pouco importa.

*Evolução*
*Passar na Academia* = 1 ponto.
*Ser graduado (Missão/Exame)* = 2 pontos. 
        Qualquer tipo de Up, ganhado de qualquer forma (sem ser evento) dará ao player os devidos pontos.
*Participar de uma missão narrada* = 1 ponto.
*Uma missão narrada bem sucedida* = 2 pontos. 
        Válido para qualquer tipo de missão narrada.

*Ganhar um x1* 
*Sem morte* = 1 ponto. 
*Com Morte* = 10 pontos. 
        Válido apenas se for x1 contra players. Ataques à um grandioso número de NPC também conta. Ex: invadir uma vila, pegar uma invocação em ON, pegar uma arma em ON, uma bijuu, por exemplo.

*Completar o treino de um Jutsu criado ou Treinar jutsus por Linhas*
*Rank D* = 0.25 ponto
*Rank C* = 0.3 pontos
*Rank B* = 1.25 pontos
*Rank A* = 2.5 pontos
*Rank S* = 3.75 pontos

*Completar treinos e evoluções de suas técnicas* 
*Doujutsu LV 1* = 0.4 pontos
*Doujutsu LV 2* = 0.5 pontos
*Doujutsu LV 3* = 1 ponto
*Doujutsu Especial LV1* (Ex> Mangekyou) = 140 pontos
*Doujutsu Especial LV 2* (Ex> Mangekyou Eterno, Tenseigan, Rinnegan e outros) = 280 pontos

*Susanoo / Treinos Jinchuuriki* = 2 pontos (Todos os treinos)

*Senninka* = 5 pontos 
        Treino completo.
*Gama Sennin* = 26.25
        Imperfeito.
*Gama Sennin / Hebi Sennin / Byakugou* = 47.75 pontos
        Completo.

*Treino Completo 1° portão* = 5 ponto
*Treino Completo 2° portão* = 7.5 pontos
*Treino Completo 3° portão / 1° ativação do Shinchi Tenkohou* = 10 pontos
*Treino Completo 4° portão /2° ativação do Shinchi Tenkohou* = 12.5 pontos
*Treino Completo 5°portão / 3° ativação do Shinchi Tenkohou* = 15 pontos
*Treino Completo 6° portão* = 17.5 pontos
*Treino Completo 7° portão* = 20.5 pontos
*Treino Completo 8° portão* = 23 pontos

*Karma lv 1* = 10 pontos
        Completo.
*Karma lv 2* = 12.5 pontos
        Completo.
*Karma lv 3* = 16.25 pontos
        Completo (luta contra Otsutsuki conta).

*° A̶d̶m̶i̶n̶i̶s̶t̶r̶a̶ç̶ã̶o̶:̶ S̶u̶p̶e̶r̶v̶i̶s̶o̶r̶e̶s̶ e̶ P̶l̶a̶y̶e̶r̶s̶ (̶A̶n̶a̶r̶q̶u̶i̶a̶)̶ °*

*Narração sem pretenção de batalha* = 5 pontos
*Narração com pretenção de batalha* = 5 pontos
        *Caso ganhe* = 10 pontos
*Narrar missões* = 10 pontos
        *Caso ganhe* = 15 pontos
                A narração é geral: pega desde o momento que o NPC passa a missão (caso não tenha kage ou representante player), até o momento final das missões. Caso tenha viagem e o player caia contra players de viagem, esse narrador deve também fazer a narração desses.

*Aprovar Fichas e Repcionar* = 0.5 pontos
        Só será contabilizado se o aprovador por seu nick e/ou ID na área "Notas adm:"
        Tais fichas devem ser mandadas no grupo N'RPG • DB Revolution (grupo na descrição do avisos)
*Aprovar Cenas / Treinos de Jutsu* = 0.25 pontos
        Só será contabilizado se o relatório for mandando no grupo N'RPG • DB Revolution (grupo na descrição do avisos)

*Manter as coisas em ordem* = 0.25 pontos
        Falar players que saíram, trocaram de aparência, etc.
        Só será contabilizado se o relatório for mandando no grupo N'RPG • DB Revolution (grupo na descrição do avisos)

*Dar ideias e criar evento* = será avaliado de acordo com o evento
*Tutelar eventos* = será avaliado de acordo com o evento

*Divulgar prêmios e semelhantes* = 1 ponto
*Ajudar na resolução de algum problema* = será avaliado de acordo com a situação
        Decidir prêmios, por exemplo


*Correção/Criação de Dicionário* = 0.3 por jutsu

*Recrutar Players* = 3 pontos
        *Player Recrutado é On* = 7 pontos
*Criação Missões Narrada* = 5 pontos

*Consertar Sistemas Errados* = depende do erro

Coisas ganhas em eventos não contam para NADA!

*Perdas de Check In:*
Atrasar cenas (players) = -1 ponto 
        Perda contínua. Se na mesma história o player atrasar, as perdas vão aumentando de 1 em 1
Atrasar cenas (narradores)= -2 pontos
        Perda contínua. Se na mesma história o narrador atrasar, as perdas vão aumentando de 2 em 2
*Apagar personagens ou matar-los atoa* = - 5 pontos
        Salvo players novos que entraram recentemente e talvez não estavam tão ligados nas estratégias de criações

● ━━━━━━━
       *→: Detalhes*
╘ Os prêmios são vitalícios, isso significa que mesmo que você troque, perca, mude de personagem, você ainda terá seus pontos de Check In. Você pode resgatar seus pontos se eles já atingirem o nível de um prêmio, seja pra juntar-lo com outros prêmios que tenha, seja porque necessita para ficar mais forte. Veja abaixo a tabela de pontos do Check In *(sujeita à mudanças, caso esteja fácil demais ou difícil demais de ganhar prêmio. Estejam cientes disso!)*

╘ *Nível Ruim* = 35 Pontos de Check In
╘ *Nível Médio* = 70 Pontos de Check In
╘ *Nível Bom* = 140 Pontos de Check In
╘ *Nível Super Bom* = 280 Pontos de Check In 

● ━━━━━━━

🦉 Satori:  N/A
🐍 Reibi: M/A
🐿️ Shukaku: 
🐈‍⬛ Matatabi: N/A
🐢 Isobu: N/A
🦧 Son Goku: N/A 
🐎 Kokuō: N/A
🐌 Saiken: N/A
🦋 Chōmei: N/A
🐙 Gyūki: N/A
🦊⚫ Kurama Ying: N/A
🦊⚪ Kurama Yang: N/A

_🌳Ashura🌀 : Juuzou_
_♦️Indra♦️ :_ Patry
_▫️Hamura▫:_
_🦯Urashiki🦯: Basaran_
_❌Kinshiki❌: Sakon_

🕸️Líderes de Clã:🕸️

Uchiha: Patry'''
