# Exercício Python 041: A Confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print('O atleta de {} anos'.format(idade))

if idade <= 9:
    print('CATEGORIA: Mirim')
elif idade <= 14:
    print('CATEGORIA: Infantil')
elif idade <= 19:
    print('CATEGORIA: Junior')
elif idade <= 25:
    print('CATEGORIA: Senior')
else:
    print('CATEGORIA: Master')

