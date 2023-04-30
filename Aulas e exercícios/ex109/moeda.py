# Crie um programa chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir, dobra () e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(p, num, e=True):
    if e:
        res = f"R${p + (p * num / 100):.2f}"
        return res
    else:
        res = f"{p + (p * num / 100):.2f}"
        return res


def diminuir(p, num, e=True):
    if e:
        res = f"R${p - (p * num / 100):.2f}"
        return res
    else:
        res = f"{p - (p * num / 100):.2f}"
        return res


def dobra(p, e=True):
    if e:
        res = f"R${p * 2}"
        return res
    else:
        res = f"{p * 2:.2f}"
        return res


def metade(p, e=True):
    if e:
        res = f"R${p / 2}"
        return res
    else:
        res = f"{p / 2:.2f}"
        return res


def moeda(p):
    res = f"R${p:.2f}"
    return res
