#Desenho um código que extraia o domínio de um e-mail informado.#

email = input("Me informe seu e-mail:")
dominio = email.split ("@") [-1]
print ("O dominio informado foi: {}".format(dominio))