#Faça um programa em Python que leia os 4 lados A, B, C e D de um quadrilátero (valores inteiros) e diga se o mesmo é um quadrado, um retângulo ou um quadrilátero qualquer. Considere que os lados A e C são opostos, bem como os lados B e D.#

A = int(input("lado A ="))
B = int(input("lado B ="))
C = int(input("lado C ="))
D = int(input("lado D ="))

if A == B == C == D:
    print ("Quadrado")

elif A==C and B==D:
    print ("Retângulo")

else:
    print ("Quadrilatero")