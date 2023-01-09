import pandas as pd

from modulos.utils import *
from modulos.conecao import *

#######################################################################
""" 
adder.py é um dos módulos secundários e que é o primeiro a ser requerido
pelo query.py. O módulo carrega todas as funções que tenham o sentido
de adicionar algo ao banco de dados, de acordo com a guia dada pelo 
query.py
"""
#######################################################################

"""PLAYERS"""

def add_player():
    confirmacao = False
    while confirmacao == False:
        
        print(select('select id_player, nome from player order by id_player asc'))

        print('\nSOBRE O PLAYER A SER REGISTRADO:')
        id_player = int(input('Id: '))
        nome = str(input('Nome: '))
        numero = str(input('Número: '))
        recrutador = int(input('Recrutado por: '))
        check_in = 0
        status = 'off'
        
        #formatar o número do player
        #numero_ajustado = phonenumbers.parse(numero, "BB")
        sql = f'''INSERT INTO player(
            id_player, nome, numero, recrutador, check_in, status)
    VALUES ({id_player}, '{nome}', '{numero}', {recrutador}, {check_in}, '{status}');
'''
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
                # input que abre um leque para escurtar trabalho e automatizar dados para criação de personagem. Ao responde que quer criar um personagem ao player, automaticamente o parâmento dado pela função atual (p_add_player) se torna ativo (1) e seguido, o parâmetro de id_player (p_id_player) se tornar o próprio ID dado na função, sendo assim, uma condição (1 + ID), por fim será lida pela funçaõ add_pp.
                input_add_pp = str(input('\nDeseja adicionar um Personagem para esse Player? 1 para "sim" e qualquer tecla para "não": '))
                if input_add_pp == "1":
                    confirmacao = True
                    add_pp(p_add_player = 1, p_id_player = id_player)
                else:
                    confirmacao = True

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql

def add_check_in():
    confirmacao = False
    while confirmacao == False:
            #printa primeiramente o check de todos os players para depois dar as opções de adição
            print(select('select id_player, nome, check_in from player order by check_in desc, id_player asc'))
            id_player = int(input('Digite o Id do player: '))
            novo_check_in = float(input('Digite os pontos ganhos: '))
            check_in_player = str(select(f'select check_in from player where id_player = {id_player}')).replace('check_in', '')

            antigo_check_in = float(check_in_player)

            check_in = round(novo_check_in + antigo_check_in,2)
            print(f'\nO novo valor de Check In: {novo_check_in} + {antigo_check_in} = {check_in}')

            sql = f"update player set status = 'on' where id_player = {id_player}; UPDATE player SET check_in = {check_in} WHERE id_player = {id_player}"
            confirmacao_1 = str(input(f'''\nConfirmação dos valores:
    
    {sql} 

está correto? 1 para "sim" e qualquer valor para "não". '''))
            
            if confirmacao_1 == '1':
                confirmacao = True

                try:
                    
                    pd.read_sql_query(sql, con=engine)

                    confirmacao_add_new_check_in = str(input('\nDeseja adicionar mais pontos? 1 para "sim" e qualquer tecla para "não": '))
                    if confirmacao_add_new_check_in == "1":
                        add_check_in()
                except:
                    confirmacao_add_new_check_in = str(input('\nDeseja adicionar mais pontos? 1 para "sim" e qualquer tecla para "não": '))
                    if confirmacao_add_new_check_in == "1":
                        add_check_in()
    return


"""ITENS"""

def add_arma():
    confirmacao = False
    while confirmacao == False:

        print('\n LISTA DE PERSONAGEMS')
        print(select('Select id_pp, nome from pp order by id_pp asc')) # select para os personagems

        print('\n LISTA DE ARMAS')
        #print(select('select * from arma where id_arma < 40'))
        print(select('select * from arma order by id_arma asc')
        )
        print('\nSOBRE O PERSONAGEM A SER DADO A ARMA:')
        id_arma = float(input('Digite o ID da arma: '))
        select('Select id_pp, nome from pp')
        id_pp = float(input('Digite o id do pp: '))
        sql = f"update arma set id_pp = {id_pp} where id_arma = {id_arma}"
        
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                    break
                finally:
                    break

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql


