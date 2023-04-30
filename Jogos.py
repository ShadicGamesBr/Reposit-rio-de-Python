print("JOGOS")
print()
jogos = ["\033[34mJO-KEN-PO\033[m", "\033[32mJogo da adivinhação\033[m", "\033[31mJogo da Tabuada\033[m",
         "\033[36mPense em um número!\033[m", "Voltar"]

for ele in jogos:
    print(ele)
esc = int(input("\nPor favor, escolha um jogo"))
if esc == 1:
    dados = {"Derrotas": 0, "Empates": 0, "Vitórias": 0}  # derrotas, #empates, #vitórias
    while True:
        def computador(fala, interacao=False):
            if not interacao:
                print(fala)
            else:
                str(input(f"{fala} ?"))
            return fala


        from random import sample

        from time import sleep


        print()
        print(jogos[0])
        escjogador = str(input("Sua escolha:")).strip().lower()

        computador("Jo")
        sleep(0.5)
        computador("Ken")
        sleep(0.5)
        computador("Po")
        sleep(0.5)
        esccomp = sample(["tesoura", "pedra", "papel"], k=1)
        print(esccomp)

        # perder
        if escjogador == "tesoura" and esccomp == ["pedra"] or escjogador == "pedra" and esccomp == [
            "papel"] or escjogador == "papel" and esccomp == ["tesoura"]:
            dados["Derrotas"] += 1
            print(f"\033[31mO computador escolheu {esccomp}, e você escolheu {escjogador}, logo Você perdeu\033[m")

        # empatar
        elif escjogador == "tesoura" and esccomp == ["tesoura"] or escjogador == "pedra" and esccomp == [
            "pedra"] or escjogador == "papel" and esccomp == ["papel"]:
            dados["Empates"] += 1
            print(f"\033[33mTivemos um empate!\033[m")
        # ganhar
        else:
            dados["Vitórias"] += 1
            print(f"\033[32mO computador escolheu {esccomp}, e você escolheu {escjogador}, logo você ganhou\033[m")
        esc = str(input("Quer mostrar seu score no jogo ? (o jogo para)"))
        if esc == "s":
            for k, v in dados.items():
                print(f"{k}: {v}")
            break
    print("\033[96mAté a próxima\033[m")


if esc == 2:
    print("Em breve")
if esc == 2:
    print("Em breve")
if esc == 2:
    print("Em breve")
if esc == 2:
    print("Em breve")
