# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
import random
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!')
            v += 1
        else:
            print('Você Perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!!')
        else:
            print('Você Perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over!! VocÊ venceu {v} vezes!!')
