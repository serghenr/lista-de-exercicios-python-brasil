"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():

    size_arquive_mega_bytes = int(input('Tamanho em MB: '))
    speed_internet_mega_bits_per_second = int(input('Velocidade em Mbps: '))

    size_arquive_mega_bits = size_arquive_mega_bytes * 8
    time_download_per_seconds = size_arquive_mega_bits / speed_internet_mega_bits_per_second
    time_download_per_minutes = round(time_download_per_seconds / 60)

    print(f'O tempo aproximado do Download é: {time_download_per_minutes} minuto(s)')
