#Exercicios de condicionais

primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

#O condicional and, avalia as varaiveis de comparacao e retorna a expressao verdadeira ou em caso de falso a primeira condicao que representa
#um valor falso
converte_primeiro_valor = int(primeiro_valor)
converte_segundo_valor = int(segundo_valor)

if converte_primeiro_valor > converte_segundo_valor:
    print(f'O {primeiro_valor=} e maior que o {segundo_valor=}')
elif converte_segundo_valor > converte_primeiro_valor:
    print(f'O {segundo_valor=} e maior que o {primeiro_valor=}')
else:
    print(f'Os dois valores sao iguais {primeiro_valor} = {segundo_valor}')

#O condicional or, avalia a primeira condicao verdadeira da expressao e a retorna
#exemplo

verdadeiro = input('nao false') or 'false'
print(verdadeiro)