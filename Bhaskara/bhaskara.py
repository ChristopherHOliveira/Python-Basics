def bhaskara(a, b, c):

    # Equação: ax² + bx + c = 0
    # delta = b² - 4ac
    # x = (-b +- raiz(delta) / 2a

    delta = b**2 - 4*a*c

    if delta < 0:
        resposta = (f'\n\nDelta ({delta}) é menor do que 0.\n'
                    'Portanto a equação não possui resultado real.')
        return resposta
    elif delta == 0:
        x = -b / (2*a)
        resposta = ('\n\nDelta é igual a 0.\n'
                    'Portanto a equação possui um resultado real:'
                    f'x = {x}.')
        return resposta
    else:
        x1 = ((-b) + delta**(1/2)) / (2 * a)
        x2 = ((-b) - delta**(1/2)) / (2 * a)
        resposta = (f'\n\nDelta ({delta}) é maior que 0.\n'
                    'Portanto a equação possui dois resultados reais:\n'
                    f'x1 = {x1}\n'
                    f'x2 = {x2}')
        return resposta


# chamando a função e imprimindo o retorno
print(bhaskara(3, 33, 99))
print(bhaskara(1, -10, 25))
print(bhaskara(1, 12, -13))
