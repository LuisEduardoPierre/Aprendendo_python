'''
Desempacotamento em chamadas de funcoes

'''

string = 'ABCD'
lista = ['Maria','Helena','Eduarda']
tupla = ('Python','e','legal')

#Isso aqui para a demonstacao de dados
for nome in lista:
    print(nome)

#E o mesmo nesse caso, pois o * DESEMPACOTA APENAS ITERAVEIS
#Lembrando que e possivel desempacotar variaveis com objetos e erros
print(*lista)