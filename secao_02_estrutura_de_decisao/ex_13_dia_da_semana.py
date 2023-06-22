"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    >>> calcular_dia_da_semana(1)
    'Domingo'
    >>> calcular_dia_da_semana(2)
    'Segunda'
    >>> calcular_dia_da_semana(3)
    'Terça'
    >>> calcular_dia_da_semana(4)
    'Quarta'
    >>> calcular_dia_da_semana(5)
    'Quinta'
    >>> calcular_dia_da_semana(6)
    'Sexta'
    >>> calcular_dia_da_semana(7)
    'Sábado'
    >>> calcular_dia_da_semana(8)
    'Dia Inválido'
    >>> calcular_dia_da_semana(0)
    'Dia Inválido'

"""


def calcular_dia_da_semana(numero: int):

    if numero == 1:
        dia_da_semana = """'Domingo'"""
    elif numero == 2:
        dia_da_semana = """'Segunda'"""
    elif numero == 3:
        dia_da_semana = """'Terça'"""
    elif numero == 4:
        dia_da_semana = """'Quarta'"""
    elif numero == 5:
        dia_da_semana = """'Quinta'"""
    elif numero == 6:
        dia_da_semana = """'Sexta'"""
    elif numero == 7:
        dia_da_semana = """'Sábado'"""
    elif numero == 8:
        dia_da_semana = """'Dia Inválido'"""
    elif numero == 0:
        dia_da_semana = """'Dia Inválido'"""
    else:
        dia_da_semana = """'Dia Inválido'"""

    print(dia_da_semana)


if __name__ == '__main__':

    numero = int(input('Digite um número e exiba o dia correspondente da semana: '))

    msg = calcular_dia_da_semana(numero)
