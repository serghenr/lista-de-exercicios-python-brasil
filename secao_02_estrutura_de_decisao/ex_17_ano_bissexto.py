"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False

"""


def eh_ano_bissexto(ano: int):

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('True')
    else:
        print('False')


if __name__ == '__main__':

    ano = int(input('Digite o ano para saber se é bissexto: '))

    msg = eh_ano_bissexto(ano)

