
try:
    nome = str(input("Qual é o seu nome ? "))

    print(f"\033[36mVocê é muito bem vindo {nome.title().strip()}!\033[m")
except:
    print("\033[31mNão consegui aplicar o seu nome na mensagem de boas vindas, considere-se escrever apenas letras!\033[m")
    