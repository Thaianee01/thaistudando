#Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar, e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor. Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.#

print ("Calculando tintas eba")

area = float(input("Digite a area,em metros quadrados, que você deseja pintar:"))
litro = 3

volume = area / litro
latas = int(volume / 18)
preço = latas * 80


print ('você precisará de {}, isso custará {} reais'.format(latas,preço))

