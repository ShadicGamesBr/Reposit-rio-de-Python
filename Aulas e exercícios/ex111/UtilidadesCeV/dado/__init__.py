
def leiadinheiro(p):
    p = str(input(p)).strip().replace(",", ".")
    while p.isalpha() or len(p) == 0:
        p = (str(input(f"\033[0;31mErro, {p} é um preço inválido!\033[m"))).strip().replace(",", ".")
    return float(p)
