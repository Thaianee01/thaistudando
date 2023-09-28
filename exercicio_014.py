import math

n1 = float(input("digite a nota da prova 1:"))
n2 = float(input("digite a nota da prova 2:"))

media = (n1 + n2) / 2
print ("============================")
print ("Sua média final foi de: {}".format (media))

if media ==10:
    print ("Aprovado com Distinção")

elif media >= 7:
    print ("aprovado") 
    
else:
    print ("reprovado")