"""
Exercício 22 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).

    >>> decidir_se_eh_par_ou_impar(256)
    'Par'
    >>> decidir_se_eh_par_ou_impar(1)
    'Impar'
    >>> decidir_se_eh_par_ou_impar(5)
    'Impar'
    >>> decidir_se_eh_par_ou_impar(10)
    'Par'
    >>> decidir_se_eh_par_ou_impar(11)
    'Impar'
    >>> decidir_se_eh_par_ou_impar(399)
    'Impar'
"""


def decidir_se_eh_par_ou_impar(valor: int) -> str:

    if valor % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


if __name__ == '__main__':

    valor = int(input('Digite um número inteiro: '))

    msg = decidir_se_eh_par_ou_impar(valor)

    print(msg)
