'''
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se esse numero e par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao e um numero inteiro
'''

# recebe_numero = input('Digite um numero inteiro: ')

# try:
#     converte_para_numero_inteiro = int(recebe_numero)
#     verifica_se_eh_numero_par = converte_para_numero_inteiro % 2
#     if verifica_se_eh_numero_par == 0:
#         print('O numero digitado e par')
#     else:
#         print('O numero digitado e impar')
# except:
#     print('O dado digitado nao e um numero inteiro, portanto nao sei dizer se e par ou impar')



'''
Faca um programa que pergunte a hora ao usuario e baseando-se no horario descrito, 
exiba a saudacao apropriada. EX.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
'''

# recebe_hora = input('Digite uma hora para que eu possa sauda-lo: ')

# try:
#     converte_hora_em_inteiro = int(recebe_hora)
#     eh_de_dia = converte_hora_em_inteiro >= 0 and converte_hora_em_inteiro <= 11
#     eh_de_tarde = converte_hora_em_inteiro >= 12 and converte_hora_em_inteiro <= 17
#     eh_de_noite = converte_hora_em_inteiro >= 18 and converte_hora_em_inteiro <= 23

#     if eh_de_dia:
#         print('Bom dia')
#     elif eh_de_tarde:
#         print('Boa tarde')
#     elif eh_de_noite:
#         print('Boa noite')
#     else:
#         print('A hora informada nao existe, nao posso sauda-lo')

# except:
#     print('O dado informado nao e uma hora valida')

'''
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva
"Seu nome e curto" se tiver entre 5 e 6 letras, escreva "Seu nome e normal" maior que 6 letras escreva
"Seu nome e muito grande"
'''

recebe_nome = input('Me diga seu nome para que eu o julgue: ')
nome_pequeno = len(recebe_nome) <= 4
nome_normal = len(recebe_nome) >= 5 and len(recebe_nome) <= 6 

if nome_pequeno:
    print('Seu nome e curto')
elif nome_normal:
    print('Seu nome e normal')
else:
    print('Seu nome e muito grande')
