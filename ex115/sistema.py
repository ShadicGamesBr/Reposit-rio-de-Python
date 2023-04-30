from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do programa"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("Novo cadastro")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... até logo!")
        break
    else:
        print("\033[31mERRO: Digite uma opção válida\033[m")
    sleep(0.5)
