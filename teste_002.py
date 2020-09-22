import random

conta = 0
nomes = []
while (conta <= 5):
    nomes.insert(conta,str(input('Digite o nome do aluno numero {}:'.format(conta))));
    conta += 1

print('E o nome selecionado é... \n {}'.format(nomes[random.randint(0,6)]))


