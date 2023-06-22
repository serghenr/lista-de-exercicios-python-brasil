"""
Exercício 02 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. Caso seja igual a 0, retorne None.

    >>> positivo_ou_negativo(1)
    'positivo'
    >>> positivo_ou_negativo(-1)
    'negativo'
    >>> positivo_ou_negativo(0)
    'não tem positivo nem negativo'
    >>> positivo_ou_negativo(-100)
    'negativo'
"""


def positivo_ou_negativo(n):

    if n == 0:
        return 'não tem positivo nem negativo'
    elif n < 0:
        return 'negativo'
    elif n > 0:
        return 'positivo'

if __name__ == '__main__':
    n = int(input('Digite um número qualquer: '))
    msg = positivo_ou_negativo(n)
    print(msg)