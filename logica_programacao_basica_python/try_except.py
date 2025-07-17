'''

Aprendendo o try/except
try -> tentar executar o codigo
except(catch em outras linguagens) -> captura a excecao de codigo

'''

numero = input('Vou dobrar o numero que voce digitar: ')


#Checa se o input e um numero e caso ele seja ele termina a execucao, mas se der erro ele pula para o except e mostra o erro na tela
try:
    numero_float = float(numero)
    print(f'o dobro de {numero} e {numero_float * 2}')
except:
    print('Isso nao e um numero')