"""NPCS"""

def add_invo():
    confirmacao = False
    while confirmacao == False:

        print('\n LISTA DE PERSONAGEMS')
        print(select('Select id_pp, nome from pp order by id_pp asc')) # select para os personagems

        print('\n LISTA DE INVOCAÇÕES')
        print(select('Select * from invo order by id_invo asc')) # select para mostrar as invos, seus id e dono

        print('\nSOBRE O iNVOCADOR A SER REGISTRADO:')
        id_invo = int(input('Digite o ID da invo: '))
        select('Select id_pp, nome from pp')
        id_pp = float(input('Digite o id do pp: ')) 
        sql = f"update invo set id_pp = {id_pp} where id_invo = {id_invo}"
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                    break
                finally:
                    break

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql


def add_bijuu():
    confirmacao = False
    while confirmacao == False:

        print('\n LISTA DE PERSONAGEMS')
        print(select('Select id_pp, nome from pp order by id_pp asc')) # select para os personagems

        print('\n LISTA DE BIJUUS')
        print(select('Select * from bijuu order by id_bijuu asc')) # select para mostrar as bijuu, seus id e jinchuriki

        print('\nSOBRE O JINCHURIKI A SER REGISTRADO:')
        id_bijuu = int(input('Digite o ID da Bijuu: '))
        select('Select id_pp, nome from pp')
        id_pp = float(input('Digite o id do pp: ')) 
        sql = f"update bijuu set id_pp = {id_pp} where id_bijuu = {id_bijuu}"
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                    break
                finally:
                    break

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql


def add_reen():
    confirmacao = False
    while confirmacao == False:

        print('\n LISTA DE PERSONAGEMS')
        print(select('Select id_pp, nome from pp order by id_pp asc')) # select para os personagems

        print('\n LISTA DE REENCARNAÇÕES')
        print(select('Select * from reen order by id_reen asc')) # select para mostrar as reencarnação, seus id e seus reencarnados

        print('\nSOBRE O REENCARNADO A SER REGISTRADO:')
        id_reen = int(input('Digite o ID da Reencarnação: '))
        select('Select id_pp, nome from pp')
        id_pp = float(input('Digite o id do pp: ')) 
        sql = f"update reen set id_pp = {id_pp} where id_reen = {id_reen}"
        try:
            confirmacao_1 = int(input(f'''Confirmação dos valores:
 
{sql} 

está correto? 1 para "sim" 0 para "não". '''))
            if confirmacao_1 == 1:
                confirmacao = True
                try:
                    pd.read_sql_query(sql, con=engine)
                    break
                finally:
                    break

            elif confirmacao_1 == 0:
                 confirmacao = False
            else:
                 confirmacao = False                             
        except ValueError:
            print('O valor não corresponde. Tente novamente')
    return sql


"""PERSONAGEM"""

