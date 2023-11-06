import math

x = int(input("digite a posicao do numero de Fibonacci = "))

numero_atual = 1
numero_anterior = 1

if x==1 or x==2:
    print (f'numero de Fibonacci = {numero_atual}')
    
else:
    for cont in range (3, x +1):
        proximo_numero = numero_atual + numero_anterior
        numero_anterior = numero_atual
        numero_atual = proximo_numero
    print (f'numero de Fibonacci = {numero_atual}')