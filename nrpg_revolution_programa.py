from multiprocessing import connection
from re import T
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine
from datetime import datetime
tempo = datetime.now()


#criação de conexão
engine = create_engine('postgresql://postgres:160587pvcdacr4sh-pvCr4sh_PV@localhost:5432/nrpg_revolution')

#Lista

#Query
def SELECT_simples(sql):
    df = pd.read_sql_query(sql, con=engine)
    print(df)
    return sql

def SELECT(sql):
    try:
        df = pd.read_sql_query(sql, con=engine)
        print(df)
    finally: 
        query_adicional()
    return sql

#Para fazer a atualização de base MUDAAAAAAAAAAR
def SELECT_base():
    sql = 'SELECT base FROM pp_info ORDER BY base ASC;'
    df = pd.read_sql_query(sql, con=engine)
    print(df)
    return df

#INSERT INTO arma_info MUDAAAAAAAAAAR
def commit_arma():
    confirmacao = False
    while confirmacao == False:
        arma = str(input('Digite o nome completo da Arma: '))
        personagem_1 = str(input('Digite o nome do personagem que possui a arma: ')) 
        personagem_2 = str(input('Digite o nome do personagem que possui a arma: ')) 
        personagem_3 = str(input('Digite o nome do personagem que possui a arma: ')) 
        personagem_4 = str(input('Digite o nome do personagem que possui a arma: ')) 
        personagem_5 = str(input('Digite o nome do personagem que possui a arma: ')) 
        personagem_6 = str(input('Digite o nome do personagem que possui a arma: '))
        id_arma = int(input('Digite o ID da arma: '))
        sql = f"INSERT INTO arma_info(arma, personagem_1, personagem_2, personagem_3, personagem_4, personagem_5, personagem_6, id_arma) VALUES ('{arma}', '{personagem_1}', '{personagem_2}', '{personagem_3}', '{personagem_4}', {personagem_5}', '{personagem_6}, {id_arma})"
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    df = pd.read_sql_query(sql, con=engine)
                finally:
                    query_adicional()

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

#INSERT INTO invo_info MUDAAAAAAAAAAR
def commit_invo(): 
    confirmacao = False
    while confirmacao == False:
        invo = str(input('Digite o nome da invocação: '))
        personagem_1 = str(input('Digite o nome do personagem que possui a invo(1): ')) 
        personagem_2 = str(input('Digite o nome do personagem que possui a invo(2): ')) 
        id_invo = int(input('Digite o ID da invo: '))
        sql = f"INSERT INTO invo_info(invo, personagem_1, personagem_2, id_invo) VALUES ('{invo}', '{personagem_1}', '{personagem_2}', {id_invo})"
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    df = pd.read_sql_query(sql, con=engine)
                finally:
                    query_adicional()

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

#INSERT INTO player_info MUDAAAAAAAAAAR
def commit_player():
    confirmacao = False
    while confirmacao == False:
        id_player = int(input('''Id: '''))
        nome = str(input('Nome: '))
        numero = int(input('Número: ')) 
        recrutador = int(input('''Recrutado por: '''))
        sql = f'''INSERT INTO player(
            id_player, nome, numero, recrutador)
    VALUES ({id_player}, '{nome}', {numero}, {recrutador});
'''
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                finally:
                    query_adicional()

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

