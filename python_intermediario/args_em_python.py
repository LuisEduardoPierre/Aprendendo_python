'''
args - Argumentos nao nomeados
* - *args (empacotamento de desempacotamento)
'''

#Lembrar sempre do desempacotamento
x,y,*resto = 1,2,3,4
print(x,y,resto)


def soma(x,y):
    return x + y

#*args e um parametro coringa que pode receber de forma indefinida varios argumentos NAO NOMEADOS
#E ele sempre vai empacotar os dados recebidos em uma TUPLA, que pode ser convertida em lista usando type coersion
def soma2(*args):
    args = list(args)
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total
#Este soma realizado acima pode ser feito dessa forma ou utilizando a funcao sum() que tem o mesmo objetivo
#Da forma acima e boa para treinar a logica, mas se precisar fazer algo mais enxuto temos a funcao citada


total2 = soma2(1,2,3,4,5,6)
print(total2)