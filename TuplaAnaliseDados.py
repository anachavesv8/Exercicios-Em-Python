# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

a = (int(input('Digite 1º numero: ')), int(input('Digite 2º numero: ')),
     int(input('Digite 3º numero: ')), int(input('Digite 4º numero: ')))
print(f'Voce digitou os valores {a}')
print(f'O valor 9 apareceu {a.count(9)} vezes')
if 3 in a:
    print(f'O valor 3 apareceu na {a.index(3)+1}ª posição')
else:
    print('Os valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares digitadores foram ', end='')
for n in a:
    if n % 2 == 0:
        print(n, end=', ')
