#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa = int(input("Digite o valor da casa que deseja comprar:"))
salario = int(input("Digite o seu salário:"))
anos = int(input("Digite em quantos anos você gostaria de pagar:"))

meses = anos * 12
prestacao = casa / meses
limite_emprestimo = 0.3 * salario

if prestacao <= limite_emprestimo:
    print ("Emprestimo aprovado")
    print (f'O valor do emprestimo aceito foi de: R$ {prestacao:.2f}')
else:
    print ("emprestimo recusado")