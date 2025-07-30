'''
Metodos uteis dos dicionarios em python
Len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com as chaves e valores
setdefault - adiciona o valor se a chave nao existe
copy - retorna uma copia rasa
get - obtem uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o ultimo item adicionado
update - Atualiza um dicionario com outro

TODOS OS ITENS EM PYTHON SAO OBJETOS
'''

pessoa = {
'nome': 'Luis Eduardo',
'sobrenome': 'Souza Pierre',
}

print(len(pessoa))
#Podemos fazer coercao de dados com os resultados dos metodos de dict
print(list(pessoa.keys()))


for chave in pessoa.keys():
    print(chave)