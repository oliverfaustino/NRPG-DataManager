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
from sistemas_rpg.ficha import *
from sistemas_rpg.id import *
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
        "5" para adicionar <um> novo Player
        "6" para adicionar <um> novo Personagem

PONTOS E SISTEMA:
        "7" para adicionar pontos de Check In
        "8" para adicionar pontos de Missão

R: '''))
            if query_adicoes == 0:
                confirmacao = True
                query()

            elif query_adicoes == 1:
                add_arma()

            elif query_adicoes == 2:
                add_bijuu()

            elif query_adicoes == 3:
                add_invo()

            elif query_adicoes == 4:
                add_reen()

            elif query_adicoes == 5:
                add_player()

            elif query_adicoes == 6:
                add_pp()
                    
            elif query_adicoes == 7:
                add_check_in()
                
            elif query_adicoes == 8:
                add_pontos_missao()
                        
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
    Player:
        "1" para remoção <de um> Player

    Personagem
        "2" para remoção <de um> Personagem

NPCS E ITENS:
    Armas:
        "3" para remover <uma> usuário (arma)           
        
    Bijuu:
        "4" para remover <um> Jinchuuriki

    Reencarnação:
        "5" para remover <um> Reencarnado
        "6" para remover <uma> Reencarnação


R: '''))
            if query_remocoes == 0:
                confirmacao = True
                query()

            elif query_remocoes == 1:
                remover_player()
            
            elif query_remocoes == 2:
                remover_pp()

            elif query_remocoes == 3:
                remover_usuario()

            elif query_remocoes == 4:
                remover_jinchuriki()

            elif query_remocoes == 5:
                remover_reen()

            elif query_remocoes == 6:
                remover_reen()
            
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
PLAYERS E PERSONAGENS
    Player:
        "1" para atualização <de> Check In
        "2" para mostrar os Recrutas e Recrutador

    Personagem: (PARA CRIAÇÂO)
        "3 para mostrar os Nomes
        "4" para mostrar as Aparências
        "5" para mostrar o Sistema 3!
        "6" para mostrar as Bases
        "7" para mostrar os Clãs
        "8" para mostrar a Ficha de Criação

        "9" para mostrar todos acima (Personagem)

    Personagem: (PARA ORGANIZAÇÃO)
        "10" para mostrar as Patentes
        "11" para mostrar o sistema de Id

        "12" para mostrar os Check In, ID e Patentes

NPCS E ITENS:
    NPC's:
        "13" para mostrar as Armas
        "14" para mostrar as invos
        "15" para mostrar as Bijuu
        "16" para mostrar as Reencarnações

        "17" para mostrar todos acima (NPC's)
        "18" para mostrar todos acima (NPC's e Personagem)

R: '''))

            if query_atualizacoes == 0:
                confirmacao = True
                query()

            elif query_atualizacoes == 1:
                sistema_check_in()

            elif query_atualizacoes == 2: # Digite 1 para mostrar os Recrutas e Recrutador;
                sistema_recrutamento()

            elif query_atualizacoes == 3: # Digite 1 para mostrar os Nomes ocupados;
                sistema_nome()

            elif query_atualizacoes == 4: # Digite 2 para mostrar as Aparências ocupadas;
                sistema_aparencia()

            elif query_atualizacoes == 5: # mostrar o sistema 3!
                print(tres_fatorial)
                copiar(tres_fatorial)

            elif query_atualizacoes == 6: # mostrar as Bases
                sistema_base()

            elif query_atualizacoes == 7: # mostrar os Clãs ocupados;             
                sistema_cla()

            elif query_atualizacoes == 8: # mostrar a Ficha de Criação.
                print(ficha)
                copiar(ficha)

            elif query_atualizacoes == 9:  #para mostrar todos   
                sistema_nome()
                sistema_aparencia()
                
                print(tres_fatorial)
                copiar(tres_fatorial)
                
                sistema_base()
                sistema_cla()
                
                print(ficha)
                copiar(ficha)

            elif query_atualizacoes == 10: # para mostrar as Patentes
                sistema_patentes()
            
            elif query_atualizacoes == 11: # mostrar os Check In
                print(id)
                copiar(id)

            elif query_atualizacoes == 12: # para mostrar as Patentes e Elementos Juntos
                sistema_patentes()
                sistema_check_in()  
                print(id)
                copiar(id)

            elif query_atualizacoes == 13: # para mostrar as Armas
                sistema_arma()

            elif query_atualizacoes == 14: # para mostrar as invos
                sistema_invo()

            elif query_atualizacoes == 15: # para mostrar as Bijuus
                sistema_bijuu()

            elif query_atualizacoes == 16: # para mostrar as Reencarnações
                sistema_reen()

            elif query_atualizacoes == 17: # para mostrar as COISAS DE NPCS
                sistema_arma()
                sistema_invo()
                sistema_bijuu()
                sistema_reen()

            elif query_atualizacoes == 18: # para mostrar as NPCS E PERSONAGENS
                sistema_arma()
                sistema_invo()
                sistema_patentes()
                sistema_check_in()  
                print(id)
                copiar(id)

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
            
    return



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