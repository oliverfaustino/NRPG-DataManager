import sys

# sistemas do rpg #
from sistemas_rpg.sistema_invo import *
from sistemas_rpg.sistema_base import *
from sistemas_rpg.sistema_ficha import *
from sistemas_rpg.sistema_cla import *
from modulos.info import *

# modulos do programa #
from modulos.utils import *
from modulos.adder import *
from modulos.updater import *

def query():
    confirmacao = False 
    while confirmacao == False:
        try:
            query = int(input(f'''
----- ----- >> Sistema << ------ -----

    "0" para fechar o programa

----- ------ >> Adições << ------ -----
    "1" para opções de adições

----- ------ >> Remoções << ------ -----
    "2" para opções de remoção

---- ---- >> Atualizações << ---- ----
    "3" para opções de atualizações

------ ------ >> Buscas << ------ ------
    "4" para opções de buscas

R: '''))

            if query == 0:
                sys.exit('\nConexão encerrada!')

            elif query == 1:
                confirmacao = True
                query_adicoes()

            elif query == 2:
                confirmacao = True
                query_remocoes()  

            elif query == 3:
                confirmacao = True
                query_atualizacoes()    

            elif query == 4:
                confirmacao = True
                query_buscas()

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return query



def query_adicoes():
    confirmacao = False 
    while confirmacao == False:

        try: # try que formulará as query sobre as adições de informações
            query_adicoes = int(input('''
----- ------ >> Adições << ------ -----
        
        ["0" para voltar]

        "1" para fazer um INSERTO INTO arma * em desenvolvimento * ;
        "2" para fazer um INSERT INTO invo * em desenvolvimento * ;
        "3" para adicionar um novo Player
        "4" para adicionar um novo Personagem
        "5" para adicionar pontos de Check In

R: '''))
            if query_adicoes == 0:
                confirmacao = True
                query()

            elif query_adicoes == 1:
                confirmacao = True
                add_arma()

            elif query_adicoes == 2:
                confirmacao = True
                add_invo()

            elif query_adicoes == 3:
                confirmacao = True
                add_player()

            elif query_adicoes == 4:
                confirmacao = True
                add_pp()
                    
            elif query_adicoes == 5:
                confirmacao = True
                update_check_in()
                        
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return



def query_remocoes():
    confirmacao = False 
    while confirmacao == False:
        
        try: # try que formulará as query sobre as atualizações de informações
            query_remocoes = int(input('''
----- ------ >> Remoções << ------ -----
        
        ["0" para voltar]
    
        "1" para remoção em Player
        "2" para remoção em Personagem
        "3" para remoção em Armas
        "4" para remoção em Invocações

R: '''))
            if query_remocoes == 0:
                confirmacao = True
                query()
            elif query_remocoes == 1:
                confirmacao = True
                query_remocoes_player()
            
            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return



def query_remocoes_player():
    confirmacao = False 
    while confirmacao == False:

        try:
            query_remocoes_player = int(input('''
----- ------ >> Remoções << ------ -----
        
        ["0" para voltar]                                

R: '''))
            if query_remocoes_player == 0:
                confirmacao = True
                query_remocoes() 

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
    return



def query_atualizacoes():
    confirmacao = False 
    while confirmacao == False:  
            
        try:  # try que formulará as query sobre as atualizações de informações
            query_atualizacoes = int(input('''
    ---- ---- >> Atualizações << ---- ----
            
            ["0" para voltar]

            "1" para atualizações em Player
            "2" para atualizações em Personagens

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

            else:
                print('\nO valor não corresponde. Tente novamente')

        except ValueError:
            print('\nO valor não corresponde. Tente novamente')
            
    return



def query_atualizacoes_player():
    return



def query_atualizacoes_pp():
    confirmacao = False 
    while confirmacao == False:  
        try:
            query_atualizacoes_pp = int(input('''
    ---- ---- >> Atualizações << ---- ----
        
        ["0" para voltar]
        
        Personagem:
            "1" para mostrar os Nomes
            "2" para mostrar as Aparências
            "3" para mostrar os Registros Ninja      
            "4" para mostrar as Bases
            "5" para mostrar os Clãs
            "6" para mostrar a Ficha de Criação

R: '''))
            if query_atualizacoes_pp == 0:
                confirmacao = True
                query_atualizacoes()

            elif query_atualizacoes_pp == 1: # Digite 1 para mostrar os Nomes ocupados;
                confirmacao = True
                select('select nome FROM pp ORDER BY nome ASC;')

            elif query_atualizacoes_pp == 2: # Digite 2 para mostrar as Aparências ocupadas;
                confirmacao = True
                select('select aparencia FROM pp ORDER BY aparencia ASC;')

            elif query_atualizacoes_pp == 3: # Digite 3 para mostrar os Registros ninja ocupados; 
                confirmacao = True
                select('select registro_ninja from pp order by registro_ninja asc')

            elif query_atualizacoes_pp == 4: # "4" para mostrar as Bases
                confirmacao = True          
                print(sistema_base)
                copiar(sistema_base)

            elif query_atualizacoes_pp == 5: # Digite 5 para mostrar os Clãs ocupados;
                confirmacao = True             
                print(sistema_cla)
                copiar(sistema_cla)

            elif query_atualizacoes_pp == 6: # Digite 6 para mostrar a Ficha de Criação.
                confirmacao = True
                print(sistema_ficha)
                copiar(sistema_ficha)
                            
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
            "3" busca por Registro Ninja
            "4" busca por Base
            "5" busca por 
            "7" busca por Dono
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