"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):


    if telefonou == True and estava_no_local == True and mora_perto == True and deveia == True and trabalhou == True:
        return 'Assassino'
    elif telefonou == False and estava_no_local == False and mora_perto == False and deveia == False and trabalhou == False:
        return 'Inocente'


if __name__ == '__main__':

    telefonou = str(input("Telefonou para a vítima? "))
    estava_no_local = str(input("Esteve no local do crime? "))
    mora_perto = str(input("Mora perto da vítima? "))
    deveia = str(input("Devia para a vítima? "))
    trabalhou = str(input("Já trabalhou com a vítima? "))

    msg = investigar(telefonou, estava_no_local, mora_perto, deveia, trabalhou)
