#######################################################################
""" 
query.py é o módulo principal após o main (NRPG-DataManager.py) Sendo ele
quem ficará em looping para saber as ações que o usuário deseja fazer, até
não haver mais coisas a mexer.
De acordo com os pedidos do player, o query.py irá chamar outros módulos
que farão o desejado.
"""
#######################################################################

import sys

# sistemas do rpg #
from sistemas_rpg.invo import *
from sistemas_rpg.base import *
from sistemas_rpg.ficha import *
from sistemas_rpg.cla import *
from sistemas_rpg.invo import *
from sistemas_rpg.tres_fatorial import *
from modulos.sistemas import *
from modulos.info import *

# modulos do programa #
from modulos.utils import *
from modulos.adder import *
from modulos.updater import *
from modulos.remover import *


# função inicial. Responsável por saber o primeiro interesse do usuário, seja adicionar
# remover, buscar ou atualizar informações
def query():
    confirmacao = False 
    while confirmacao == False:
        try:
            query = int(input(f'''
----- ----- >> Sistema << ------ -----
    "0" para fechar o Programa

----- ------ >> Adições << ------ -----
    "1" para opções de Adições

----- ------ >> Remoções << ------ -----
    "2" para opções de Remoções

---- ---- >> Atualizações << ---- ----
    "3" para opções de Atualizações

------ ------ >> Buscas << ------ ------
    "4" para opções de Buscas (EM DESENVOLVIMENTO)

R: '''))

            if query == 0:
                # encerra o programa.
                sys.exit('\nConexão encerrada!')

            elif query == 1:
                confirmacao = True
                #chama o módulo responsável pelas adições
                query_adicoes()

            elif query == 2:
                confirmacao = True
                #chama o módulo responsável pelas remoções
                query_remocoes()  

            elif query == 3:
                confirmacao = True
                #chama o módulo responsável pelas atualizações
                query_atualizacoes()    

            elif query == 4:
                confirmacao = True
                # chama o módulo responsável pelas atualizações
                query_buscas()

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return query


# Aprofundamento da aba de adições. Responsável por saber o real interesse do usuário em adições
# add um novo player, um usuário para arma, etc
def query_adicoes():
    confirmacao = False 
    while confirmacao == False:
        try:
            query_adicoes = int(input('''
----- ------ >> Adições << ------ -----
        
        ["0" para voltar]

NPCS e ITENS:
        "1" para adicionar <um> Usuário (arma)
        "2" para adicionar <um> Jinchuriki (bijuu)
        "3" para adicionar <um> Invocador (invo)
        "4" para adicionar <uma> Reencarnação (reen)

PLAYERS E PERSONAGENS:
        "4" para adicionar <um> novo Player
        "5" para adicionar <um> novo Personagem

PONTOS E SISTEMA:
        "6" para adicionar pontos de Check In

R: '''))
            if query_adicoes == 0:
                confirmacao = True
                query()

            elif query_adicoes == 1:
                confirmacao = True
                add_arma()

            elif query_adicoes == 2:
                confirmacao = True
                add_bijuu()

            elif query_adicoes == 3:
                confirmacao = True
                add_invo()

            elif query_adicoes == 4:
                confirmacao = True
                add_player()

            elif query_adicoes == 5:
                confirmacao = True
                add_pp()
                    
            elif query_adicoes == 6:
                confirmacao = True
                add_check_in()
                        
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return


# Aprofundamento da aba de remoções. Responsável por saber o real interesse do usuário em remover
# um novo player, um usuário para arma, etc
def query_remocoes():
    confirmacao = False 
    while confirmacao == False:
        
        try: 
            query_remocoes = int(input('''
----- ------ >> Remoções << ------ -----
        
        ["0" para voltar]
    
PLAYERS E PERSONAGENS
        "1" para remoção <de um> Player
        "2" para remoção <de um> Personagem

NPCS E ITENS
        "3" para remoção <em> Arma
        "4" para remoção <em> Invocação
        "5" para remoção <em> Bijuus

R: '''))
            if query_remocoes == 0:
                confirmacao = True
                query()

            elif query_remocoes == 1:
                confirmacao = True
                remover_player()
            
            elif query_remocoes == 2:
                confirmacao = True
                remover_pp()

            elif query_remocoes == 3:
                confirmacao = True
                query_remocoes_arma()

            elif query_remocoes == 4:
                confirmacao = True
                query_remocoes_invo()

            elif query_remocoes == 5:
                confirmacao = True
                query_remocoes_bijuu()
            
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return


