#EXERCICIO 2: Faça um programa em Python que leia diversos números inteiros quaisquer e ao final apresente o somatório e a média aritmética destes números. Antes da leitura de cada número o programa deve perguntar se deseja ler (mais) um número ('S' ou 'N'). Quando um 'N' for lido a leitura termina e as médias são exibida.

quantidade = 0
somatorio = 0

while True:
    n1 = int(input("Digite um numero:"))
    somatorio += n1
    quantidade += 1

    media = somatorio / quantidade
    proximo = input ("deseja ler mais um numero? (S/N)")
    
    if proximo == "N":
        print (f'media aritimetica = {media:.2f}')
        break

    if proximo == "S":
        continue