import sys
import pyperclip

# sistemas do rpg #
from sistemas_rpg.sistema_invo import *
from sistemas_rpg.sistema_base import *
from sistemas_rpg.sistema_ficha import *
from sistemas_rpg.sistema_cla import *
# modulos do programa #
from modulos.select import *
from modulos.commit import *
from modulos.updater import *

tempo = datetime.now()

#imput sobre query
def query_():
    """'''\n----- ----- >> Sistema << ------ -----
    
    Digite 0 para  o programa.'''

'''---- ---- >> Atualizações << ---- ----
    Personagem:
        Digite 1 para mostrar os Nomes ocupados;
        Digite 2 para mostrar as Aparências ocupadas;
        Digite 3 para mostrar os Registros ninja ocupados;       
        Digite 4 para mostrar as Bases ocupadas;
        Digite 5 para mostrar os Clãs ocupados;
        Digite 6 para mostrar a Ficha de Criação.

    Itens/NPC:
        Digite 7 para mostrar as Invocações ocupadas * em desenvolvimento * ;
        Digite 8 para mostrar as Armas ocupadas * em desenvolvimento * .'''

'''----- ------ >> Adições << ------ -----
    Digite 8 para fazer um INSERTO INTO arma * em desenvolvimento * ;
    Digite 9 para fazer um INSERT INTO invo * em desenvolvimento * ;
    Digite 10 para adicionar um novo player;
    Digite 11 para adicionar um novo personagem.'''

'''----- ------ >> Remoções << ------ -----
    Digite 12 para retirar um Player (irá tirar todas as relações do Player);
    Digite 13 para retirar um Personagem (irá tirar todas as relações do Player);
'''"""
    analise_operacao = False 
    while analise_operacao == False:
        try:
            query = int(input(f'''\n----- ----- >> Sistema << ------ -----
    
    "0" para fechar o programa

----- ------ >> Adições << ------ -----
    "1" para opções de adições

----- ------ >> Remoções << ------ -----
    "2" para opções de remoção

---- ---- >> Atualizações << ---- ----
    "3" para opções de atualizações

R: '''))
            analise_operacao = True
        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return query

def query_chose():
    analise = False 
    while analise == False:
        query = query_()

        if query == 0:
            sys.exit('\nConexão encerrada!')

        elif query == 1:
            analise = False
            analise_adicoes = False
            while analise_adicoes == False:

                try: # try que formulará as query sobre as adições de informações
                    query_adicoes = int(input('''
----- ------ >> Adições << ------ -----
        
        [Digite 0 para voltar]

        "1" para fazer um INSERTO INTO arma * em desenvolvimento * ;
        "2" para fazer um INSERT INTO invo * em desenvolvimento * ;
        "3" para adicionar um novo player;
        "4" para adicionar um novo personagem.

R: '''))
                    if query_adicoes == 0:
                        analise_adicoes = True
                        query_chose()

                    elif query_adicoes == 1:
                        analise_adicoes = True
                        commit_arma()

                    elif query_adicoes == 2:
                        analise_adicoes = True
                        commit_invo()

                    elif query_adicoes == 3:
                        analise_adicoes = True
                        commit_player()

                    elif query_adicoes == 4:
                        analise_adicoes = True
                        commit_pp()
                    
                    else:
                        print('\nO valor não corresponde. Tente novamente')

                except ValueError:
                        print('\nO valor não corresponde. Tente novamente')
        
        elif query == 3:
            analise = False
            analise_atualizacoes = False
            while analise_atualizacoes == False:   
            
                try:  # try que formulará as query sobre as atualizações de informações
                    query_atualizacoes = int(input('''
    ---- ---- >> Atualizações << ---- ----
            
            ["0" para voltar]

            "1" atualizações em Player
            "2" atualizações em Personagens

R: '''))

                    if query_atualizacoes == 0:
                        analise_atualizacoes = True
                        query_chose()

                    elif query_atualizacoes == 1:
                        analise_atualizacoes = True
                        print('oi 1')
                        #query_atualizacoes_player

                    elif query_atualizacoes == 2:
                        analise = True
                        analise_atualizacoes = True
                        analise_atualizacoes_pp = False

                        while analise_atualizacoes_pp == False:
                            query_atualizacoes_pp = int(input('''
    ---- ---- >> Atualizações << ---- ----
        
        Personagem:
            "1" para mostrar os Nomes
            "2" para mostrar as Aparências
            "3" para mostrar os Registros Ninja      
            "4" para mostrar as Bases
            "5" para mostrar os Clãs
            "6" para mostrar a Ficha de Criação

R: '''))
                            if query_atualizacoes_pp == 0:
                                analise_atualizacoes_pp = True
                                query_chose()

                            elif query_atualizacoes_pp == 1: # Digite 1 para mostrar os Nomes ocupados;
                                analise_atualizacoes_pp = True
                                select('select nome FROM pp ORDER BY nome ASC;')

                            elif query_atualizacoes_pp == 2: # Digite 2 para mostrar as Aparências ocupadas;
                                analise_atualizacoes_pp = True
                                select('select aparencia FROM pp ORDER BY aparencia ASC;')

                            elif query_atualizacoes_pp == 3: # Digite 3 para mostrar os Registros ninja ocupados; 
                                analise_atualizacoes_pp = True
                                select('select registro_ninja from pp order by registro_ninja asc')

                            elif query_atualizacoes_pp == 4: # "4" para mostrar as Bases
                                analise_atualizacoes_pp = True
                                
                                print(sistema_base)
                                try:
                                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não\n\nR: '))
                                    
                                    if copiar == 1:
                                        pyperclip.copy(sistema_base)
                                        print('\nCopiado com sucesso!')
                        
                                    else:
                                        pass
                        
                                except ValueError:
                                    pass

                            elif query_atualizacoes_pp == 5: # Digite 5 para mostrar os Clãs ocupados;
                                analise_atualizacoes_pp = True
                                
                                print(sistema_cla)
                                try:
                                    copiar = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não\n\nR: '))
                                    if copiar == 1:
                                        pyperclip.copy(sistema_cla)
                                        print('''\nCopiado com sucesso!''')
                        
                                    else:
                                        print("")
                        
                                except ValueError:
                                    print("")
                            
                            elif query_atualizacoes_pp == 6: # Digite 6 para mostrar a Ficha de Criação.
                                analise_atualizacoes_pp = True
                                print(sistema_ficha)
                            else:
                                print('\nO valor não corresponde. Tente novamente')
                        
                    else:
                        print('\nO valor não corresponde. Tente novamente')

                except ValueError:
                    print('\nO valor não corresponde. Tente novamente')

        else:
            print('\nO valor não corresponde. Tente novamente')
              
    return