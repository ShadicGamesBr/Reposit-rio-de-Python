#Adicione ao módulo moeda.py criado nos desafio anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.

import dado
import moeda

p = dado.leiadinheiro("Digite o preço: R$")
moeda.resumo(p, 7, 22)
