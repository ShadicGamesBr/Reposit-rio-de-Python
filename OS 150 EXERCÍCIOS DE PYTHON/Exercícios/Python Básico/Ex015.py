try:
    print("Verificador de vogais e consoantes")
    pala = str(input("digite uma palavra: ")).strip().replace(" ", "").lower()
    vogais = 0
    vogaisE = ["a", "e", "i", "o", "u"]
    for i in range(0, len(pala)):
        for k in range(0, 5):
            if pala[i] in vogaisE[k]:
                vogais += 1
    print(f"Quantidade de \033[36mVogais\033[m: {vogais}\nQuantidade de \033[36mconsoantes\033[m: {len(pala)-vogais}")
except:
    print("Erro, tente reiniciar o programa")
