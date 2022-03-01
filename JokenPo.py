#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('\033[1;30;45m{:=^40}\033[m'.format('JOKENPO'))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


print('''\n Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\nEscolha uma opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou{}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #jogou peda
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('jogada invalida')
elif computador == 1: #jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
    else:
        print('jogada invalida')
elif computador == 2: #jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
