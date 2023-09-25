#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético `%`, que retorna o resto da divisão de dois números.

limite = int(input("Digite o numero limite que gostaria de saber se é primo:"))
 
lista = []

for numero in range(1, limite+1):
    r = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            r = r + 1
    if r == 2:
        lista.append(i)
print(lista)