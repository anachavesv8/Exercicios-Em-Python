#Crie um programa que leia o nome completo da pessoa, mostrando o primeiro e ultimo nome.

n = str(input('Qual seu nome completo? ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))