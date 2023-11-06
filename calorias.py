#Faça um programa em Python que solicite a quantidade de quilômetros percorridos em uma corrida (km), o peso da pessoa que correu (kg) e o tempo (min) que a corrida demandou. O programa deve imprimir o total de calorias gastas, considerando o cálculo de calorias abaixo: Total Gasto de Calorias = Velocidade (em km/h) x Peso (em kg) x 0,00175 x Tempo (em min) #

import math

km = float(input("distancia percorrida(em km) ="))
minutos = float(input("tempo da corrida (em min) = "))
peso = float(input("peso da pessoa (em kg) = "))

horas = minutos/60
velocidade = (km/horas)
total = (velocidade*peso*minutos*0.00175) 
print (f'total gasto de calorias = {total:.2f}')