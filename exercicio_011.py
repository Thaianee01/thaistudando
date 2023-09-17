#Faça um programa em Python que leia 3 números inteiros positivos e diferentes entre si. Em seguida, o programa deve informar a média aritmética (“truncada”, ou seja, a parte inteira da média) dos mesmos. Informe também o primeiro número que está mais próximo do valor da média.#

import math

A = int(input("numero 1 = "))
B = int(input("numero 2 = "))
C = int(input("numero 3 = "))

if A >=0 and B>=0 and C >=0 and A!=B and B!=C and A!= C:
    Media = (A + B + C) // 3
    print ("media truncada = " , Media)

#numero mais proximo#
Resultado1 = abs (A - Media)
Resultado2 = abs (B - Media)
Resultado3 = abs (C - Media)

if Resultado1 <= Resultado2 and Resultado1 <= Resultado3:
    numero_proximo = A
    
elif Resultado2 <= Resultado1 and Resultado2 <= Resultado3:
    numero_proximo = B
    
else: 
    numero_proximo = C

print ("numero mais proximo da media = ", numero_proximo)