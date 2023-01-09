from time import sleep
import pandas as pd

from modulos.utils import *
from modulos.query import *
from modulos.conecao import *

#######################################################################
""" 
remover.py é um o módulo principal pela função de remoção de informações a serem requeridas pelo query.py. O módulo carrega todas as funções que tenham o sentido
de remover algo ao banco de dados, de acordo com a guia dada pelo 
query.py
"""
#######################################################################

"""PLAYERS"""

def remover_player():
    confirmacao = False
    
    while confirmacao == False:
        print(select('select * from player order by id_player'))
        
        print('\nSOBRE O PLAYER A SER REMOVIDO:')
        id_player = int(input('Digite o id do player: '))
        
        confirmacao_player = input(f'''Está correto? 
Isso é uma ação delicada, irá excluir tudo sobre esse player de id = {id_player}. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')

        if confirmacao_player == '1':
            confirmacao = True
            
            # chama todas as funções de remover para assegurar que não sobre nada sobre esse player, logo, nada sobre o seu personagem também, para assim o player ser removido completamente
            
            remover_reen(p_remover_player = 1, p_id_player = id_player)
            remover_jinchuriki(p_remover_player = 1, p_id_player = id_player)
            remover_invo(p_remover_player = 1, p_id_player = id_player)
            remover_usuario(p_remover_player = 1, p_id_player = id_player)
            remover_pp(p_remover_player = 1, p_id_player = id_player)

            print(f'\nREMOVENDO PLAYER DE ID: {id_player}...')
            sleep(3)

            try:
                sql = f'''update player set recrutador = 0 where recrutador = {id_player}; DELETE FROM player WHERE id_player = {id_player}'''
                
                pd.read_sql_query(sql, con=engine)
                
                print('\nPLAYER REMOVIDO COM SUCESSO')
            
            except:
                print('\nPLAYER REMOVIDO COM SUCESSO')
                pass       
    return sql


"""PERSONAGENS"""

# esse parâmetro dado dentro da função serve para identificar quando que, na função remover_player foi confirmada a execução. Naturalmente ela é sempre 0, mas quando o remover_player chama essa função, ele dá o parâmetro p_remover_player como 1 e o p_id_player como o id_player dado na função, assim a função analisa quando o valor p_remover_player é igual a 1 e se for, ela executa a remoção do personagem. Quando a função remover_pp é chamada sem o gatilho da remover_player ela acaba repetindo a mesma lógica nas outras funções, pois para remover o pp por completo, ele não pode estar em relação com nenhuma outra tabela. Caso ela seja chamada pelo remover_player, isso não precisará ocorrer, pois as outras tabelas serão chamadas primeiro.
def remover_pp(p_remover_player = 0, p_id_player = 0):

    if p_remover_player == 1:
        id_player = p_id_player
        
        print(f'\nREMOVENDO PERSONAGEM DO PLAYER DE ID: {id_player}...')
        sleep(3)    
    
        try:
            sql = f'''DELETE FROM pp WHERE id_player = {id_player}'''
            pd.read_sql_query(sql, con=engine)
            
            print('PERSONAGEM REMOVIDO COM SUCESSO!')
    
        except:
            print('PERSONAGEM REMOVIDO COM SUCESSO!')
            pass 
    
    else:          
        confirmacao = True
    
        while confirmacao == False:
            print(select('select id_pp, id_player, nome, aparencia, base_1, base_2, base_3, cla_1, cla_2, cla_3, id_afiliacao, id_patente, id_cargo, data_criacao from pp order by id_pp'))

            print('\nSOBRE O PERSONAGEM A SER REMOVIDO:')
            id_pp = int(input('Digite o id do personagem: '))
        
            confirmacao_pp = input(f'''\nEstá correto?
Isso é uma ação delicada, irá excluir tudo sobre esse personagem de id = {id_pp}. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        
            if confirmacao_pp == '1':
                confirmacao = True
                
                remover_reen(p_remover_pp = 1, p_id_pp = id_pp)
                remover_jinchuriki(p_remover_pp = 1, p_id_pp = id_pp)
                remover_invo(p_remover_pp = 1, p_id_pp = id_pp)
                remover_usuario(p_remover_pp = 1, p_id_pp = id_pp)
                
                print(f'\nREMOVENDO PERSONAGEM DO PLAYER DE ID: {id_player}...')
                sleep(3)
                try:
                  
                    sql = f'''DELETE FROM pp WHERE id_pp = {id_pp}'''
                    pd.read_sql_query(sql, con=engine)

                    print('PERSONAGEM REMOVIDO COM SUCESSO!')
                except:
                    print('PERSONAGEM REMOVIDO COM SUCESSO!')
                    pass

    return 


"""ITENS"""

def remover_usuario(p_remover_player = 0, p_id_player = 0, p_remover_pp = 0, p_id_pp = 0):
    
    # caso o parâmetro for ativo por outra função. Remove TODAS as armas dos personagens desse player a ser removido
    if p_remover_player == 1:
        id_player = p_id_player

        print(f'\nREMOVENDO AS ARMAS DO(S) PERSONAGEM(S) DO PLAYER DE ID: {id_player}...')
        
        try:
            sql = f'''update arma set id_pp = 0 from pp where pp.id_player = {id_player}'''

            pd.read_sql_query(sql, con=engine)

            print('USUÁRIO REMOVIDO COM SUCESSO!')
        
        except:
            print('USUÁRIO REMOVIDO COM SUCESSO!')
            pass 

    # caso o parâmetro for ativo por outra função. Remove TODAS as armas desse personagem
    if p_remover_pp == 1:
        id_pp = p_id_pp
        
        print(f'\nREMOVENDO AS ARMAS DO PERSONAGEM DE ID: {id_pp}...')
        sleep(3)    
        
        try:
            sql = f'''update arma set id_pp = 0 where id_pp = {id_pp}'''
            
            pd.read_sql_query(sql, con=engine)

            print('ARMAS REMOVIDO COM SUCESSO!')
        
        except:
            print('USUÁRIO REMOVIDO COM SUCESSO!')
            pass

    # nenhum parãmetro for ativo, ou seja, a função foi chamada diretamente. Remove armas ESPECÍFICAS, não removendo todas caso o personagem detenha mais de uma.
    else:          
        confirmacao = True
        while confirmacao == False:

            print(select('select * from arma oder by id_arma'))

            print('\nSOBRE A ARMA QUE PERDEU SEU USUÁRIO:')
            id_arma = int(input('Digite o id da arma: '))
        
            confirmacao_arma = input(f'''\nEstá correto?
Isso é uma ação delicada, irá excluir qualquer personagem como dono de tal arma escolhida. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        
            if confirmacao_arma == '1':
                confirmacao = True
                print(f'\nREMOVENDO AS ARMAS DO PERSONAGEM DE ID: {id_pp}...')
                sleep(3)
                try:
                      

                    sql = f'''update arma set id_pp = 0 where id_arma = {id_arma}'''
                    pd.read_sql_query(sql, con=engine)
            
                    print(f'\nARMAS REMOVIDAS COM SUCESSO: {id_pp}...')
                
                except:
                    print(f'\nARMAS REMOVIDAS COM SUCESSO: {id_pp}...')
                    pass

    
    return 


"""NPCS"""

def remover_invo(p_remover_player = 0, p_id_player = 0, p_remover_pp = 0, p_id_pp = 0):
    
    # caso o parâmetro for ativo por outra função. Remove TODAS as armas dos personagens desse player a ser removido
    if p_remover_player == 1:
        id_player = p_id_player

        print(f'\nREMOVENDO AS INVOCAÇÕES DO(S) PERSONAGEM(S) DO PLAYER DE ID: {id_player}...')

        try:
            sql = f'''update invo set id_pp = 0 from pp where pp.id_player = {id_player}'''

            pd.read_sql_query(sql, con=engine)

            print('INVOCAÇÕES REMOVIDAS COM SUCESSO!')

        except:
            print('USUÁRIO REMOVIDO COM SUCESSO!')
            pass 

    # caso o parâmetro for ativo por outra função. Remove TODAS as armas desse personagem
    if p_remover_pp == 1:
        id_pp = p_id_pp
        
        print(f'\nREMOVENDO AS INVOCAÇÕES PERSONAGEM DE ID: {id_pp}...')
        sleep(3)    
        
        try:
            sql = f'''update invo set id_pp = 0 where id_pp = {id_pp}'''
            
            pd.read_sql_query(sql, con=engine)

            print('INVOCAÇÕES REMOVIDAS COM SUCESSO!')

        except:
            print('USUÁRIO REMOVIDO COM SUCESSO!')
            pass

    # nenhum parãmetro for ativo, ou seja, a função foi chamada diretamente. Remove armas ESPECÍFICAS, não removendo todas caso o personagem detenha mais de uma.
    else:          
        confirmacao = True
        while confirmacao == False:

            print(select('select * from invo oder by id_invo'))

            print('\nSOBRE A INVOCAÇÃO QUE PERDEU SEU INVOCADOR:')
            id_invo = int(input('Digite o id da invocação: '))
        
            confirmacao_invo = input(f'''\nEstá correto?
Isso é uma ação delicada, irá excluir qualquer invocação que esse personagem é invocador. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        
            if confirmacao_invo == '1':
                confirmacao = True
                
                print(f'\nREMOVENDO A INVOCAÇÃO PERSONAGEM DE ID: {id_pp}...')
                sleep(3)   
                try:

                    sql = f'''update invo set id_pp = 0 where id_invo = {id_invo}'''
                    pd.read_sql_query(sql, con=engine)
            
                except:
                    print('INVOCAÇÃO REMOVIDA COM SUCESSO!')      
                    pass    
    
    return 


def remover_jinchuriki(p_remover_player = 0, p_id_player = 0, p_remover_pp = 0, p_id_pp = 0):
    
    # caso o parâmetro for ativo por outra função. Remove TODAS as armas dos personagens desse player a ser removido
    if p_remover_player == 1:
        id_player = p_id_player

        print(f'\nREMOVENDO AS BIJUU(S) DO(S) PERSONAGEM(S) DO PLAYER DE ID: {id_player}...')
        sleep(3)  

        try:
            sql = f'''update bijuu set id_pp = 0 from pp where pp.id_player = {id_player}'''

            pd.read_sql_query(sql, con=engine)

            print('BIJUUS REMOVIDAS COM SUCESSO!')
        
        except:
            print('BIJUUS REMOVIDAS COM SUCESSO!')
            pass 

    # caso o parâmetro for ativo por outra função. Remove TODAS as armas desse personagem
    if p_remover_pp == 1:
        id_pp = p_id_pp
        
        print(f'\nREMOVENDO AS BIJJUS PERSONAGEM DE ID: {id_pp}...')
        sleep(3)    
        
        try:
            sql = f'''update bijuu set id_pp = 0 where id_pp = {id_pp}'''
            
            pd.read_sql_query(sql, con=engine)

            print('BIJUU REMOVIDAS COM SUCESSO!')
        except:
            print('BIJUU REMOVIDAS COM SUCESSO!')
            pass

    # nenhum parãmetro for ativo, ou seja, a função foi chamada diretamente. Remove armas ESPECÍFICAS, não removendo todas caso o personagem detenha mais de uma.
    else:          
        confirmacao = True
        while confirmacao == False:

            print(select('select * from bijuu oder by id_bijuu'))

            print('\nSOBRE A BIJUU QUE PERDEU SEU JINCHUURIKI:')
            id_bijuu = int(input('Digite o id da Bijuu: '))
        
            confirmacao_bijuu = input(f'''\nEstá correto?
Isso é uma ação delicada, irá excluir Bijuu que esse personagem é Jinchuuriki. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        
            if confirmacao_bijuu == '1':
                confirmacao = True

                print(f'\nREMOVENDO A BIJJU DO PERSONAGEM ID: {id_pp}...')
                sleep(3) 
                try:

                    sql = f'''update bijuu set id_pp = 0 where id_bijuu = {id_bijuu}'''
                    pd.read_sql_query(sql, con=engine)

                    print('BIJUU REMOVIDA COM SUCESSO!')
                except:
                    print('BIJUU REMOVIDA COM SUCESSO!')
                    pass       
        
    return 


def remover_reen(p_remover_player = 0, p_id_player = 0, p_remover_pp = 0, p_id_pp = 0):
    
    # caso o parâmetro for ativo por outra função. Remove TODAS as armas dos personagens desse player a ser removido
    if p_remover_player == 1:
        id_player = p_id_player

        print(f'\nREMOVENDO AS REENCARNAÇÃO(ÕES) DO(S) PERSONAGEM(S) DO PLAYER DE ID: {id_player}...')
        sleep(3)

        try:
            sql = f'''update reen set id_pp = 0 from pp where pp.id_player = {id_player}'''

            pd.read_sql_query(sql, con=engine)

            print('REENCARNAÇÕES REMOVIDAS COM SUCESSO!')

        except:
            print('REENCARNAÇÕES REMOVIDAS COM SUCESSO!')
            pass 

    # caso o parâmetro for ativo por outra função. Remove TODAS as armas desse personagem
    if p_remover_pp == 1:
        id_pp = p_id_pp
        
        print(f'\nREMOVENDO A REENCARNAÇÃO DO PERSONAGEM DE ID: {id_pp}...')
        sleep(3)    
        
        try:
            sql = f'''update reen set id_pp = 0 where id_pp = {id_pp}'''
            
            pd.read_sql_query(sql, con=engine)

            print('REENCARNAÇÃO REMOVIDA COM SUCESSO!')

        except:
            print('REENCARNAÇÃO REMOVIDA COM SUCESSO!')
            pass

    # nenhum parãmetro for ativo, ou seja, a função foi chamada diretamente. Remove armas ESPECÍFICAS, não removendo todas caso o personagem detenha mais de uma.
    else:          
        confirmacao = True
        while confirmacao == False:

            print(select('select * from reen oder by id_reen'))

            print('\nSOBRE A REENCARNAÇÃO QUE PERDEU SEU REENCARNADO:')
            id_reen = int(input('Digite o id da Reencarnação: '))
        
            confirmacao_reen = input(f'''\nEstá correto?
Isso é uma ação delicada, irá excluir Reencarnação que esse personagem é Reencarnado. 

Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        
            if confirmacao_reen == '1':
                confirmacao = True
                
                print(f'\nREMOVENDO A REENCARNAÇÃO DO PERSONAGEM DE ID: {id_pp}...')
                sleep(3)
                
                try:
                    sql = f'''update reen set id_pp = 0 where id_reen = {id_reen}'''
                    pd.read_sql_query(sql, con=engine)

                    print('REENCARNAÇÃO REMOVIDA COM SUCESSO!')
                except:
                    print('REENCARNAÇÃO REMOVIDA COM SUCESSO!')
                    pass           
    
    return 