#crie um programa que leia o nome completo de uma pessoa e mostre
#o nome com todas maiusculas
#o nome com todas Minusculas
#quantas letras ao todo sem considerar espaços
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print(nome.split())