sal = float(input("Qual salário do funcionario atual? R$"))
sal1 = sal + (sal * 0.15)
print('Seu salário atual é R${:.2f}, com aumento de 15%, será de R${:.2f}'.format(sal, sal1))