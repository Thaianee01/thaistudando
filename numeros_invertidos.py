#Faça um programa em Python que leia um número inteiro, que deve estar entre 100 e 999, e exiba o mesmo de forma invertida, um dígito por linha da tela#

import math

numero = int(input("digite um numero de 000 999 = "))
digito = numero//100
digito_02 = (numero % 100) // 10
digito_03 = (numero % 100) % 10

print (digito)
print (digito_02)
print (digito_03)