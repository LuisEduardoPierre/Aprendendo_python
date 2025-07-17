#Condicionais em python
#if/elif/else

entrada = input('Quer entrar ou sair do codigo?')

#Bem simples a principio, funciona como as condicionais de outras linguagens
#O if pode existir sem o elif e sem o else, mas nunca ao contrario, os outros dois dependendo do if pra existir
if entrada == 'entrar':
    print('voce entrou no sistema de cadastro')
elif entrada == 'sair':
    print('voce saiu do sistema de cadastro')
else:
    print('Voce nao informou a opcao correta')