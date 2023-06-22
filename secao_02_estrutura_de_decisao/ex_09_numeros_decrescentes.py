"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):

    if x > y and x > z:
        maior = x
        if y > z:
            menor = z
            meio = y
        else:
            menor = y
            meio = z
    elif y > z and y > x:
        maior = y
        if z > x:
            menor = x
            meio = z
        else:
            menor = z
            meio = x
    else:
        maior = z
        if y > x:
            menor = x
            meio = y
        else:
            menor = y
            meio = x

    print(f'{maior}, {meio}, {menor}')


if __name__ == '__main__':

    x = float(input('Digite 1° número: '))
    y = float(input('Digite 2° número: '))
    z = float(input('Digite 3° número: '))

    msg = ordenar_decrescente(x, y, z)
