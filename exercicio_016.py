#Faça um programa em Python que leia as 3 notas de um aluno (N1, N2 e N3) e imprima a média final deste aluno. Considere que a média é ponderada e que o peso de N1 é 2, o peso de N2 é 3, e o peso de N3 é 5#

import math
N1 = float(input ("digite a primeira nota = "))
N2 = float(input ("digite a segunda nota ="))
N3 = float(input ("digite a terceira nota = "))

Total = (N1*2 + N2*3 + N3*5)/ 10
print (f'Total = {Total:.2f}')