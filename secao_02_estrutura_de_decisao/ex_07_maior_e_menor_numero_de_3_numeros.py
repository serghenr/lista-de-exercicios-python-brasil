"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2, 3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):

    if x > y and x > z:
        maior = x
        if y > z:
            menor = z
        else:
            menor = y
    elif y > z and y > x:
        maior = y
        if z > x:
            menor = x
        else:
            menor = z
    else:
        maior = z
        if y > x:
            menor = x
        else:
            menor = y

    print(f'Maior: {maior}\n'
          f'Menor: {menor}')


if __name__ == '__main__':
    x = int(input('Digite 1° número: '))
    y = int(input('Digite 2° número: '))
    z = int(input('Digite 3° número: '))

    msg = calcular_maior_de_3_numeros(x, y, z)
