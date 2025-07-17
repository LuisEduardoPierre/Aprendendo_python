'''
Interpolacao de strings
Funciona basicamente de forma semelhante ao que aconteceria em C
s- string
d e i - int
f - float
x e X - Hexadecimal (pouco usado)

'''

#Pode ser feito dessa forma
nome = 'Luis'
preco = 100.2324324
variavel = '%s, o preco total foi %.2f' % (nome, preco)
print(variavel)

#Ou dessa forma
print('%s voce me deve %.2f' % (nome,preco))
