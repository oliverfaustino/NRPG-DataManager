import pandas as pd
from modulos.conecao import *
import pyperclip

def copiar(item):
    try:
        item_copiar = int(input('\nDeseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
        if item_copiar == 1:
            item_copiado = pyperclip.copy(item)
            print('\nCopiado com sucesso!')
        else:
            pass

    except ValueError:
        pass
    return item_copiado     

def select(sql):
    try:
        df = str(pd.read_sql_query(sql, con=engine))
        if sql == 'select nome FROM pp ORDER BY nome ASC;':
            sistema_nome = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ B̶a̶s̶e̶s̶  ° -🚻』

       →: O que são "Nomes de PP"?

Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem os Nomes de PPs. Os Nomes de PPs, são simplesmente os nomes que damos aos nossos personagens. Abaixo estará listado os nomes ocupados:

{df}'''
        print(sistema_nome)
        copiar(sistema_nome) 

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
