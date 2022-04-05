# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.,


while True:
    r = int(input('Digite um valor para ver a tabuada: '))
    if r < 0:
        break
    print('-=' * 12)
    for c in range(1, 11):
        print(f'{r} x{c} = {r*c}')
    print('-=' * 12)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE')
