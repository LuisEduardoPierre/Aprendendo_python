

from traceback import print_tb


pessoa = {}

#Na criacao de dicionarios podemos criar as chaves dinamicamente
#Seja utilizando de variaveis, ou utilizando de nomes hard coded ou seja fixos

chave = 'name'

pessoa[chave] = 'Banana'
pessoa['sobrenome'] = 'Nanica'


print(pessoa[chave])
print(pessoa['sobrenome'])

#Podemos inculsive alterar o dicionario dinamicamente
del pessoa['sobrenome']
print(pessoa)

#Ou seja, quando falamos de acoes que podemos fazer na estrutura de dados podemos basicamente fazer qualquer operacao de 
#CRUD - Create, Read, Update, Delete

#Caso a execucao de um programa fosse parada devido a uma excecao deveriamos tratar esse problema utilizando o metodo get()
##dessa forma

if pessoa.get('sobrenome') is None:
    
    print('nao existe sobrenome')
else:
    print(pessoa['sobrenome'])