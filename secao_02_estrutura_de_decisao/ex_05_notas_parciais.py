"""
Exercício 05 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
Obs: 0 <= nota <= 10

    >>> notas_parciais(10, 4)
    'Aprovado'
    >>> notas_parciais(0, 10)
    'Reprovado'
    >>> notas_parciais(5, 8)
    'Reprovado'
    >>> notas_parciais(10, 10)
    'Aprovado com Distinção'
"""


def notas_parciais(nota_1, nota_2):

    if (nota_1 + nota_2) / 2 == 10:
        return 'Aprovado com Distinção'
    elif (nota_1 + nota_2) / 2 >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

if __name__ == '__main__':

    nota_1 = int(input('Digite a 1° nota: '))
    nota_2 = int(input('Digite a 2° nota: '))

    msg = notas_parciais(nota_1, nota_2)
    print(msg)