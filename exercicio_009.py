#Faça um programa em Python que leia 2 números float e um operador aritmético (+, -, *, /) e informe o resultado da operação sob os dois números.#

import math

X = float(input("operando 1 = "))
operação = input ("operador (+,-,*,/) = ")
Y = float(input("operando 2 ="))

if operação == "+" :
    valor = X + Y
    print (f'resultado = {valor :.2f}')

elif operação == "-" :
    valor = X - Y
    print (f'resultado = {valor :.2f}')

elif operação == "*" :
    valor = X * Y
    print (f'resultado = {valor :.2f}')

elif operação == "/" :
    valor = X / Y
    print (f'resultado = {valor :.2f}')

else:
    print ("operador inválido")