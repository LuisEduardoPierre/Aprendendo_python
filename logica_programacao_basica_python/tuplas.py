'''
Introducao a tuplas e desempacotamento

'''

#Desempacotamento

# nomes = ['Maria','Jose','Felipe']

# nome1,nom2,nome3 = nomes #O desempacotamento ocorre quando voce pega os elementos de uma lista e reatribui eles a outras variaveis
# #No entanto o numero de variaveis deve ser o mesmo que o numero de elementos
# # Se eu quiser guardar apenas um elemento da lista devo criar uma variavel de resto para que os outros valores possam ser reempacotados

# desempacota_1, *resto = ['Paulo','Pedro','Joaquim']
# print(desempacota_1)
# #Mas e o resto? Nesse caso ele armazena os elementos restantes
# print(resto)
# #posso pular mais elementos a medida que acrescento mais underlines a declaracao
# _,_,desempacota_2, *_ = ['Saulo','Fabio','Messias']
# print(desempacota_2)

#Tuplas

#Tuplas sao listas imutaveis
#Podem ser declaradas de duas formas distintas

tupla_1 = 'Marcos','Pierre','Samara'
#ou
tupla_2 = ('Larissa','Douglas','Kauan')
print(tupla_1)
print(tupla_2)
#Eh possivel fazer a coercao de tipos para tupla, nesse caso da LISTA para a TUPLA e o inverso tambem
tuple(nomes)
