#Faça um programa em Python que leia um número inteiro e imprima uma mensagem indicando se é par ou ímpar e também se é positivo ou negativo. Considere que o número zero é par, mas não é nem positivo nem negativo.#

numero = int(input("digite um numero qualquer = "))

if numero == 0:
    print("par")
    
elif numero % 2 == 0:
    print("par")
    
else:
    print("ímpar")

if numero > 0:
    print("positivo")
    
elif numero < 0:
    print("negativo")