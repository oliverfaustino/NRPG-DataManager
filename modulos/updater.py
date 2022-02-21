import pandas as pd
from modulos.conecao import *


# atualizar os invo
def atualizacao_invo(nome, id):
    invo_lista= str(pd.read_sql_query(f'select pp.nome from pp, invo where invo.id_invo = {id} and pp.id_pp = invo.id_pp_1 or pp.id_pp = invo.id_pp_2', con=engine))
    invo = f'{nome}: {invo_lista}'
    return invo

# atualizar os clãs
def atualizacao_cla(nome, limite):
    cla_lista = str(pd.read_sql_query('SELECT cla_1, cla_2 FROM pp;', con=engine))
    conta = cla_lista.count(nome)
    if conta > limite:
        print('Base lotada.')
        cla = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
    else:
        cla = f'{nome} ({conta}/{limite})'
    return cla
    
# atualizar as bases
def atualizacao_base(nome, limite):
    base_lista = str(pd.read_sql_query('SELECT base FROM pp;', con=engine))
    conta = base_lista.count(nome)
    if conta > limite:
        print('Base lotada.')
        base = f'{nome} (LIMITE ULTRAPASSADO!!! /{limite})'
        
    else:
        base = f'{nome} ({conta}/{limite})'
    return base
