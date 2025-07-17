'''
Funcoes em python sao trechos de codigo usados para replicar determinada acao ao longo do seu codigo
Elas podem receber valores para parametros (argumentos) e retornar um valor especifico
Por padrao funcoes python retornam None (ou simplesmente nao tem retorno)
'''

#Quando uma funcao possui parametros, para que ela possa funcionar voce PRECISA inserir os argumentos na chamada da funcao
#Caso contrario ela no executa o codigo por falta de argumentos
def imprimir(a, b, c):
    print('Varias')
    print('Varias2')
    print('Varias3')
    print('Varias4')

#Mas caso ela nao tenha, ela pode ser chamada sem nenhuma passagem de argumento
def Print():
    print('Varias')

#Aqui ele funciona
imprimir(1, 2, 3)
#Neste nao
# imprimir(1,2,3)

#Para usar o valores recebidos e bem facil
#basta utilizar eles na execucao da funcao
def usando_variaveis(a,b):
    print(a,b)

#dessa forma
usando_variaveis(1,2)
#E toda chamada pode ter valores diferentes
usando_variaveis(3,4)
usando_variaveis(5,6)

#Para evitar a situacao anterior de NAO EXECUCAO por falta de variaveis na funcao, podemos colocar um valor padrao
#caso os argumentos nao sejam passados

def fala_oi(nome='Leonardo'):
    print(f'Ola! seu nome e {nome} nao e?')

#Passando argumentos
fala_oi('Luis')
#Sem passagem de argumentos
fala_oi()

#Funciona da mesma forma, mas evita que a funcao nao seja executada por falta de parametros
#Ou quando voce deseja que uma variavel em uma funcao seja sempre a mesma coisa quando for executada
