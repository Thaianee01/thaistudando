#EXERCICIO 1: Faça um programa em Python que leia diversos números inteiros positivos quaisquer e ao final informe qual o maior número lido. Quando terminar de entrar com todos os números, entre com o número zero.#

anterior = 0
maior_numero = 0

while True:
    numero = int(input("numero ="))
    
    if numero == 0:
        break
    
    if numero > maior_numero:
        maior_numero = numero

print(f'maior numero: {maior_numero}')