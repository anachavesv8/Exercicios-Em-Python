# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

tot = 0
tot1 = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu?: '.format(c)))
    maior = date.today().year - ano
    if maior >= 21:
        tot += 1
    else:
        tot1 +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tot))
print('E também tivemosd {} pessoas menores de idade'.format(tot1))
