#Faça um programa que peça dois números, imprima o maior deles ou imprima "Números iguais" se os números forem iguais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O número {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que {}.'.format(n2, n1))
else:
    print('Numéros iguais')