from tkinter.tix import Tree
import pandas as pd
import phonenumbers

from modulos.utils import *
from modulos.query import *
from modulos.conecao import *

def remove_player():
    confirmacao = False
    while confirmacao == False:
        print(select('select * from player order by id_player'))
        print('\nSobre o Player à ser removido:')
        id_player = int(input('Digite o id do player: '))
        
        confirmacao_1 = input(f'''\nEstá correto? \nIsso é uma ação delicada, irá excluir tudo sobre esse player de id = {id_player}. Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        if confirmacao_1 == '1':
            confirmacao = True
            remove_pp(p_remove_player = 1, p_id_player = id_player)
            try:
                sql = f'''DELETE FROM player WHERE id_player = {id_player}'''
                pd.read_sql_query(sql, con=engine)
                print('\nRemovido com sucesso!')
            except: 
                pass       
    return sql

def remove_pp(p_remove_player = 0, p_id_player = 0):
    if p_remove_player == 1:
        id_player = p_id_player
        print('\nSobre o Personagem à ser removido:')
        print(f'Digite o id do dono do personagem: {id_player}')
            
        try:
            sql = f'''DELETE FROM pp WHERE id_player = {p_id_player}'''
            pd.read_sql_query(sql, con=engine)
        except:
            pass 
    else:          
        confirmacao = True
        while confirmacao == False:
            print(select('select id_pp, id_player, nome, aparencia, base, cla_1, cla_2, id_afiliacao, id_patente, id_cargo, data_criacao from pp order by id_pp'))
            print('\nSobre o Personagem à ser removido:')
            id_pp = int(input('Digite o id do personagem: '))
        
            confirmacao_1 = input(f'''\n

Está correto? \nIsso é uma ação delicada, irá excluir tudo sobre esse personagem de id = {id_pp}. Deseja continuar? "1" para "sim" e qualquer letra para "não": ''')
        if confirmacao_1 == '1':
            confirmacao = True
            remove_pp()
            try:
                sql = f'''DELETE FROM pp WHERE id_pp = {id_pp}'''
                pd.read_sql_query(sql, con=engine)
            except:
                pass

            confirmacao = False             
    return    