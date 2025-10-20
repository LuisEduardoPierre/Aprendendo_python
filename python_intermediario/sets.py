# UTILIZANDO SETS #

'''
Sets são conjuntos matemáticos e respeitam as regras e operações realizadas com conjuntos
Sua declaração é bem similar ao de dicts, no entando não usamos os pares chave valor
Apenas as chaves com os valores que desejamos armazenar
Os sets tem algumas peculiaridades, como, são iteraveis, 
NÃO garantem ordenação e podem armazenar qualquer tipo de dados (exceto valores considerados mutáveis como as listas e dicts)

'''

#Definição de um set vazio

s1 = set((5,6,7,8,9,1,2,3,4))
print(s1)

#Sets podem ser declarados de duas formas diferentes, sendo a primeira e a segunda forma como mostrada acima
s2 = {1,2,3,4,5}
print(s2, type(s2))

#Operadores manuais úteis
'''
União | União -  Une dois conjuntos
Intersecção & - Itens presentes em ambos conjuntos
Diferença - Itens presentes apenas no set da esquerda
Diferença simétrica ^ - Itens que não estão em ambos
'''

#União
s3 = s1 | s2
print(s3)

#Intersecção
s3 = s1 & s2
print(s3)

#Diferença
s3 = s1 - s2
print(s3)

#Diferença simétrica
s3 = s1 ^ s2
print(s3)