#INSERT INTO pp_info MUDAAAAAAAAAAR
def commit_pp():
    confirmacao = False
    while confirmacao == False:
        id_pp = float(input('Id do personagem: '))
        id_player = int(input('Id do player dono do personagem: '))
        nome = str(input('Nome: '))
        aparencia = str(input('Aparência: '))
        sangue = str(input('Tipo sanguíneo: '))
        base = str(input('Base: '))
        cla_1 = str(input('Cla 1: ')) 
        cla_2 = str(input('Cla 2: ')) 
        id_afiliacao = int(input('''Afiliação:
    1 = Shinobi;
    2 = Andarilho;
    3 = Nukkenin.
''')) 
        id_patente = int(input('''Patente:
    1 = Acadêmico / Rank E
    2 = Gennin / Rank D
    3 = Chunnin / Rank C
    4 = Jounnin / Rank B
    5 = Jounnin Rank A
    6 = Jounnin Rank S
''')) 
        id_elemento_1 = int(input('''1° Elemento:
    1 = Katon
    2 = Fuuton
    3 = Raiton
    4 = Doton
    5 = Suiton
''')) 
        id_elemento_2 = int(input('''2° Elemento:
    0 = Nenhum
    1 = Katon
    2 = Fuuton
    3 = Raiton
    4 = Doton
    5 = Suiton
''')) 
        registro_ninja = int(input('Registro ninja: '))
        data_criacao= str(input('Data de criação: '))
        id_hiden_1 = float(input('1° Hiden: '))
        if id_hiden_1 == 0: #SEM HIDEN
            id_kkg_1 = int(input('1° Kekkei Genkai: '))
            if id_kkg_1 == 0: #SEM HIDEN E SEM KKG
                id_traco_unico_1 = int(input('1° Traço Único: '))
                if id_traco_unico_1 == 0: #Se um Traço único for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas

                    # SEM TUDO
                    sql = f''' 
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}');'''
                else: 
                    id_traco_unico_2 = int(input('2° Traço Único: '))
                    if id_traco_unico_2 == 0: #Se um Traço único for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas

                        # 1 TRAÇO
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_traco_unico_1});'''
                    else:
                        id_traco_unico_3 = int(input('3° Traço Único: '))

                        # 3 TRAÇO
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_traco_unico_1, 
            id_traco_unico_2)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_traco_unico_1}, {id_traco_unico_2}, {id_traco_unico_3});'''
            else:
                id_kkg_2 = int(input('2° Kekkei Genkai: '))
                if id_kkg_2 == 0:
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 1 KKG
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_kkg_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1});'''
                    else:
                        id_traco_unico_2 = int(input('2° Traço Único: '))
                        if id_traco_unico_2 == 0: # 0 HIDEN 1 KKG E 1 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_kkg_1, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1}, {id_traco_unico_1});'''
                        else: # 0 HIDEN 1 KKG E 3 TRAÇO
                            id_traco_unico_3 = int(input('3° Traço Único: '))                 
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''                
                else:
                    id_kkg_3 = int(input('3° Kekkei Genkai: '))
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 3 KKG
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1}, {id_kkg_2}, {id_kkg_3});'''
                    else:
                        id_traco_unico_2 = int(input('2° Traço Único: '))
                        if id_traco_unico_2 == 0: # 0 HIDEN 3 KKG E 1 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1});'''
                        else: # SEM HIDEN 3 KKG 3 TRAÇO
                            id_traco_unico_3 = int(input('3° Traço Único: '))
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao,id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''
        else:
            id_hiden_2 = float(input('2° Hiden: '))
            if id_hiden_2 == 0: #Se uma Hiden for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas
                id_kkg_1 = int(input('1° Kekkei Genkai: '))
                if id_kkg_1 == 0: #Se uma Kkg for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 1 HIDEN 0 KKG E 0 TRAÇO
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1});'''
                    else:
                        id_traco_unico_2 = int(input('2° Traço Único: '))
                        if id_traco_unico_2 == 0: # 1 HIDEN 0 KKG E 1 TRAÇO
                           sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_traco_unico_1});''' 
                        else: # 1 HIDEN 0 KKG E 3 TRAÇO
                            id_traco_unico_3 = int(input('3° Traço Único: '))
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_traco_unico_1}, {id_traco_unico_2}, {id_traco_unico_3});'''
                else:
                    id_kkg_2 = int(input('2° Kekkei Genkai: '))
                    if id_kkg_2 == 0:
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 1 HIDEN 1 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1});'''
                        else:
                            id_traco_unico_2 = int(input('2° Traço Único: '))
                            if id_traco_unico_2 == 0: # 1 HIDEN 1 KKG E 1 TRAÇO
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_kkg_1, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_traco_unico_1});'''
                            else: # 1 HIDEN 1 KKG E 3 TRAÇO
                                id_traco_unico_3 = int(input('3° Traço Único: '))
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_kkg_1, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''                  
                    else:
                        id_kkg_3 = int(input('3° Kekkei Genkai: '))
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 1 HIDEN 3 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_kkg_2}, {id_kkg_3});'''
                        else:
                            id_traco_unico_2 = int(input('2° Traço Único: '))
                            if id_traco_unico_2 == 0: # 1 HIDEN 3 KKG E 1 TRAÇO
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1},{id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1});'''
                            else:
                                id_traco_unico_3 = int(input('3° Traço Único: '))
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1}, {id_traco_unico_2}, {id_traco_unico_3});'''
            else:
                id_hiden_3 = float(input('3° Hiden: '))
                id_kkg_1 = int(input('1° Kekkei Genkai: ')) 
                if id_kkg_1 == 0:
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 ==0:  # 3 HIDEN
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3});'''
                    else:
                        id_traco_unico_2 = int(input('2° Traço Único: '))
                        if id_traco_unico_2 == 0: # 3 HIDEN 0 KKG E 1 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, {id_traco_unico_1});'''
                        else: # 3 HIDEN 0 KKG E 3 LAÇO
                            id_traco_unico_3 = int(input('3° Traço Único: '))    
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''   
                else:
                    id_kkg_2 = int(input('2° Kekkei Genkai: '))
                    if id_kkg_2 == 0:
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 ==0: # 3 HIDEN 1 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1});'''
                        else: 
                            id_traco_unico_2 = int(input('2° Traço Único: '))
                            if id_traco_unico_2 == 0: # 3 HIDEN 1 KKG E 1 TRAÇO
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_traco_unico_1});'''
                            else: # 3 HIDEN 1 KKG E 3 TRAÇO
                                id_traco_unico_3 = int(input('3° Traço Único: '))
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_, id_traco_unico_1, id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''
                    else:
                        id_kkg_3 = int(input('3° Kekkei Genkai: '))
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 3 HIDEN 3 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_kkg_2}, {id_kkg_3});'''
                        else:
                            id_traco_unico_2 = int(input('2° Traço Único: '))
                            if id_traco_unico_2 ==0: # 3 HIDEN 3 KKG E 1 TRAÇO
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1});'''
                            else: # 3 HIDEN 3 KKG E 3 TRAÇO
                                id_traco_unico_3 = int(input('3° Traço Único: '))
                                sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3, id_traco_unico_1, 
            id_traco_unico_2, id_traco_unico_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{registro_ninja}', 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                finally:
                        query_adicional()
            elif confirmacao_1 == 0:
                confirmacao = False
            else:
                confirmacao = False             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

# atualizar as bases  MUDAAAAAAAAAAR
def atualizacao_base(nome, limite):
    base_lista = str(pd.read_sql_query('SELECT base FROM pp_info;', con=engine))
    conta = base_lista.count(nome)
    if conta > limite:
        print('Base lotada.')
        base = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
        
    else:
        base = f'{nome} ({conta}/{limite})'
    return base

# atualizar os clãs  MUDAAAAAAAAAAR
def atualizacao_cla(nome, limite):
    cla_lista = str(pd.read_sql_query('SELECT cla_1, cla_2 FROM pp_info;', con=engine))
    conta = cla_lista.count(nome)
    if conta > limite:
        print('Base lotada.')
        cla = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
    else:
        cla = f'{nome} ({conta}/{limite})'
    return cla

#imput sobre query  MUDAAAAAAAAAAR
def query(): 
    analise_operacao = False 
    while analise_operacao == False:
        try:
            query = int(input('''Quais operações deseja fazer? 