# Aprofundamento da aba de remoções EM arma. Responsável por saber o real interesse do usuário em remover dentro de uma arma
# um remover a arma em si, um usuário da arma, etc.
def query_remocoes_arma():
    confirmacao = False 
    while confirmacao == False:

        try:
            query_remocoes_arma = int(input('''
----- ------ >> Remoções << ------ -----

        ["0" para voltar]                                
        
        Arma:
            "1" para remover <um> Usuário
            "2" para remover <uma> Arma

R: '''))
            if query_remocoes_arma == 0:
                confirmacao = True
                query_remocoes() 
            
            elif query_remocoes_arma == 1:
                confirmacao = True
                remover_player_arma()

            elif query_remocoes_arma == 1:
                confirmacao = True
                remover_arma()

            else:
                print('\nO valor não corresponde. Tente novamente')
        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return

# Aprofundamento da aba de remoções EM invocações. Responsável por saber o real interesse do usuário em remover dentro de uma invo
# um remover a invocação em si, um usuário da invocação, etc.
def query_remocoes_invo():
    confirmacao = False 
    while confirmacao == False:

        try:
            query_remocoes_invo = int(input('''
----- ------ >> Remoções << ------ -----

        ["0" para voltar]                                
        
        Invocação:
            "1" para remover <um> Usuário
            "2" para remover <uma> Invocação

R: '''))
            if query_remocoes_invo == 0:
                confirmacao = True
                query_remocoes() 
            
            elif query_remocoes_invo == 1:
                confirmacao = True
                remover_player_invo()

            elif query_remocoes_invo == 1:
                confirmacao = True
                remover_invo()

            else:
                print('\nO valor não corresponde. Tente novamente')
        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return

# Aprofundamento da aba de remoções EM bijuu. Responsável por saber o real interesse do usuário em remover dentro de uma bijuu
# um remover a bijuu em si, um jinchuuriki da bijuu, etc.
def query_remocoes_bijuu():
    confirmacao = False 
    while confirmacao == False:

        try:
            query_remocoes_bijuu = int(input('''
----- ------ >> Remoções << ------ -----

        ["0" para voltar]                                
        
        Bijuu:
            "1" para remover <um> Jinchuuriki
            "2" para remover <uma> Bijuu

R: '''))
            if query_remocoes_bijuu == 0:
                confirmacao = True
                query_remocoes() 
            
            elif query_remocoes_bijuu == 1:
                confirmacao = True
                remover_player_bijuu()

            elif query_remocoes_bijuu == 1:
                confirmacao = True
                remover_bijuu()

            else:
                print('\nO valor não corresponde. Tente novamente')
        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return


# Aprofundamento da aba de atualizações. Responsável por saber o real interesse do usuário em buscar atualizações
def query_atualizacoes():
    confirmacao = False 
    while confirmacao == False:  
            
        try:
            query_atualizacoes = int(input('''
    ---- ---- >> Atualizações << ---- ----
            
            ["0" para voltar]

            "1" para atualizações em Player
            "2" para atualizações em Personagens
            "3" para atualizações em NPC's
R: '''))

            if query_atualizacoes == 0:
                confirmacao = True
                query()

            elif query_atualizacoes == 1:
                confirmacao = True
                query_atualizacoes_player()

            elif query_atualizacoes == 2:
                confirmacao = True
                query_atualizacoes_pp()

            elif query_atualizacoes == 3:
                confirmacao = True
                query_atualizacoes_npc()
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
            
    return


# Aprofundamento da aba de atualização em PLAYER. Responsável por saber o real interesse do usuário buscar atualização em player
def query_atualizacoes_player():
    confirmacao = False 
    while confirmacao == False:  
        try:
            query_atualizacoes_player = int(input('''
    ---- ---- >> Atualizações << ---- ----
        
        ["0" para voltar]
        
        Players:
            "1" para mostrar os Check In
R: '''))
            if query_atualizacoes_player == 0:
                confirmacao = True
                query_atualizacoes()
            elif query_atualizacoes_player == 1:
                confirmacao = True
                sistema_check_in()
                
        except:
               print('\nO valor não corresponde. Tente novamente')     
    return


