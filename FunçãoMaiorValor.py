# Faça um programa que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros. Seu programa tem que
# analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'o maior valor informado foi {maior}.')

maior(2, 5, 9, 56, 100, 21, 87, 5)
