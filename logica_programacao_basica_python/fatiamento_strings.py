'''

Fatiamento de Strings
012345678
Ola Mundo
-987654321
Fatiamento [i:f:p] [::]
i = inicio(Pode ser omitido, ele comeca no indice 0 por padrao)
f = fim (Quando esse e omitido ele vai ate o fim da string por padrao)
p = passo ou seja de quanto em quanto deve ser fatiado a string
Obs.: a funcao len retorna a quantidade de caracteres na string

'''

#Exemplo de omissao de fim e inicio de string
variavel = 'Ola Mundo'
print(variavel[0:])
print(variavel[:9])

#Exemplo de contagem com len
print(len(variavel))

#Invertendo string com fatiamento
print(variavel[::-1])