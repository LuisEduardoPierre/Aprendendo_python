'''
Flag - bandeira que marca o local de um acontecimento no codigo
None = Null de outras linguagens
is e is not - e ou nao e um tipo
id = endereco da identidade

'''

# v1 = 'b'
# v2 = 'b'
# print(id(v1))
# print(id(v2))



condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('fds')
else:
    print('n fds')

#Is e is not e muito utilizado com None retornando um boolean
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)