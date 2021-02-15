n1 = float(input("Digite o 1° número: "))
n2 = float(input("Digite o 2° número: "))
res = "s"

while res == "s" or res == "S":
    print("")
    print("Operadores aritméticos")
    print("[ + , - , * , / , ^ ]")
    print("")
    print("Operadores relacionais")
    print("[ > , < , = , != , >= , <= ]")
    print("")
    print("Para",n1, "[operador]", n2, ", ")
    print("")
    op = input("digite o operador desejado: ")
    print("")

    if op == "+":
        print(n1, op, n2, "=", n1+n2)
    elif op == "-":
        print(n1, op, n2, "=", n1-n2)
    elif op == "/":
        print(n1, op, n2, "=", n1/n2)
    elif op == "*":
        print(n1, op, n2, "=", n1*n2)
    elif op == "^":
        print(n1, op, n2, "=", n1**n2)
    elif op == ">":
        print(n1, op, n2, "=", n1>n2)
    elif op == "<":
        print(n1, op, n2, "=", n1<n2)
    elif op == "=":
        print(n1, op, n2, "=", n1==n2)
    elif op == "!=":
        print(n1, op, n2, "=", n1!=n2)
    elif op == ">=":
        print(n1, op, n2, "=", n1>=n2)
    elif op == "<=":
        print(n1, op, n2, "=", n1<=n2)
    else:
        print("Operador inválido!\n")
    
    res = input("Deseja continuar? (S/N)")

    while res != "s" and res != "S" and res != "n" and res != "N":
        res = input("Caractere inválido. Deseja continuar? (S/N)")

    if res == "s" or res =="S":
        n1 = float(input("Digite o 1° número: "))
        n2 = float(input("Digite o 2° número: "))