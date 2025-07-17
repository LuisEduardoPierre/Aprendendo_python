'''
enumerate - enumera iteraveis (indices)

'''

lista = ['Maria','Jaum', 'Luix']
lista.append('Faubio')

lista_enumerada = enumerate(lista)
print(lista_enumerada)

#Podemos iterar diretamente a quantidade de itens da lista por meio do enumerate\
#Onde ele retorna o indice do elemento mais o elemento em si

for quant in lista_enumerada:
    print(quant)
