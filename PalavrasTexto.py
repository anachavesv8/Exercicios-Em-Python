#crie um programa que leia o nome de uma cidade e diga
#se ela começa com o nome "santo" ou não.

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == "SANTO")