#Faça um programa em Python que leia um valor inteiro que representa o comprimento de um lado de um quadrado e imprima a area e o comprimento da diagonal deste quadrado. Lembre que diagonal² = lado² + lado². Quando o programa imprime "lado = ", o usuario deve entrar com o valor do lado do quadrado. Entao o programa deve imprimir a area e o comprimento da diagonal, com duas casas decimais, seguindo os exemplos a seguir.#

import math
L = int(input("lado ="))
a = L * L
print(f'area = {a:.2f}')

diagonal = L**2 + L**2
raiz = math.sqrt(diagonal)
print(f'diagonal = {raiz:.2f}')