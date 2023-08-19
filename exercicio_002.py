import math

#Faça um programa em Python que leia o numero de horas trabalhadas por um funcionario durante um mês, o valor que recebe por hora, o numero de horas extras trabalhadas e o numero de dependentes. O numero de horas trabalhadas durante um mês não inclui o número de horas extras. O programa deve calcular e imprimir o salário deste funcionário, sabendo-se que para cada hora extra o valor recebido é o dobro do valor normal e que cada dependente acrescenta 5% ao salário normal (sem contabilizar horas extras).#

a = int(input ("numero de horas trabalhadas no mes ="))
b = int(input ("valor recebido por hora = "))
c = int(input ("numero de horas extras trabalhadas = "))
d = int(input ("numero de dependentes = "))

x = a * b * (1+(d*0.05)) + 2* b * c 
print (f' valor total do salario = {x:.2f}')