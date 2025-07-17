'''Retorno dos valores das funcoes'''

#O retorno da MAIORIA das variaveis em Python e None
#Como mostrado no exemplo
variavel = print('Luis')
print(variavel)

#Para que as funcoes retornem os valores que entram em suas chamadas precisamos usar a palavra chave return
#Qualquer coisa chamada APOS o return nao e executado, porque o return retorna para a execucao do programa principal
#Ou seja ele tem duas funcoes, tem a funcao de retornar valores e de simultaneamente retornar ao codigo principal

def soma(x,y):
    return x + y

soma1 = soma(2,2)
soma2 = soma(3,3)

#Apenas consegui exibir a soma dessas variaveis porque o return retornou os valores que foram inseridos na funcao

print(soma1 + soma2)

