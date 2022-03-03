import pandas as pd
from modulos.conecao import *
from modulos.utils import select


# atualizar os invo
def update_invo(nome, id): 
    lista= str(pd.read_sql_query(f'select pp.id_pp, pp.nome from pp, invo where pp.id_pp = invo.id_pp_1 and invo.id_invo = {id}', con=engine))
    invo_lista = lista.replace('id_pp', '').replace('nome', '').replace('0', '').split()
    invo = f'{id} {nome}: {invo_lista};'
    return invo



# atualizar os clãs
def update_cla(nome, limite):
    cla_lista = str(pd.read_sql_query('SELECT cla_1, cla_2 FROM pp;', con=engine))
    conta = cla_lista.count(nome)
    
    if conta > limite:
        print('Base lotada.')
        cla = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
    
    else:
        cla = f'{nome} ({conta}/{limite})'
    
    return cla
    


# atualizar as bases
def update_base(nome, limite):
    base_lista = str(pd.read_sql_query('SELECT base FROM pp;', con=engine))
    conta = base_lista.count(nome)
    
    if conta > limite:
        print('Base lotada.')
        base = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
        
    else:
        base = f'{nome} ({conta}/{limite})'
    
    return base



# atualizar check_in
def update_check_in():
    select('select id_player, nome, check_in from player order by id_player asc')
    confirmacao = False
    while confirmacao == False:
        
        try:
            player = int(input('Digite o Id do player: '))
            check_in = float(input('Digite o novo valor: '))
            sql = f'UPDATE player SET check_in = {check_in} WHERE id_player = {player}'
            confirmacao_1 = str(input(f'''Confirmação dos valores:
    
    {sql} 

    está correto? 1 para "sim" e qualquer valor para "não". '''))
            
            if confirmacao_1 == '1':
                confirmacao = True
            
                try:
                    pd.read_sql_query(sql, con=engine)
            
                except:
                    pass
        
        except ValueError:
            print('\nO valor não corresponde. Tente novamente')

    return