#Atividade para reforco

nome = input('Digite seu nome: ')
idade = input('Agora digite sua idade: ') or 0
idade = int(idade)
print()

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espacos')
    else:
        print(f'Seu nome NAO contem espacos')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print(f'Desculpe, voce deixou campos vazios')