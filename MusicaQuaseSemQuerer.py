# Faça um programa que mostre na tela uma letra de música que você gosta.

with open("letra.txt", "r") as arquivo:
    musica = arquivo.read()
print(musica)