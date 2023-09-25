#Faça um programa em Python para calcular e imprimir o dígito verificador de uma conta bancária. O usuário deve informar o número da conta que deve ser um número inteiro com 4 dígitos. O dígito verificador será calculado como segue:

comentario = [ 
    "Somar todos os quatro dígitos."
    "Multiplicar todos os quatro dígitos."
    "Subtrair o resultado da soma (passo 1) do resultado da multiplicação (passo 2)."
    "O dígito verificador será o resto da divisão do resultado da subtração (passo 3) por 9. "
]

import math

numero = int(input("numero da conta (4 digitos) ="))

n1 = numero//1000
n2 = (numero%1000) //100
n3 = (numero % 100) // 10
n4 = (numero % 100) % 10
soma = n1 + n2 +n3+ n4
multiplicacao = n1*n2*n3*n4
conta = multiplicacao - soma
verificador = conta % 9

print ("digito verificador =", verificador)