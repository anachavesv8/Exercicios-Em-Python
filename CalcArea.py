# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def terreno(larg, compr):
    area = larg * compr
    print(f'A area de um terreno {larg} x {compr} é de {area}')

larg = float(input('Largura do terreno: '))
compr = float(input('Comprimento do terreno'))
terreno(larg, compr)
