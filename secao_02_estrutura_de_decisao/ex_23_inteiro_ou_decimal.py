"""
Exercício 23 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

    >>> decidir_se_eh_inteiro_ou_decimal('256')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('1.0')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('2.0000')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('2.00001')
    'Decimal'
    >>> decidir_se_eh_inteiro_ou_decimal('11.2')
    'Decimal'
    >>> decidir_se_eh_inteiro_ou_decimal('3.1415')
    'Decimal'
"""


def decidir_se_eh_inteiro_ou_decimal(valor: str) -> str:

    if valor == 1:
        return 'Inteiro'
    elif valor % 2 == 0 and valor != 1:
        return 'Inteiro'
    else:
        return 'Decimal'


if __name__ == '__main__':
    valor = float(input('Digite um número: '))

    msg = decidir_se_eh_inteiro_ou_decimal(valor)

    print(msg)
