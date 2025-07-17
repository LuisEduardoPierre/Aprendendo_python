#Aprendendo formatacao de strings

#fstrings

nome = 'Jusenildes'
nome2 = 'Edson'
idade = 57
altura = 1.80
texto = f'{nome} e uma mae muito perfeita e tem {idade} anos, e {nome2} e um pai excelente e tem {altura:.2f} de altura '
print(texto)

#Utilizando o metodo format
a = 'aaaaaaaa'
b = 'B'
c = 1.1
#a formatacao de baixo pode ser pega por indices
string = 'a={} b={} c={}'.format(a,b,c)
string2 = 'a={1} b={0} c={2}'.format(a,b,c)
#podemos nomear tbm as variaveis, mas se nomearmos um parametro devemos nomear todos os outros
string3 = 'a={1} b={0} c={2}'.format(nome1=a,nome2=b,nome3=c)
print(string,string2)