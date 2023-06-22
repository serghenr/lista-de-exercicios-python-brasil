"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):

    from datetime import datetime

    try:
        data = datetime.strptime(f'{day}/{month}/{year}', data_ptbr_format).date()
    except ValueError:
        print('Data válida')
    else:
        print('Data inválida')

    if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
            return f'Data válida'
        if day == 0 or day < 0 or day == '':
            return f'Data inválida'
        elif month == 0 or month < 0 or month == '':
            return f'Data inválida'
        elif year == 0 or year < 0 or month == '':
            return f'Data inválida'
        else:
            return f'Data inválida'



if __name__ == "__main__":

    day = int(input('Digite o dia: '))
    month = int(input('Digite o mês: '))
    year = int(input('Digite o ano: '))