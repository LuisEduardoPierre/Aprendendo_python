'''
Funcao que multiplica todos os argumentos
nao nomeados recebidos
retorne o total para uma variavel e mostre o valor
da variavel

Crie uma funcao que retorna se o numero e par ou impar
'''


def multiplicacao(*args):
    total = 1
    for mult in args:
        total *= mult
    return total

result = multiplicacao(1,2,3,4,5)
print(result)
print(1*2*3*4*5)


def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Impar'
    
par_ou_impar = par_ou_impar(2)
print(par_ou_impar)