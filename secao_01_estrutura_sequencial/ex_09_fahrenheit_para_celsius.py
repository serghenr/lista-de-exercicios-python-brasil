"""
Exercício 09 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_09_fahrenheit_para_celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '0'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de -18 Celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '70'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de 21 Celsius

"""

""


def transformar_para_celsius():
    f = float(input('Qual é a temperatura em Farenheit que você vê agora? '))
    c = (f - 32) / 1.8
    print(f'Essa temperatura é de {c:.0f} Celsius')
