# Faça um programa que pergunte ao usuário um número e valide se o numero é par ou impar:
#Crie uma variável para receber o valor, com conversão para inteiro
#Para um número ser par, a divisão dele por 2 tem que dar resto 0

valor = int(input('Qual numero? '))
valor1 = valor %2

if valor1 == 0:
    print('Esta numero é par')
else:
    print('Este numero é impar')