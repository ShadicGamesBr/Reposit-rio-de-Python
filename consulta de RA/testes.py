from matplotlib import pyplot as plt
from random import randint

disciplinas = {"Artes" , "Biologia", "Educação física", "Filosofia", "Física", "Geografia", "História", "Inglês", "Português", "Matemática", "Química", "Sociologia"}


boletim = {}
for v in disciplinas:
    nivel1 = disciplinas
    boletim[nivel1] = {}
    for k in boletim:
        boletim[0] = randint(0, 10)
print(boletim)
