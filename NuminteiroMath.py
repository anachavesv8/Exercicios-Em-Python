#Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porçao inteira.

#utilizando biblioteca:

#from math import trunc

# import math
# num =  float(input('Digite um valor: '))
# print('O Valor digitado foi {} e a sua porçao inteira é {}'.format(num, math.trunc(num)))


#utilizando sem biblioteca

num = float(input('Digite um valor: '))
print('O Valor digitado foi {} e a sua porçao inteira é {}'.format(num, int(num)))