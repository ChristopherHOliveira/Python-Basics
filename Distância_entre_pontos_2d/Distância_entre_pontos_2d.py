# pré determinando valor 's' na variável resposta do while:
res = "s"

# entrada de dados de coordenada X e Y do primeiro ponto:
print("Olá, este programa calcula a distância entre dois pontos!")
print("Digite as coordenadas do primeiro ponto:")
ax = float(input("Coordenada X: "))
ay = float(input("Coordenada Y: "))

# entrada de dados de coordenada X e Y do segundo ponto:
print("Digite as coordenadas do segundo ponto:")
bx = float(input("Coordenada X: "))
by = float(input("Coordenada Y: "))

# loop enquanto a resposta for 's':
while res == "s" or res =="S":
    
    # fórmula da distância entre os pontos:
    dist = ((bx-ax)**2+(by-ay)**2)**(1/2)
    
    # saída:
    print("A distância cartesiana entre os dois pontos é ", dist)

    # Loop para rodar ou não o programa novamente:
    res = input("Deseja calcular outra distância? (S/N)")

    # enquanto a resposta for inválido, repetir a pergunta: 
    while res != "s" and res != "S" and res != "n" and res != "N":
        res = input("Caractere inválido. Deseja calcular outra distância? (S/N)")

    # se 's', receber os dados novamente e repetir o programa no while:
    if res == "s" or res == "S":
        print("Digite as coordenadas do primeiro ponto:")
        ax = float(input("Coordenada X: "))
        ay = float(input("Coordenada Y: "))

        print("Digite as coordenadas do segundo ponto:")
        bx = float(input("Coordenada X: "))
        by = float(input("Coordenada Y: "))

# criar programa que calcula a distância espacial tridimensional entre dois pontos
