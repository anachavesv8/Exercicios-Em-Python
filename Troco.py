# Qual o valor do troco?
# Defina uma variável para o valor de uma compra que custou R$100,98;
# Defina uma variável para o valor que o cliente pagou R$150,00;
# Defina uma variável que calcula o valor do troco e exiba-o no console com o valor final arredondado.

compra = 100.98
dinheiro = 150.00
troco = dinheiro - compra
troco1 = round(troco, 2)
print('O seu troco é R$ ', troco1)