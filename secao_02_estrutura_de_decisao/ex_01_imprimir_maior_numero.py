"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


""


def maior_de_dois_numeros(x, y):

    if x > 0 and y > 0:
        if y > x:
            print(y)
    elif x < 0 and y < 0:
        if x > y:
            print(x)
    elif x < 0 < y:
        if x < y:
            print(y)
    else:
        print(x)

if __name__ == '__main__':
    x = int(input('X = 1° número: '))
    y = int(input('Y = 2° número: '))

    msg = maior_de_dois_numeros(x,y)
