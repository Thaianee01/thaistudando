#Faça um programa em Python que leia, inicialmente, a quantidade de números inteiros que serão digitados. Em seguida, o programa deve ler cada um dos números e ao final apresentar a média deles. #

import math

total = int(input("Digite a quantidade de numeros = "))

soma = 0

for i in range(total):
    numero = int(input("numero = "))
    soma += numero

media = soma / total
print(f'Media = {media:.2f}')