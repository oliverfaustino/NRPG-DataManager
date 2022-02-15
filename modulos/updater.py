import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:160587pvcdacr4sh-pvCr4sh_PV@localhost:5432/nrpg_revolution')



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
