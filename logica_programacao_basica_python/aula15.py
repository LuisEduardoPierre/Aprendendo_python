#sozinha essa funcao nao faz nada
#
#Agora quando voce utiliza uma variavel ela armazena o valor
nome = input('Qual seu nome?')
print(f'O nome dele e {nome}')

#O input SEMPRE recebe uma string
numero = input('Digite um numero')
print(type(numero))

#Por isso e necessario sempre fazer a conversao de tipos
#Nao e recomendado voce fazer o casting dessa forma, existe um jeito melhor que sera apresentado no futuro
numero2 = int(input('Digite outro numero'))
print(type(numero2))

#Dessa forma e mais seguro
numero3=input('Digite outro numero')
converte_para_int = int(numero3)
print(type(numero3))