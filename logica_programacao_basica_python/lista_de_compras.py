''''Atividade da lista de compras'''
import os


lista_de_compras = []

while True:
    print('Selecione uma opcao: ')
    escolha = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if escolha == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_de_compras.append(valor)
    elif escolha == 'a':
        indice_apagar = input('Escolha o indice que sera apagado')

        try:
            indice_convertido = int(indice_apagar)
            del lista_de_compras[indice_convertido]
        except:
            print('Nao foi possivel apagar o indice, provavelmente porque ele nao existe na lista')
             
    elif escolha == 'l':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('Nao ha itens a serem listados ainda')
        else:
            #Ha duas formas de resolver esse problema, depende do que voce deseja
            #A primeira forma e esta, onde apenas mostro os itens de forma desordenada

            # print('Lista de itens armazenados: ')
            # for i in lista_de_compras:
            #     print(f'-{i}')

            #A segunda forma foi mostrada em aula, onde colocamos os valores do enumerate em duas variaveis distintas, gerando uma "lista ordenada"
            #por exemplo
            for i, valor in enumerate(lista_de_compras):
                print(i, valor)
    elif escolha == 's':
        print('Obrigado por gerar sua lista conosco, tenha um otimo dia!! :)')
        break;     
    else:
        print('Opcao incorreta, por favor insira i, a, ou l!!!')

        
