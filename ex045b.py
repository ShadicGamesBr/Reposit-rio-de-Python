from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opcoes:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA""")
jogador = int(input("Qual e a sua jogada ? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=-"*15)
print("O computador escolheu {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=-"*15)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")

    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")

    else:
        print("JOGADA INVALIDA")

elif computador == 1: # O computador jogou  PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")

    else:
        print("JOGADA INVALIDA")

elif computador == 2:
    # O computador jogou  TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")

    else:
        print("JOGADA INVALIDA")
