# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

valor = 0
continuar = 's'
soma = quant = 0
media = 0
while continuar in 'Ss':
    valor = int(input('Digite um número:'))
    soma += valor
    quant +=1
    if quant == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    continuar = str(input('Deseja continuar? [s/n] ')).upper().split()[0]
media = soma / quant
print('Você digitou {} números e a média é {:2f}'.format(quant, media))
print('O maior valor foi {} e o menor {}'.format(maior,menor))
