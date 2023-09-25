#Faça um programa em Python que leia um número N (número de termos de uma progressão aritmética), a1 (o primeiro termo da progressão) e R (a razão da progressão), e escreva os N termos desta progressão, bem como o somatório e o produto dos N termos. Considere que todos os números são inteiros positivos.#

import math

n = int(input("digite o numero de termos = "))
a1 = int(input("digite o primeiro termo = "))
razao = int(input("digite a razao da progressao = "))

termos = [] 

for i in range (n):
    termo = a1 + i * razao #termos gerais de uma p.a
    termos.append(termo)

print ("termos = ")
    
for termo in termos:
    print(termo)

soma = 0
somatorio = sum(termos)

produto = 1
for termo in termos:
    produto *= termo

print (f'somatorio = {somatorio}')
print (f'produto = {produto}')