# Aqui uma variável recebe um valor qualquer digitado pelo usuário
t1 = float(input("Digite uma temperatura qualquer: "))
res = "s"

# loop para continuar a executar o programa se a resposta for S ou s
while res == "s" or res == "S":
    print(f"Para converter {t1} °Celsius para Fahrenheit, digite F.")
    con = input(f"Ou para converter {t1} °Fahrenheit para Celsius, digite C: ")

    # loop para o usuário digitar corretamente as opções F, f, C ou c
    while con != "F" and con != "f" and con != "C" and con != "c":
        print("Caractere inválido, digite novamente.")
        print(f"Para converter {t1} °Celsius para Fahrenheit, digite F.")
        con = input(f"Ou para converter {t1} °Fahrenheit para Celsius, digite C: ")

    # condição que testa se vai converter de °C para °F ou de °F para °C
    if con == "F" or con == "f":
        tF = t1 * (9/5) + 32
        print(t1, " °C é igual a ", tF, " °F.")
    elif con == "C" or con =="c":
        tC = (t1 - 32) * (5/9)
        print(t1, " °F é igual a ", tC, " °C.")

    # loop final em caso de uma nova conversão
    res = input("Deseja continuar? (S/N): ")
    if res == "s" or res == "S":
        t1 = float(input("Digite uma temperatura qualquer: "))
