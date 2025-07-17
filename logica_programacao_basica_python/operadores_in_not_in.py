#Aprendendo operadores in e not in
#strings em python sao iteraveis ou seja voce pode caminhar por esses dados com seus indices
# 0 1 2 3 
# L U I S

nome = 'Luis'

print(nome[2])

#O operador in verifica na string inteira se ela contem algo que o programador esteja procurando e retorna um booleano
print('L' in nome) #Retorno True

#O operador not in faz o contrario, verifica em toda a string iterando sobre ela se o valor existe e retorna um booleano
print('u' not in nome) #Retorno False