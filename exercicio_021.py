#EXERCICIO 4: Faça um programa em Python que leia diversos números inteiros e informe a média de números pares e ímpares lidos. Para terminar, entre com o número zero, que não deverá ser considerado no cálculo das médias.

par = 0
impar = 0
soma_par = 0
soma_impar = 0
media_par = 0
media_impar = 0

while True:
    pergunta = input("deseja fornecer um numero? (S/N) =")
    
    if pergunta == "S":
        n1 = int(input("digite o numero ="))
        
        if n1 % 2 == 0:
            par = par + 1
            soma_par += n1
            media_par = soma_par / par
            
        else:
            impar = impar + 1 
            soma_impar += n1
            media_impar = soma_impar / impar

    if pergunta == "N":
        break

print(f"media pares = {media_par:.2f}")
print(f"media impares= {media_impar:.2f}")