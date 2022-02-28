#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano =  int(input('Qual ano de nascimento? '))
print('''Escolha uma opção: 
[ 1 ] MASCULINO
[ 2 ] FEMININO
''')

sex =  int(input('Escolha uma opção acima: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))

if sex == 2:
    print('O sexo feminino não é obrigatorio o alistamento')
elif idade == 18 and sex == 1:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18 and sex == 1:
    saldo = 18 - idade
    print('Falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano.'.format(ano))
elif  idade > 18 and sex == 1:
    saldo = (idade - 18)
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}!'.format(ano))

