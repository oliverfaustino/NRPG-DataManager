import pandas as pd
#from sqlalchemy import create_engine
from modulos.select_engine import *

#engine = create_engine('postgresql://postgres:160587pvcdacr4sh-pvCr4sh_PV@localhost:5432/nrpg_revolution')

#
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
                    pass

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
                    pass

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

#INSERT INTO player
def commit_player():
    confirmacao = False
    while confirmacao == False:
        select('select id_player, nome from player order by id_player asc')
        print('\nSobre o Player à ser registrado')
        id_player = int(input('Id: '))
        nome = str(input('Nome: '))
        numero = int(input('Número: ')) 
        recrutador = int(input('Recrutado por: '))
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
                    pass

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

#INSERT INTO pp
def commit_pp():
    confirmacao = False
    while confirmacao == False:
        select('select id_player, nome from player order by id_player asc')
        print('\nSobre o Personagem à ser registrado')
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
        select('select id_hiden, nome from hiden order by id_hiden asc')
        id_hiden_1 = float(input('1° Hiden: '))
        if id_hiden_1 == 0: #SEM HIDEN
            select('select id_kkg, nome from kkg order by id_kkg asc')
            id_kkg_1 = float(input('1° Kekkei Genkai: '))
            if id_kkg_1 == 0: #SEM HIDEN E SEM KKG
                select('select id_traco_unico, nome from traco_unico order by id_traco_unico asc')
                id_traco_unico_1 = int(input('1° Traço Único: '))
                if id_traco_unico_1 == 0: #Se um Traço único for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas

                    # SEM TUDO
                    sql = f''' 
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
                id_kkg_2 = float(input('2° Kekkei Genkai: '))
                if id_kkg_2 == 0:
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 1 KKG
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_kkg_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''                
                else:
                    id_kkg_3 = float(input('3° Kekkei Genkai: '))
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 3 KKG
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''
        else:
            id_hiden_2 = float(input('2° Hiden: '))
            if id_hiden_2 == 0: #Se uma Hiden for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas
                id_kkg_1 = float(input('1° Kekkei Genkai: '))
                if id_kkg_1 == 0: #Se uma Kkg for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 == 0: # 1 HIDEN 0 KKG E 0 TRAÇO
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
                    id_kkg_2 = float(input('2° Kekkei Genkai: '))
                    if id_kkg_2 == 0:
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 1 HIDEN 1 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_kkg_1)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''                  
                    else:
                        id_kkg_3 = float(input('3° Kekkei Genkai: '))
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 1 HIDEN 3 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_hiden_1}, {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, {id_traco_unico_1}, {id_traco_unico_2}, {id_traco_unico_3});'''
            else:
                id_hiden_3 = float(input('3° Hiden: '))
                id_kkg_1 = float(input('1° Kekkei Genkai: ')) 
                if id_kkg_1 == 0:
                    id_traco_unico_1 = int(input('1° Traço Único: '))
                    if id_traco_unico_1 ==0:  # 3 HIDEN
                        sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''   
                else:
                    id_kkg_2 = float(input('2° Kekkei Genkai: '))
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
            '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, 
            {id_kkg_1}, {id_traco_unico_1}, {id_traco_unico_2}, 
            {id_traco_unico_3});'''
                    else:
                        id_kkg_3 = float(input('3° Kekkei Genkai: '))
                        id_traco_unico_1 = int(input('1° Traço Único: '))
                        if id_traco_unico_1 == 0: # 3 HIDEN 3 KKG E 0 TRAÇO
                            sql = f'''
        INSERT INTO pp(
            id_pp, id_player, nome, aparencia, sangue, base, cla_1, cla_2, 
            id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
            registro_ninja, data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
            id_kkg_1, id_kkg_2, id_kkg_3)
    VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base}', '{cla_1}', '{cla_2}', 
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
            {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, {registro_ninja}, 
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
                except:
                    pass

            elif confirmacao_1 == 0:
                confirmacao = False
            else:
                confirmacao = False             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

