'''
Funcoes que retornam, outras funcoes em python se chama closure
'''

#Closure e uma definicao importante que auxilia programadores a criarem dinamicamente novas funcoes a partir
#de uma funcao existente, isso significa que os resultados esperados de uma determinada funcao podem mudar de acordo com
#a necessidade de cada caso de aplicacao para cada funcao, fica confuso so escrever dessa forma portanto vamos ao exemplo


def criar_saudacao(saudacao):
    def saudar(nome_pessoa):
        return f'{saudacao}, {nome_pessoa}!'
    return saudar

#A funcao acima mostra um exemplo perfeito de closure, temos uma funcao que nao retorna um valor fixo, necessitando que todas as vezes
#A chamemos de forma regular, podemos simplesmente chamala da seguinte forma

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

#Dessa forma colocamos por padrao na memoria assim que as variaveis sao criadas o 'Bom dia' e o 'Boa noite'
#Isso ocorre porque o python precisa resolver as funcoes antes de continuar a execucao normal do programa
#Ou seja ele resolve parcialmente, ate que a chamemos novamente, dessa vez pelo nome das variaveis que criamos
print(falar_bom_dia('Luis'))
print(falar_boa_noite('Luis'))
#Isso possibilita que criemos resultados diferentes pela chamada da mesma funcao com valores diferentes
#resumindo, a closure seria a preparacao da funcao para uso futuro construindo sempre que precisarmos de resultados diferentes em 
#situacoes diferentes, pode ser comparado ao padrao de projeto strategy, que aplica esse tipo de paradigma para resolver problemas
#de codigo recorrentes, mas com resultados diferentes