def add_pp(p_add_player = 0, p_id_player = 0):
    
    # lê os parâmetros de add_player (parâmetro q é ativado quando se confirma adicionar um personagem ao player registrado no add_player) e transforma o parâmetro recebido como p_id_player no id do player, óbvio, dono do personagem e como. Dentro do banco de dados o id de um personagem é a junção do id do seu dono antes do ponto e depois do ponto é correspondente ao número de personagens possuído. Se o player é Id 1 e esse é o seu primeiro / único personagem, logo, o id do personagem é 1.1
    if p_add_player == 1:
        id_player = p_id_player
        id_pp = float(p_id_player)+ 0.1 # como todo player novo já de fábrica vem com apenas um persongam, basta pegar o seu valor e somar por 0.1
        print(f'Id do player dono do personagem: {id_player}')
        print(f'Id do personagem: {id_pp}')

    
    else:
        print('\nPLAYERS / ID EXISTENTES:')
        # printa os players para saber os ids disponíveis
        print(select('select id_player, nome from player order by id_player asc'))
        print('\nSOBRE O PERSONAGEM A SER REGISTRADO:')
        id_pp = float(input('Id do personagem: '))
        # dado o id do personagem, aqui transformamos o id_pp em string, para que possa haver uma retirada dos valores atrás do ponto
        s_id_pp= str(id_pp) 
        s_id_player = s_id_pp[0:s_id_pp.find('.')]
        print(f'Id do player dono do personagem: {s_id_player}')
        id_player = int(s_id_player)


    confirmacao = False
    while confirmacao == False:

        # em toda variável terá um looping para confirmar a informação dada.

        print('Caso tenha digitado algo errado enquanto fazia os resgistros, basta digitar 0 logo após. Caso tudo tenha ido corretamente, basta digitar qualquer outra letra.')
        
        

        nome = str(input('Nome: '))
        aparencia = str(input('Aparência: '))            
        sangue = str(input('Tipo sanguíneo: '))
        
        base_1 = str(input('1° Base: '))
        # se a primeira base for igual a 0, significa que ele não tem nenhuma base, logo irá partir para os clãs
        if base_1 == '0':
            base_2 = '0'
            base_3 = '0'

        else:
            # base 2
            base_2 = str(input('2° Base: '))

            if base_2 == '0':
                base_3 = '0'

            else:
                # base 3
                base_3 = str(input('3° Base: '))


# confirmação para os clãs

        cla_1 = str(input('1° Clã: '))
        
        # se a primeira cla for igual a 0, significa que ele não tem nenhuma clã
        if cla_1 == '0':
            cla_2 = '0'
            cla_3 = '0'

        else:
            # cla 2
            cla_2 = str(input('2° Clã: '))

            if cla_2 == '0':
                cla_3 = '0'

            else:
                # cla 3
                cla_3 = str(input('3° Clã: '))


        id_afiliacao = int(input('''Afiliação:
    1 = Shinobi;
    2 = Andarilho;
    3 = Nukkenin.
'''))
        
        id_patente = 1

        id_elemento_1 = int(input('''1° Elemento:
        1 = Katon
        2 = Fuuton
        3 = Raiton
        4 = Doton
        5 = Suiton
''')) 

        if cla_1 == "Sarutobi" or cla_2 == "Sarutobi" or cla_3 == 'Sarutobi':
            id_elemento_2 = int(input('''2° Elemento:
        0 = Nenhum
        1 = Katon
        2 = Fuuton
        3 = Raiton
        4 = Doton
        5 = Suiton
''')) 
        
        else: 
            id_elemento_2 = 0

        data_criacao= str(input('Data de criação: '))

        # mostras as hiden dentro do sistema
        print(select('select id_hiden, nome from hiden order by id_hiden asc'))
        id_hiden_1 = float(input('1° Hiden: '))
        
        
        if id_hiden_1 == 0: #SEM HIDEN
            id_hiden_2 = 0
            id_hiden_3 = 0

            # mostrar as kkg dentro do sistema
            print(select('select id_kkg, nome from kkg order by id_kkg asc'))
            id_kkg_1 = float(input('1° Kekkei Genkai: '))
            
            
            if id_kkg_1 == 0: #SEM HIDEN E SEM KKG
                id_kkg_2 = 0
                id_kkg_3 = 0 
            
            else:
                id_kkg_2 = float(input('2° Kekkei Genkai: ')) 
                
                if id_kkg_2 == 0:
                    id_kkg_3 = 0
                    
                else:
                    id_kkg_3 = float(input('3° Kekkei Genkai: '))    
            
        else:
            id_hiden_2 = float(input('2° Hiden: '))
            
            if id_hiden_2 == 0: #Se uma Hiden for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas 
                id_hiden_3 = 0

                # mostrar as kkg dentro do sistema
                print(select('select id_kkg, nome from kkg order by id_kkg asc'))
                id_kkg_1 = float(input('1° Kekkei Genkai: '))
                
                if id_kkg_1 == 0: #Se uma Kkg for = 0, as que vem depois obviamente não vão existir. Logo, serão excluídas
                    id_kkg_2 = 0
                    id_kkg_3 = 0

                else:
                    id_kkg_2 = float(input('2° Kekkei Genkai: '))
                        
                        
                    if id_kkg_2 == 0:
                        id_kkg_3 = 0

                    else:
                        id_kkg_3 = float(input('3° Kekkei Genkai: '))

            else:
                id_hiden_3 = float(input('3° Hiden: '))

                # mostrar as kkg dentro do sistema
                print(select('select id_kkg, nome from kkg order by id_kkg asc'))
                id_kkg_1 = float(input('1° Kekkei Genkai: ')) 
                
                if id_kkg_1 == 0:
                    id_kkg_2 = 0
                    id_kkg_3 = 0

                else:
                    id_kkg_2 = float(input('2° Kekkei Genkai: '))
                    
                    
                    if id_kkg_2 == 0:
                        id_kkg_3 = 0
                        
                    else:
                        id_kkg_3 = float(input('3° Kekkei Genkai: '))

        sql = f'''
            INSERT INTO pp(
                id_pp, id_player, nome, aparencia, sangue, base_1, base_2, base_3, cla_1, cla_2, cla_3, 
                id_afiliacao, id_patente, id_elemento_1, id_elemento_2,
                data_criacao, id_hiden_1, id_hiden_2, id_hiden_3,
                id_kkg_1, id_kkg_2, id_kkg_3, pontos_missao)
        VALUES ({id_pp}, {id_player}, '{nome}', '{aparencia}', '{sangue}', '{base_1}', '{base_2}', '{base_3}', '{cla_1}', '{cla_2}','{cla_3}', {id_afiliacao}, {id_patente}, {id_elemento_1}, {id_elemento_2}, '{data_criacao}', {id_hiden_1}, {id_hiden_2}, {id_hiden_3}, {id_kkg_1}, {id_kkg_2}, {id_kkg_3}, 0);'''
                
        confirmacao_1 = input(f'''\nConfirmação dos valores:
    
    {sql} 

    está correto? "1" para "sim" e qualquer valor para "não". ''')
        if confirmacao_1 == '1':
            confirmacao = True
            try:
                pd.read_sql_query(sql, con=engine)
            except:
                pass
            #confirmacao = True
    return sql

