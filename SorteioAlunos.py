#Um prof quer sotear um dos segus 4 alunos para apagar o quadro
#faca um programa que ajude ele, lendo o nome deles e escrevendo o nome sorteado.

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))