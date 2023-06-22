"""
Exercício 08 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
Mostrar salário com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_08_horas_trabalhadas_mes
    >>> numeros =['80', '55.62']
    >>> ex_08_horas_trabalhadas_mes.input = lambda k: numeros.pop()
    >>> ex_08_horas_trabalhadas_mes.calcular_salario()
    Seu salário desse mês é 4449.60

"""

""


def calcular_salario():
    ganho_hora = float(input('Digite o quanto você ganha por hora trabalhada: '))
    horas_mes = float(input('Digite o total de horas trabalhadas no mês: '))
    salario = ganho_hora * horas_mes
    print(f'Seu salário desse mês é {salario:.2f}')
