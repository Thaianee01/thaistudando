par = 0
impar = 0
soma_par = 0
soma_impar = 0

while True:
    numero = int(input("digite o numero ="))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        par = par + 1
        soma_par += numero

    else:
        impar = impar + 1
        soma_impar += numero

if par > 0:
    pares = soma_par/par
else:
    pares = 0

if impar > 0:
    impares = soma_impar/impar
else:
    impares = 0

print("media pares = {0:.2f}".format(pares))
print("media impares = {0:.2f}".format(impares))