from modulos.utils import *


if __name__ == '__main__':

    query()

    #Função que confirmará se o usuário ainda quer se manter no programa
    def query_adicional(repeticao =True):
        try:
            confirmacao = int(input('\nDeseja fazer mais alguma ação? Digite 1 para "sim" e 0 "não": '))
            if confirmacao == 1:
                repeticao = True

            elif confirmacao == 0:
                repeticao = False
                print('\nFim de Conexão. Bem sucessidida.\n')
                
            else:
                repeticao = False

        except ValueError:
            print('\nO valor não corresponde. Tente novamente!')
        return repeticao

while query_adicional() == True:
    query()    

