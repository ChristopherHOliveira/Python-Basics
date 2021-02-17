res = "s"

print("Olá, este programa calcula a distância entre dois pontos!")
print("Digite as coordenadas do primeiro ponto:")
ax = float(input("Coordenada X: "))
ay = float(input("Coordenada Y: "))

print("Digite as coordenadas do segundo ponto:")
bx = float(input("Coordenada X: "))
by = float(input("Coordenada Y: "))

while res == "s" or res =="S":

    dist = ((bx-ax)**2+(by-ay)**2)**(1/2)

    print("A distância cartesiana entre os dois pontos é ", dist)

    res = input("Deseja calcular outra distância? (S/N)")

    while res != "s" and res != "S" and res != "n" and res != "N":
        res = input("Caractere inválido. Deseja calcular outra distância? (S/N)")

    if res == "s" or res == "S":
        print("Digite as coordenadas do primeiro ponto:")
        ax = float(input("Coordenada X: "))
        ay = float(input("Coordenada Y: "))

        print("Digite as coordenadas do segundo ponto:")
        bx = float(input("Coordenada X: "))
        by = float(input("Coordenada Y: "))

# criar programa que calcula a distância espacial tridimensional entre dois pontos