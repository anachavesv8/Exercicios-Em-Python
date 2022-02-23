#programa de aluguel de carro, quantos dias e quantos km, sendo R$60 por dia, e R$0,15 por km
dias = int(input("Quantos dias o carro foi utilizado? "))
km = float(input('Quantos KM foram rodadeos?'))

dias1 = dias * 60.00
km1 = km * 0.15
soma = dias1 + km1

print('O total a pagar é R${}'.format(soma))