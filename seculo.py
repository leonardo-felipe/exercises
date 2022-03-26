# O primeiro século vai do ano 1 até e incluindo o ano 100, o segundo século - do ano 101 até e incluindo * o ano 200, etc.
# Dado um ano, retorne o século em que ele se encontra.
# Exemplos:
# entrada: 1705, resultado: 18
# entrada: 1900, resultado: 19
# entrada: 1601, resultado: 17
# entrada: 2000, resultado: 20

ano = int(input())

def seculo(ano):
    print((ano - 1) // 100 + 1)

seculo(ano)
