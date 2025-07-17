'''
Calculadora com while
'''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite a operacao desejada (+-/*):  ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos numeros digitados sao invalidos')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
            print(num_1_float * num_2_float)
    else:
        print('nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s') #Esse poderia ser inserido na linha acima

    if sair is True:
        break

