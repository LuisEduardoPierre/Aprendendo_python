'''
Higher Order Functions
Funcoes de primeira classe
'''

def saudacao(msg):
    return msg

#Olha que curioso, as variaveis estao no mesmo nivel hierarquico em python, junto com os tipos primitivos
#Portanto podemos atribuir a uma variavel o espaco de memoria referente a uma determinada funcao se usarmos apenas
#o seu nome sem o uso de parenteses () 
saudacao_2 = saudacao

v = saudacao_2('Bom dia')

#Podemos passar funcoes como parametros para a execucao de uma funcao
#Como pode ser observado no exemplo a seguir
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Pierre')
    )
#Como foi citado mais acima, podemos passar a referencia de memoria de uma funcao para uma outra funcao em python
#Que nesse caso seria uma "Variavel" ou um argumento da funcao.
# Quando chamamos a saudacao em executa, estamos nos referindo ao espaco de memoria onde foi alocado saudacao
# e como passamos o endereco de memoria dessa funcao, podemos executala em outro lugar, que nesse caso e uma funcao
#a funcao nesse caso recebe um *args, com varios argumentos, que por sua vez envia de volta para saudacao(msg,nome)
#E ao final de tudo o valor retornado vai saindo da pilha de chamadas ate chegar no print que esta na tela, entao o fluxo seria
#executa(saudacao *args) -> funcao(*args) -> saudacao(msg,nome) -> executa(valor_retornado:'Bom dia, Luis') -> print('Bom dia, Luis)
