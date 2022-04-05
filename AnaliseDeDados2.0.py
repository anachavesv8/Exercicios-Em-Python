# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

tot18 = 0
toth = 0
totm = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual genero? [F/M]: ')).upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == "F" and idade < 20:
        totm += 1
    print('-'*20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [s/n]: ')).upper()[0]
    if resp == 'N':
        break
    print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'e Temos {totm} mulheres com menos de 20 anos')
