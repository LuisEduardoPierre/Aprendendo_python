'''
Aqui podemos usar a closure para exemplificar o aprendizado

Note que temos que criar funcoes que duplicam, triplicam e quadruplicam os valores recebidos por parametro
Qual a forma que vimos que podemos retornar diversos resultados utilizando apenas uma funcao?
A closure
Portanto o resultado seria assim...
'''
#Note que o exemplo da aula closure.py se encaixa perfeitamente nessa solucao
def multiplicador(multiplicador):
    def realizar_multiplicacao(numero):
        return multiplicador * numero
    return realizar_multiplicacao

#Definicao das variaveis de multiplicacao
dobra = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)

#Agora eu preciso chamar as variaveis defindas com esses valores, passando o numero que eu desejo que cada operacao resolva
print(dobra(2))
print(triplica(2))
print(quadruplica(2))
#Aqui tenho tres variaveis que podem ser reutilizadas e sempre poderao me entregar resultados diferentes com a chamada de apenas um funcao
