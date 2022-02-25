#crie um jogo que faça o computador pensar em um jogo de 0 a 5
#usuario tem que adivinhar, avisando se ganhou ou não

from random import randint
from time import sleep

computador = randint(0, 5) #faz o computador sortear o numero
print('-+-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS!! Você conseguiu me vencer!')
else:
    print('GANHEI!!! Eu pensei no número {} e não no {}'.format(computador, jogador))