'''
Dicionarios em python (Tipo dict)
Dicionarios sao estruturas de dados do tipo par de chave e valor.
Chaves podem ser consideradas como "indice" que vimos na lista e podem ser tipos imutaveis
como str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionario
Usamos as chaves - {} - ou a classe dict para cirar dicionarios
Imutaveis: str, int, float, bool, tuple

Mutavel = dict, list
pessoa = {
'nome': 'Luis Eduardo',
'sobrenome': 'Souza Pierre',
'idade': 21,
'altura': 1.83,
'enderecos': [
{'rua': 35,'numero': 40},
{'rua':'Prazeres','numero':102}
]

'''
#Um dicionario pode ser criado dessa forma
pessoa = {
'nome': 'Luis Eduardo',
'sobrenome': 'Souza Pierre',
'idade': 21,
'altura': 1.83,
'enderecos': [
{'rua': 35,'numero': 40},
{'rua':'Prazeres','numero':102}
]
}

#Ou dessa forma, que e menos utilizada que a criada acima
# pessoa = dict(nome='Luis',sobrenome='Eduardo')

#Os dados de um dicionario sao acessados pelo chave associada a determinado valor
#Nesse caso acesso o valor altura, mas poderia acessar outros valores se precisasse, 
# apenas precisaria trocar o nome da chave que eu desejo acessar
print(pessoa['altura'])

#Podemos iterar sobre dicinarios, mas geralmente nao e necessario
for chave in pessoa:
    print(chave, pessoa[chave])