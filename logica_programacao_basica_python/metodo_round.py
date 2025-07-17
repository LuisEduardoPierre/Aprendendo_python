'''Tratando imprecisao de ponto flutuante'''


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
#A funcao round faz a atividade mostrada acima so que com um metodo especifico, que mantem a tipagem do numero como float ao inves
#de transformar e retornar uma string
#     variavel float, quantidade de casas decimais
print(round(numero_3,1))

#Ou posso usar uma classe do modulo Decimal
import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2

print(numero_3)

