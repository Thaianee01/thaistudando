#Faça um programa em Python que leia, no máximo, 10 números inteiros positivos quaisquer e ao final apresente o somatório e a média aritmética destes números. Se desejar terminar antes da leitura dos 10 números, entre com o número zero. Caso nenhum número seja somado, não apresente a soma e a média.

numero = 0
soma = 0
numero_somado = False

for i in range (10):
    n1 = int(input("digite o numero ="))
    
    if n1 == 0:
        break
    
    if n1 > 0:
        soma += n1
        numero = numero + 1
        media = soma / numero
        numero_somado = True

if numero_somado:
    print(f"soma = {soma}")
    print(f"media = {media:.2f}")