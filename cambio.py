# Uma casa de câmbio vende diferentes moedas para brasileiros que desejam viajar para o exterior. O cliente informa a moeda desejada e dá um valor em reais para a compra. O operador do caixa acessa o sistema, informa a letra inicial da moeda a ser comprada, entra com o valor a ser convertido e o sistema informa o valor de conversão para a nova moeda. Faça um programa em Python que simula o sistema da casa de câmbio. #

import math
moeda = input("digite a moeda (E,D,M,A,F) =")
dinheiro = float(input("digite o valor em reais = "))

if moeda == 'E':
    taxa = 0.18

elif moeda == 'D':
    taxa = 0.19

elif moeda == 'M':
    taxa = 5.13
    
elif moeda == 'A':
    taxa = 40.43

elif moeda == 'F':
    taxa = 0.17

converção = dinheiro * taxa

print(f'valor convertido = {converção:.2f}')