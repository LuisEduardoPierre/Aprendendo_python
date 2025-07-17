'''Argumentos nomeados
 e nao nomeados
 '''

def banana(fruta1='banana',fruta2='maca'):
    print(fruta1,fruta2)

#Argumentos nomeados possuem um = na frente do nome do argumento da funcao
#podemos fazer a chamada da funcao com parametros nomeados caso desejemos alterar a ordem de atribuicao

banana(fruta1='maca',fruta2='banana')