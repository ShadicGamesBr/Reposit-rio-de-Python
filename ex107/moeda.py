# Crie um programa chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir, dobra () e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(p, num):
    res = p + (p * num / 100)
    return res


def diminuir(p, num):
    res = p - (p * num / 100)
    return res


def dobra(p):
    res = p * 2
    return res


def metade(p):
    res = p / 2
    return res


def moeda(p):
    res = f"R${p:.2f}"
    return res
