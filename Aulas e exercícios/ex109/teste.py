# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um
# parâmetro a mais,informando se o valor retornado por elas vai ser ou não formatado
# pela funçãomoeda(), desenvolvida no desafio 108.

import moeda
p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobra(p, True)}.")
print(f"Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumentar(p, 10, True)}.")
print(f"Reduzindo 13% de {moeda.moeda(p)} temos {moeda.diminuir(p, 13, True)}")
