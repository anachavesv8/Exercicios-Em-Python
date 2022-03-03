# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
#
# APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() #separar as palavras
junto = ''.join(palavra) #juntas as palavras sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O Inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO É PALINDROMO')

print('Você digitou a frase {}'.format(junto))