# Aprofundamento da aba de atualização em PERSONAGEM. Responsável por saber o real interesse do usuário buscar atualização em PP
def query_atualizacoes_pp():
    confirmacao = False 
    while confirmacao == False:  
        try:
            query_atualizacoes_pp = int(input('''
    ---- ---- >> Atualizações << ---- ----
        
        ["0" para voltar]
        
        Personagem:

PARA CRIAÇÂO DE PERSONAGENS:
            "1" para mostrar os Nomes
            "2" para mostrar as Aparências
            "3" para mostrar o Sistema 3!
            "4" para mostrar as Bases
            "5" para mostrar os Clãs
            "6" para mostrar a Ficha de Criação

            "7" para mostrar todos acima

PARA ORGANIZAÇÂO EM GERAL:
            "8" para mostrar as Patentes
            "9" para mostrar os Elementos

            "10" para mostrar os Elementos e Patentes
R: '''))
            if query_atualizacoes_pp == 0:
                confirmacao = True
                query_atualizacoes()

            elif query_atualizacoes_pp == 1: # Digite 1 para mostrar os Nomes ocupados;
                sistema_nome()

            elif query_atualizacoes_pp == 2: # Digite 2 para mostrar as Aparências ocupadas;
                sistema_aparencia()

            elif query_atualizacoes_pp == 3: # mostrar o sistema 3!
                print(tres_fatorial)
                copiar(tres_fatorial)

            elif query_atualizacoes_pp == 4: # mostrar as Bases
                sistema_base()

            elif query_atualizacoes_pp == 5: # mostrar os Clãs ocupados;             
                sistema_cla()

            elif query_atualizacoes_pp == 6: # mostrar a Ficha de Criação.
                print(ficha)
                copiar(ficha)

            elif query_atualizacoes_pp == 7:  #para mostrar todos  
                
                sistema_nome()
                
                sistema_aparencia()

                sistema_aparencia()

                print(tres_fatorial)
                copiar(tres_fatorial)

                sistema_base()
                
                sistema_cla()

                print(ficha)
                copiar(ficha)

            elif query_atualizacoes_pp == 8: # para mostrar as Patentes
                sistema_patentes()
            
            elif query_atualizacoes_pp == 9: # mostrar os Elementos
                sistema_elementos()

            elif query_atualizacoes_pp == 10: # para mostrar as Patentes e Elementos Juntos
                sistema_patentes()

                sistema_elementos()         
        

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
              
    return



def query_atualizacoes_npc():
    confirmacao = False 
    while confirmacao == False:  
        try:
            query_atualizacoes_npc = int(input('''
    ---- ---- >> Atualizações << ---- ----
        
        ["0" para voltar]
        
        NPC's:
            "1" para mostrar as Armas
            "2" para mostrar as invos

R: '''))
            if query_atualizacoes_npc == 0: # para voltar
                confirmacao = True
                query_atualizacoes()

            elif query_atualizacoes_npc == 1: # para mostrar as Armas
                print('oi')

            elif query_atualizacoes_npc == 2: # para mostrar as invos
                print(sistema_invo)
                copiar(sistema_invo)

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')



def query_buscas():
    confirmacao = False
    while confirmacao == False:
        try:
            query_buscas = int(input('''
------ ------ >> Buscas << ------ ------
            
        ["0" para voltar]

        "1" para buscas em Players
        "2" para buscas em Personagens
        "3" para buscas em Armas
        "4" para buscas em Invocações   

R:'''))
            if query_buscas == 0:
                confirmacao = True
                query()

            elif query_buscas == 1:
                confirmacao = True
                query_buscas_player()

            elif query_buscas == 2:
                confirmacao = True
            
            elif query_buscas == 3:
                confirmacao = True
            
            elif query_buscas == 4:
                confirmacao = True
            
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return



def query_buscas_player():
    confirmacao = False
    while confirmacao == False:
        
        try:
            query_buscas_player = int(input('''
------ ------ >> Buscas << ------ ------
            
        ["0" para voltar]

        Players:
            "1" busca por ID
            "2" busca por Nome
            "3" busca por Número
            "4" busca por Recrutador
            "5" busca por Check_In

R:'''))
            if query_buscas_player == 0:
                confirmacao = True
                query_buscas()

            elif query_buscas_player == 1:
                confirmacao = True

            elif query_buscas_player == 2:
                confirmacao = True

            elif query_buscas_player == 3:
                confirmacao = True
                
            elif query_buscas_player == 4:
                confirmacao = True

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')



def query_buscas_pp():
    confirmacao = False
    while confirmacao == False:
        
        try:
            query_buscas_pp = int(input('''
------ ------ >> Buscas << ------ ------
            
        ["0" para voltar]

        Personagens:
            "1" busca por ID
            "2" busca por Nome
            "3" busca por Base
            "5" busca por 
            "6" busca por Dono
R:'''))

            if query_buscas_pp == 0:
                confirmacao = True
                query_buscas()

            elif query_buscas_pp == 1:
                confirmacao = True

            elif query_buscas_pp == 2:
                confirmacao = True

            elif query_buscas_pp == 3:
                confirmacao = True
                
            elif query_buscas_pp == 4:
                confirmacao = True

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return