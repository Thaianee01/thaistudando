#Faça um programa em Python que leia o comprimento dos lados de um triângulo retângulo (B e C), e calcule e imprima o comprimento da sua hipotenusa A.#

import math

lado_B = int(input("comprimento B de um triangulo = "))
lado_C = int(input("comprimento A de um triangulo =")) 

hipotenusa = lado_B**2 + lado_C**2
raiz = math.sqrt(hipotenusa)
print (f'hipotenusa = {raiz}')