"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105.
    Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185.
    Vão sobrar 2.6 litro(s) de tinta.

"""
from math import ceil


def calcular_latas_e_preco_de_tinta():

    area_a_ser_pintada = float(input('Área em M² a ser pintada: '))
    um_litro_rende_em_m_2 = 6
    total_litros_necessario = ceil((area_a_ser_pintada / um_litro_rende_em_m_2) * 1.1)

    n_latas18 = (total_litros_necessario // 18 + 1)
    custo_lata18 = n_latas18 * 80
    sobra_latas18 = (n_latas18 * 18) - total_litros_necessario

    n_latas36 = (total_litros_necessario // 3.6 + 1)
    custo_lata36 = n_latas36 * 25
    sobra_latas36 = (n_latas36 * 3.6) - total_litros_necessario

    qt_lts18_mix_p_menor_custo = round(total_litros_necessario / 18)
    qt_g36__mixp_menor_custo = round((total_litros_necessario - qt_lts18_mix_p_menor_custo * 18) / 3.6 + 1)
    preco_p_melhor_custo_da_mistura = qt_lts18_mix_p_menor_custo * 80 + qt_g36__mixp_menor_custo * 25
    sobrara_da_mistura = (qt_lts18_mix_p_menor_custo * 18 + qt_g36__mixp_menor_custo * 3.6) - total_litros_necessario

    print(f'Você deve comprar {total_litros_necessario} litros de tinta.\n'
          f'Você pode comprar {n_latas18:.0f} lata(s) de 18 litros a um custo de R$ {custo_lata18:.0f}. Vão sobrar {sobra_latas18:.1f} litro(s) de tinta.\n'
          f'Você pode comprar {n_latas36:.0f} lata(s) de 3.6 litros a um custo de R$ {custo_lata36:.0f}. Vão sobrar {sobra_latas36:.1f} litro(s) de tinta.\n'
          f'Para menor custo, você pode comprar {qt_lts18_mix_p_menor_custo} lata(s) de 18 litros e {qt_g36__mixp_menor_custo} galão(ões) de 3.6 litros a um custo de R$ {preco_p_melhor_custo_da_mistura}.\n'
          f'Vão sobrar {sobrara_da_mistura:.1f} litro(s) de tinta.')
