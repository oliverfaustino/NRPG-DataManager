import pyperclip
import pandas as pd

from modulos.conecao import *
def copiar(objeto): # função para copiar os objetos para área de transferência
    global copiar # para resolver o porblema UnboundLocalError: local variable 'copiar' referenced before assignment:
    opcao = int(input('Deseja copiar para área de transferência? "1" para sim e qualquer tecla para não\n\nR: '))                  
    if opcao == 1:
        copiar = pyperclip.copy(objeto)
        print('\nCopiado com sucesso!')            
    else:
        pass
    return copiar




def select(sql):  # função que decta qual tipo de ação eu desejo fazer
    try:
        df = pd.read_sql_query(sql, con=engine).to_string(index=False)
    
    finally:
        pass

    return df
