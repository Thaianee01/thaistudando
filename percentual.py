#Faça um programa em Python que leia 10 números reais (do tipo float) e informe o percentual de números positivos e o percentual de números negativos lidos.

import math

positivos = 0
negativos = 0
numero = 0


for cont in range (10):
    numero = float(input("digite o numero = "))
    if numero > 0:
        positivos = positivos +1
    if numero <0:
        negativos = negativos +1


percentagemp = (positivos/10) * 100
percentagemn = (negativos/10) * 100


print(f'percentagem de numeros positivos = {percentagemp:.0f}%')
print(f'percentagem de numeros negativos = {percentagemn:.0f}%')