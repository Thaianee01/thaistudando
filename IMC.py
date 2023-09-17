import time

print ("Bem vindo a calculadora de IMC")

altura = float(input("Digite a sua altura"))
peso = float (input("Digite o seu peso"))

print ("Calculando...")
time.sleep (1)
print ("-------------")
IMC = peso / (altura**2)

print (f"Seu IMC é de {IMC:.2f}")