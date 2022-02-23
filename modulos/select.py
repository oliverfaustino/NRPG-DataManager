import pandas as pd
from modulos.conecao import *
import pyperclip

def copiar(objeto):
    try:
        objeto_copiar = int(input('\nDeseja copiar para área de transferência? "1" para sim e qualquer tecla para não: '))
        if objeto_copiar == 1:
            objeto_copiado = pyperclip.copy(objeto)
            print('\nCopiado com sucesso!')
        else:
            pass

    except ValueError:
        pass
    return objeto_copiado     

def sistema_nome(df):
    sistema_nome = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ N̶o̶m̶e̶s̶  ° -🚻』

       →: O que são "Nomes de PP"?

Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem os Nomes de PPs. Os Nomes de PPs, são simplesmente os nomes que damos aos nossos personagens. Abaixo estará listado os nomes ocupados:

{df}'''
    print(sistema_nome)
    copiar(sistema_nome)
    return

def sistema_aparencia(df):
    sistema_aparencia = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ A̶p̶a̶r̶ê̶n̶c̶i̶a̶  ° -🚻』

       →: O que é "Aparência"?

Como devem saber, o RPG é de criação, onde fazemos do 0 nossos personagens. Nisso vem as aparências personalizadas. As aparências, são simplesmente o visual que escolhemos para nossos personagens. Ser aparência do madara, te dá apenas aquele visual e não seus poderes! Seja coerente nas escolhas, pois determinados clãs têm uma característica única de aparência, respeite-as! Abaixo estará listado os aparências ocupadas:

{df}'''
    print(sistema_aparencia)
    copiar(sistema_aparencia)
    return

#

def sistema_registro_ninja(df):
    sistema_registro_ninja = f'''🚻- °  S̶i̶s̶t̶e̶m̶a̶ d̶e̶ R̶e̶g̶i̶s̶t̶r̶o̶ N̶i̶n̶j̶a̶  ° -🚻』

       →: O que é "Registro Ninja"?

Baseado no sistema de banco, onde cada ninja tem seu cartão e identificação *(leiam o sistema /banco para entender melhor)* Nisso vem os registros ninjas personalizados. Os registros, são simplesmente o uma combinação única de 6 números, seja ela qual for. Lembre-se de sua combinação não pode começar com 0. Abaixo estará listado os registros ninjas ocupados:

{df}'''

    print(sistema_registro_ninja)
    copiar(sistema_registro_ninja)
    return

#

def select(sql):
    try:
        df = str(pd.read_sql_query(sql, con=engine))

        try:
            if sql == 'select nome FROM pp ORDER BY nome ASC;':
                sistema_nome(df)

            elif sql == 'select aparencia FROM pp ORDER BY aparencia ASC;':
                sistema_aparencia(df)

            elif sql == 'select registro_ninja from pp order by registro_ninja asc':
                sistema_registro_ninja(df)
        except:
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
