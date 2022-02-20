def cor (cor):
    cores = {'clear':"[m",
         'branco':'[30m',
         'vermelho':'[31m',
         'verde':'[32m',
         'amarelo':'[33m',
         'azul':'[34m',
         'roxo':'[35m',
         'ciano':'[36m',
         'cinza':'[37m',
         'fbranco': '[40m',
         'fvermelho': '[41m',
         'fverde': '[42m',
         'famarelo': '[43m',
         'fazul': '[44m',
         'froxo': '[45m',
         'fciano': '[46m',
         'fcinza': '[47m',
         'bold':'[1m',
         'underline':'[4m',
         'negative':'[7m'}
    cor = cores[f'{cor}']
    return cor