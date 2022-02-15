import pandas as pd
from sqlalchemy import create_engine
import pyperclip

engine = create_engine('postgresql://postgres:160587pvcdacr4sh-pvCr4sh_PV@localhost:5432/nrpg_revolution')

def select(sql):
    try:
        df = str(pd.read_sql_query(sql, con=engine))
        print(df)
        try:
            copiar = int(input('\nDeseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
            if copiar == 1:
                pyperclip.copy(df)
                print('\nCopiado com sucesso!')
            else:
                pass

        except ValueError:
            pass
    finally:
        pass
    return df
def select_simples(sql):
    try:
        df = str(pd.read_sql_query(sql, con=engine))
        print(df)
    finally:
        pass
    return df

def ficha():
    ficha = print('''
''')
    
    try:
        copiar = int(input('\nDeseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
        if copiar == 1:
            pyperclip.copy(ficha)
            print('\nCopiado com sucesso!')
        
        else:
            pass
        
    except ValueError:
        pass