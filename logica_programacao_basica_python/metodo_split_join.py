'''
split e join com list e str
split - divive uma string
join - une uma string
'''



frase = '     Olha,      que coisa mais,             interessante!'
# lista_palavras = frase.split() #Sem argumentos ele separa por espacos em branco
lista_palavras_crua = frase.split(', ') #Com argumentos ele separa pelo caracter escolhido

#Agora apresentando o strip em uma string
#Nesse caso o strip retira os espacos em branco do comeco e do fim da string
#temos o r(igth)strip e o l(eft)strip que como o nome ja diz retira a esquerda e a direita da string
lista_palavras_refinadas = []

for i, frase in enumerate(lista_palavras_crua):
     lista_palavras_refinadas.append(lista_palavras_crua[i].strip())

# print(lista_palavras_crua)
# print(lista_palavras_refinadas)

frases_unidas = '-'.join(lista_palavras_refinadas) #O join funciona assim, e funciona apenas com iteraveis, ou seja listas, strings e tuplas
print(frases_unidas)
