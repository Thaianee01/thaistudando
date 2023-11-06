#Faça um programa em Python que leia a idade de uma pessoa expressa em dias e informe a quantidade correspondente de anos, meses e dias. Quando o programa imprime "total de dias vividos = ", o usuário deve entrar com o número de dias vividos pela pessoa. Então o programa deve imprimir a quantidade de anos, de meses e de dias correspondente ao total de dias que a pessoa já viveu, seguindo os exemplos a seguir. Considere que todos os anos tem 365 dias e que todos os meses tem 30 dias.#

import math
total_dias = (int(input("total de dias vividos = ")))
anos = (total_dias// 365)                # // divisão inteira
meses = (total_dias % 365) // 30         # % resto da divisão
dias = (total_dias % 365) % 30          

print(f'anos = {anos}')
print (f"meses = {meses}")
print (f"dias = {dias}")