#crie um jogo que faça o computador pensar em um jogo de 0 a 5
#usuario tem que adivinhar, avisando se ganhou ou não

from random import randint
from time import sleep

computador = randint(0, 10) #faz o computador sortear o numero
print('-+-' * 20)
print('Vou pensar em um número entre 0 a 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('\nEm que número eu pensei? ')) #jogador tenta adivinhar
    palpite += 1
    if jogador == computador:
       acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('\nACERTOU!!! com {} tentativas'.format(palpite))
