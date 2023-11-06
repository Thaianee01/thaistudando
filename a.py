quantidade = 0
somatorio = 0

while True:
    n1 = int(input("Digite um número: "))
    somatorio += n1
    quantidade += 1

    media = somatorio / quantidade

    proximo = input("Deseja ler mais um número? (S/N): ")

    if proximo.upper() == "N":
        print(f'Média aritmética = {media:.2f}')
        break
    elif proximo.upper() != "S":
        print("Opção inválida. Use 'S' para continuar ou 'N' para encerrar.")