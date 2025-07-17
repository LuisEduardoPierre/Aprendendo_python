'''
listas em python
Tipo list - Mutavel
Suporta varios valores variados
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis, append, insert, pop, del, clear, extend, +
'''


lista = [123, True, 'Luis Eduardo', 1.2, []]
lista_2 = [10,20,30,40,50]
print(lista_2)
numero = lista_2[2]
print(lista_2)
lista_2.append('Banana') #Adiciona um elemento ao final da lista
lista_2.pop() #Retira um elemento ao final da lista, mas pode escolher onde voce quer remover o elemento, nao e recomendado fazer isso pois pode reduzir performance de codigo
del lista_2[2] #Deleta um item da lista
# lista_2.clear() #Limpa a lista inteira
lista_2.insert(0,5) #Insere um elemento no indice informado e empurra os outros elementos um indice a frente
print(lista_2)
lista_3 = lista + lista_2
lista.extend(lista_2) #Faz a mesma coisa que o metodo acima, com a diferenca que ele altera o objeto que chama a funcao que nesse caso e a variavel lista
print(lista_3)