SELECT;
    Digite 1 para fazer um 'SELECT * FROM arma;' 
    Digite 2 para fazer um 'SELECT * FROM invo;' 
    Digite 3 para fazer um 'SELECT * FROM player;'
    Digite 4 para fazer um 'SELECT * FROM pp;'
        Digite 40 para mostrar as aparências ocupadas;'
        Digite 41 para mostrar os nomes ocupados;'
        Digite 42 para mostrar as bases atualizadas;
        Digite 43 para mostras os clãs atualizados;

INSERT;
    Digite 6 para fazer um 'INSERTO INTO arma;'
    Digite 7 para fazer um 'INSERT INTO invo;'
    Digite 8 para fazer um 'INSERT INTO player;'
    Digite 9 para fazer um 'INSERT INTO pp;'
'''))
            if query == 1:
                analise_operacao = True
                SELECT('SELECT * FROM arma_info;')
            elif query == 2:
                analise_operacao = True
                SELECT('SELECT * FROM invo_info;')
            elif query == 3:
                analise_operacao = True
                SELECT('SELECT * FROM player_info;')
            elif query == 4:
                analise_operacao = True
                SELECT('SELECT * FROM pp_info;')
            elif query == 5:
                analise_operacao = True
                SELECT('SELECT * FROM clas_info ORDER BY id_clas ASC')
            if query == 6:
                analise_operacao = True
                commit_arma()
            elif query == 7:
                analise_operacao = True
                commit_invo()
            elif query == 8:
                analise_operacao = True
                commit_player()
            elif query == 9:
                analise_operacao = True
                commit_pp()
            elif query == 40: # select aparencia
                analise_operacao = True
                SELECT('SELECT aparencia as aparências_em_uso FROM pp_info ORDER BY aparencia ASC;')
            elif query == 41: # select nome
                analise_operacao = True
                SELECT('SELECT personagem as nomes_de_personagem_em_uso FROM pp_info ORDER BY personagem ASC;')
            elif query == 42: # select base
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
『❌』> {atualizacao_base('Deidara', 3)}
『❌』> {atualizacao_base('Haku', 3)}
『❌』> {atualizacao_base('Hashirama', 1)}
『❌』> {atualizacao_base('Itachi', 2)}
『❌』> {atualizacao_base('Jigen', 1)}
『❌』> {atualizacao_base('Jiraya', 3)}
『❌』> {atualizacao_base('Juugo', 3)}
『❌』> {atualizacao_base('Hiruko', 1)}
『❌』> {atualizacao_base('Kabuto', 1)}
『❌』> {atualizacao_base('Kahyo', 2)}
『❌』> {atualizacao_base('Karin', 2)}
『❌』> {atualizacao_base('Kashin Koji', 2)}
『❌』> {atualizacao_base('Kakashi', 2)}
『❌』> {atualizacao_base('Madara', 5)}
『❌』> {atualizacao_base('Mei Terumi', 2)}
『❌』> {atualizacao_base('Minato', 2)}
『❌』> {atualizacao_base('Neji', 5)}
『❌』> {atualizacao_base('Obito', 1)}
『❌』> {atualizacao_base('Orochimaru', 1)} 
『❌』> {atualizacao_base('Sakon', 3)}
『❌』> {atualizacao_base('Sasori', 1)}
『❌』> {atualizacao_base('Sasuke', 3)}
『❌』> {atualizacao_base('Shin Uchiha', 1)}
『❌』> {atualizacao_base('Shinno', 1)}
『❌』> {atualizacao_base('Shion', 3)}
『❌』> {atualizacao_base('Shisui', 1)}
『❌』> {atualizacao_base('Tobirama', 1)}
『❌』> {atualizacao_base('Tsunade', 2)}
『❌』> {atualizacao_base('Yakumo', 2)}
'''
                print(sistema_base)
                query_adicional()
            elif query == 43: # select clã
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
● ━━━━━━━'''.format(atualizacao_cla('Yome', 10), atualizacao_cla('Namikaze', 10), atualizacao_cla('Ranmaru', 10), atualizacao_cla('Guren', 10), atualizacao_cla('Karatachi', 10), atualizacao_cla('Otenki', 10), atualizacao_cla('Sakon e Ukon', 10), atualizacao_cla('Kumotami', 10), atualizacao_cla('Pakura', 10), atualizacao_cla('Bakurei', 10), atualizacao_cla('Haruno', 10), atualizacao_cla('Hatake', 10), atualizacao_cla('Maito', 5), atualizacao_cla('Lee', 5), atualizacao_cla('Terumi', 10), atualizacao_cla('Shion', 5), atualizacao_cla('Rinji', 10), atualizacao_cla('Ameyuki', 10))
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
                query_adicional()
            else:
                print('O valor não corresponde. Tente novamente')
                analise_operacao = False             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
            analise_operacao = False  
    return analise_operacao

#imput sobre query adicional
def query_adicional():
    repeticao = True
    while repeticao == True:
        try:
            confirmacao = int(input('Deseja fazer mais alguma ação? Digite 1 para "sim" e 0 "não" '))
            if confirmacao == 1:
                repeticao = False
                query()
            elif confirmacao == 0:
                repeticao = False
                print('Fim de Conexão. Bem sucessidida.')
                break
            else:
                repeticao = False

        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return 

query()