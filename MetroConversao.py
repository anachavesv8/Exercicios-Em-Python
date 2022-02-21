n = float(input('Digite um valor em metro: '))

km = n / 1000
centimetros = n * 100
milimetros = n * 1000

print('O valor de {} metros, convertido é {:.0f} cm e {:.0f} mm e {} em km'.format(n, centimetros, milimetros, km))