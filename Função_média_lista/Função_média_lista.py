def media(m):
    return(sum(m)/len(m))

lst = []

tam_lst = float(input("Digite o tamanho da lista: "))

while int(tam_lst) != tam_lst:
    tam_lst = float(input("Ops, apenas números inteiros! Digite novamente: "))

print("Ok")    

for x in range(int(tam_lst)):
    lst.append(float(input(f"Digite os {tam_lst} itens da lista, um por um: ")))

print(f"A média dos valores contidos na lista é {media(lst)}")