def add_pontos_missao():
    confirmacao = False
    while confirmacao == False:
            #printa primeiramente os pontos de todos os players para depois dar as opções de adição
            print(select(' select id_pp, nome, pontos_missao from pp order by pontos_missao  desc, id_pp asc'))
            id_pp = float(input('Digite o Id do personagem: '))
            novo_pontos_missao = int(input('Digite os pontos ganhos: '))
            pontos_missao_pp = str(select(f'select pontos_missao from pp where id_pp = {id_pp}')).replace('pontos_missao', '')

            antigo_pontos_missao = int(pontos_missao_pp)

            pontos_missao = novo_pontos_missao + antigo_pontos_missao
            print(f'\nO novo valor de Pontos de Missão: {novo_pontos_missao} + {antigo_pontos_missao} = {pontos_missao}')

            sql = f'UPDATE pp SET pontos_missao = {pontos_missao} WHERE id_pp = {id_pp}'
            confirmacao_1 = str(input(f'''\nConfirmação dos valores:
    
    {sql} 

está correto? 1 para "sim" e qualquer valor para "não". '''))
            
            if confirmacao_1 == '1':
                confirmacao = True
            
                try:
                    pd.read_sql_query(sql, con=engine)

                    confirmacao_add_new_pontos_missao = str(input('\nDeseja adicionar mais pontos? 1 para "sim" e qualquer tecla para "não": '))
                    if confirmacao_add_new_pontos_missao == "1":
                        add_pontos_missao()
                except:
                    confirmacao_add_new_pontos_missao = str(input('\nDeseja adicionar mais pontos? 1 para "sim" e qualquer tecla para "não": '))
                    if confirmacao_add_new_pontos_missao == "1":
                        add_pontos_missao()
    return