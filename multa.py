#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input("Velocidade do carro:"))
limite = 80

if velocidade > 80:
    excesso_velocidade = velocidade - 80
    multa = excesso_velocidade * 5

    print (f"Você foi multado. O valor da multa é de {multa}")

else: 
    print ("Você está dentro do limite de segurança")