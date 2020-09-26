import random
nomes = []
for conta in range(0,5):
    nomes.insert(conta,str(input('Digite o nome do aluno numero {}:'.format(conta))))
print('E o nome selecionado é... \n {}'.format(nomes[random.randint(0,5)]))
