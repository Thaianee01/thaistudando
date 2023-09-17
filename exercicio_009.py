#Faça um programa em Python que leia as três notas de um aluno (números float). O programa deve calcular a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes seja 2. Imprima uma mensagem 'Aprovado' se a média for maior ou igual a 5.75 e 'Reprovado' se a média for menor que 5.75. #

n1 = float(input("nota 1 = "))
n2 = float(input("nota 2 = "))
n3 = float(input("nota 3 = "))

peso1 = 4
peso2 = 2
peso3 = 2

if n1 >= n2 and n1 >= n3:
    media_ponderada = (n1 * peso1 + n2 * peso2 + n3 * peso3) / (peso1 + peso2 + peso3)

elif n2 >= n1 and n2 >= n3:
    media_ponderada = (n2 * peso1 + n1 * peso2 + n3 * peso3) / (peso1 + peso2 + peso3)
else:
    media_ponderada = (n3 * peso1 + n2 * peso2 + n1 * peso3) / (peso1 + peso2 + peso3)
  

if media_ponderada >= 5.75:
    print("Aprovado")
else:
    print("Reprovado")