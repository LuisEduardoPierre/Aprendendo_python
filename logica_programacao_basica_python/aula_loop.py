'''
Repeticoes
While (enquanto)
Executa uma acao enquanto for verdadeira a condicao

operadores de Atribuicao

= += -= *= /= //= **= %=

Ps funciona com strings
'''
contador = 0

condicao = True

while contador <= 10 :
    contador += 1
    if contador == 4:
        continue #Esse operador pula uma execucao do codigo, nesse caso ele pula o numero 4 e continua a execucao do laco
    print(contador)

    break #Esse operador para a execucao completamente do loop
    
