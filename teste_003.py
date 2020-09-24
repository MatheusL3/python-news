nome = str(input('Digite seu nome completo: '))
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
print('Seu nome contem {} letras ao todo, e {} sem contar espaços'.format(len(nome), len(nome.replace(" ", ""))))
print('A quantidade de letras do primeiro nome é {}'.format(len(nome.split()[0])))
print('O primeiro e o ultimo nome é {} {}'.format(nome.split()[0],nome.split()[len(nome.split())-1]))
print('Seu nome tem Silva? {}'.format("SIM" if (('silva' in nome.lower()) == True) else "NÃO"))
if('silva' in nome.lower()) == True:
    print('seu nome tem Silva sim')
elif('lopes' in nome.lower()) == True:
    print("o seu nome tem Lopes")
else:
    print("seu nome não tem silva nem lopes")