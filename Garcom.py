# E os 10% do garçom?
# Defina uma variável para o valor de uma refeição que custou R$ 42,54;
# Defina uma variável para o valor da taxa de serviço que é de 10%;
# Defina uma variável que calcula o valor total da conta e exiba-o no console com essa formatação: R$ 9999.99.

qt = float(input("Quantas refeições? "))
print(qt)

pf = 42.54
tx = 0.10
total = pf * qt
taxa = total * tx
final = total + taxa

print("Sua conta deu um total de R$", final)