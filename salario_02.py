#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#1. Salário bruto.
#2. Quanto pagou ao INSS.
#3. Quanto pagou ao sindicato.
#4. O salário líquido.

import math
valor = float(input("Qual o valor da sua hora de trabalho?"))
tempo = float(input("Quantas horas você trabalha por mês?"))

salario = valor * tempo
imposto = salario * 0.11
inss = (salario - imposto) * 0.08
sindicato = (salario - imposto - inss) * 0.05
liquido = (salario- imposto - inss - sindicato)

print ('O seu salario bruto é de R$ {:.2f}'.format(salario))
print ('Valor pago de INSS: R$ {}'.format(inss))
print ('Valor pago ao sindicato: R$ {}' .format(sindicato))
print ('O seu salario líquido é de R$ {:.2f}' .format(liquido))