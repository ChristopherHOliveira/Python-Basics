# criando a função 'media', que retorna a soma de 'm' dividido pelo tamanho de 'm':
def media(m):
    return(sum(m)/len(m))

# criando uma lista vazia:
lst = []

# pedindo para o usiário digitar um valor de tamanho da lista:
tam_lst = float(input("Digite o tamanho da lista: "))

# teste para aceitar apenas números inteiros:
while int(tam_lst) != tam_lst:
    tam_lst = float(input("Ops, apenas números inteiros! Digite novamente: "))
print("Ok")    

# pedindo para o usuário digitar os itens da lista:
for x in range(int(tam_lst)):
    lst.append(float(input(f"Digite os {tam_lst} itens da lista, um por um: ")))

# saída da média dos números da lista:
print(f"A média dos valores contidos na lista é {media(lst)}")
