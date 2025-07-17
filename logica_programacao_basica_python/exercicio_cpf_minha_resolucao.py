'''Calculando um cpf'''
import os
import random

'''912.766.280-21'''
NUMERO_MULTIPLICADOR = 10
LIMITE_DE_EXECUCAO = 10
NUMERO_PARA_ENCONTRAR_PRIMEIRO_DIGITO = 11
digitos_cpf = []
digitos_calculados = []
contador_numeros_cpf_1 = 1
somador_numeros_cpf = 0
primeiro_digito = 0
segundo_digito = 0
realiza_resto_primeiro_digito = 0
realiza_resto_segundo_digito = 0
index = 0

print('Informe os nove numeros do cpf para fazer o calculo do primeiro numero')


#Coleta os nove numeros para serem processados
while contador_numeros_cpf_1 < LIMITE_DE_EXECUCAO:
    digitos_cpf.append(random.randint(0,9))
    contador_numeros_cpf_1 += 1
    os.system('cls')

print(digitos_cpf)
    
while index in range(len(digitos_cpf)):

    multiplicador_numeros_cpf = digitos_cpf[index] * contador_numeros_cpf_1
    digitos_calculados.append(multiplicador_numeros_cpf)
    somador_numeros_cpf = somador_numeros_cpf + digitos_calculados[index]
    index += 1
    contador_numeros_cpf_1 -= 1
    
realiza_resto_primeiro_digito = (somador_numeros_cpf * NUMERO_MULTIPLICADOR) % NUMERO_PARA_ENCONTRAR_PRIMEIRO_DIGITO
primeiro_digito = realiza_resto_primeiro_digito if realiza_resto_primeiro_digito <= 9 else 0

digitos_cpf.append(primeiro_digito)
print(digitos_cpf)
#Calculando o segundo digito
index = 0
contador_numeros_cpf_2 = NUMERO_PARA_ENCONTRAR_PRIMEIRO_DIGITO
somador_numeros_cpf = 0
#Limpar lista para evitar duplicar os valores e da resultado discrepante
digitos_calculados.clear()

while index < NUMERO_PARA_ENCONTRAR_PRIMEIRO_DIGITO:

    multiplicador_numeros_cpf = digitos_cpf[index] * contador_numeros_cpf_2
    digitos_calculados.append(multiplicador_numeros_cpf)
    somador_numeros_cpf = somador_numeros_cpf + digitos_calculados[index]
    index += 1
    contador_numeros_cpf_2 -= 1
    print(multiplicador_numeros_cpf)
    if contador_numeros_cpf_2 == 1:
        break
print(somador_numeros_cpf)
realiza_resto_segundo_digito = (somador_numeros_cpf * NUMERO_MULTIPLICADOR) % NUMERO_PARA_ENCONTRAR_PRIMEIRO_DIGITO
segundo_digito = realiza_resto_segundo_digito if realiza_resto_segundo_digito <= 9 else 0

digitos_cpf.append(segundo_digito)

print(digitos_cpf)

