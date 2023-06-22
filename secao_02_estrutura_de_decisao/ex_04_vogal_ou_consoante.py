"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):

    if letra in "aeiouAEIOU":
        return 'vogal'
    else:
        return 'consoante'


if __name__ == '__main__':
    letra = str(input('verifique se uma letra digitada é vogal ou consoante: '))
    msg = vogal_ou_consoante(letra)
    print(msg)
