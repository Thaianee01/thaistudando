
#Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome.#

nome = input("Qual o seu nome completo?")
primeiro = nome.split ( ) [0]
print ("Olá {}, seja bem vindo(a)".format(primeiro))