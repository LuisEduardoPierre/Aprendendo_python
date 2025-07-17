frase = 'O python e uma linguagem de programacao multiparadigma. Python foi criado por Guido van Rossum'.lower()

i = 0
qtd_apareceu_mais_vezes =0
letra_que_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
           i += 1
           continue

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_mais_apareceu = letra_atual
    i += 1

print(f'A letra que mais apareceu foi {letra_que_mais_apareceu} apareceu {qtd_apareceu_mais_vezes} vezes')