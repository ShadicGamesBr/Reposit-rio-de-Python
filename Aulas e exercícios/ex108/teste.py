#Adapte um código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de é {moeda.moeda(p)} é {moeda.moeda(moeda.dobra(p))}")
print(f"Aumentando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Reduzindo 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}")
