vp = float(input("Digite o valor do produto: R$"))
qtd = int(input("Digite a quantidade deste produto: "))
res = "s"

while res == "s":

    print("\nEscolha a condição de pagamento:")
    print("\nCÓDIGO | CONDIÇÃO DE PAGAMENTO")
    print("   1     à vista (10% de desconto)")
    print("   2     à vista no cartão de crédito (5% de desconto")
    print("   3     2x (sem juros)")
    print("   4     3x (10% de juros)")
    codigo = input("\nCódigo: ")

    while codigo != "1" and codigo != "2" and codigo != "3" and codigo != "4":
        print("Código inexistente!")
        codigo = input("\nCódigo: ")

    if codigo == "1":
        print("Valor do produto: R$", vp)
        print("Valor a pagar: R$", (vp*qtd)*0.9)

    elif codigo == "2":
        print("Valor do produto: R$", vp)
        print("Valor a pagar: R$", (vp*qtd)*0.95)

    elif codigo == "3":
        print("Valor do produto: R$", vp)
        print("Valor a pagar: 2x R$", (vp*qtd)/2)

    elif codigo == "4":
        print("Valor do produto: R$", vp)
        print("Valor a pagar: 3x R$", ((vp*qtd)*1.1)/3)

    res = input("Deseja passar outro(s) produtos? (S/N)")

    while res != "s" and res != "S" and res != "n" and res != "N":
        res = input("Caractere inválido. Deseja passar outro(s) produtos? (S/N)")

    if res == "s" or res == "S":
        vp = float(input("Digite o valor do produto: R$"))
        qtd = int(input("Digite a quantidade deste produto: "))

# adicionar carrinho com acumulador de itens