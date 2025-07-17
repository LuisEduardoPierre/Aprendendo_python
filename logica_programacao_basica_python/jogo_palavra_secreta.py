
import os 
PALAVRA_SECRETA = 'Perfume'
letras_acertadas = ''
tentativas = 0

while True:

    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra: ')
        continue #Continue pula uma execucao do laco e retorna para o comeco do mesmo

    if letra_digitada in PALAVRA_SECRETA:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in PALAVRA_SECRETA:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada {palavra_formada}')

    if palavra_formada == PALAVRA_SECRETA:
        os.system('cls')
        print('Voce venceu Yay')
        print('A palavra era', palavra_formada)
        print('Tentativas: ', tentativas)
        letras_acertadas = ''
        tentativas = 0
        break
    
    


