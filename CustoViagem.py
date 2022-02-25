#Crie um programa pergunte a distancia de uma viagem em km
#calcule o preço da passagem, cobrando R$0.50 po km para viagens de ate 200km
# e R$0.45 para viagens mais longas

km = float(input("Qual a distancia da viagem? em KM: "))
print('Você está prestes a começar uma viagem de {}km'.format(km))

if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print('O valor da Viagem vai custar R${:.2f}'.format(valor))