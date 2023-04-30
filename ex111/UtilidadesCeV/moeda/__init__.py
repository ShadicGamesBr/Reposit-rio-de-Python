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


def resumo(p=0, a=0, b=0):
    """\033[0;36m
    →Calcula a mudança de valores conforme os parâmetros a seguir:
    :param p:Preço inicial definido pelo usuário.
    :param a:Aumenta em % de preço.
    :param b:Redução em % de preço.
    :return:Função que retorna o resultado da soma entre cada uma das funções.\033[m
    """
    print("-"*30)
    print("       Resumo do valor")
    print("-"*30)
    print(str(f"Preço analisado\t\t\t\033[0;36m{moeda(p)}\033[m").replace(".", ","))
    print(str(f"Dobro do valor \t\t\t\033[0;36m{moeda(p*2)}\033[m").replace(".", ","))
    print(str(f"Metade do valor\t\t\t\033[0;36m{moeda(p/2)}\033[m").replace(".", ","))
    print(str(f"{a}% de aumento\t\t\t\033[0;36m{moeda(p + (p*a/100))}\033[m").replace(".", ","))
    print(str(f"{b}% de redução\t\t\t\033[0;36m{moeda(p - (p*b/100))}\033[m").replace(".", ","))
