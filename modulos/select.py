import pandas as pd
from modulos.conecao import *
import pyperclip

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
