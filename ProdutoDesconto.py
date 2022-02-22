prod = float(input("Qual o preço do produto R$"))

des = prod - (prod * 0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(prod, des))