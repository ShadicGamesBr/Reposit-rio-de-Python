# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir, dobra () e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobra(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13)}")
