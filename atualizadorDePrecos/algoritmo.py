from time import sleep

precos = {"Bolo de cenoura": "R$25,00",
          "Bolo de leite ninho": "R$35,00"
         ,"Bolo de cenoura c. cobertura de chocolate": "R$35,00"
         ,"Bolo de fuba c. goiaba": "R$25,00",
          "Bolo de iogurte": "R$35,00",
          "Bolo dee coco": "R$25,00",
          "Bolo de fuba": "R$25,00",
          "Bolo de fuba c. erva doce": "R$25,00",
          "Bolo de cenoura mesclado c. chocolate": "R$25,00",
          "Bolo de café": "R$25,00",
          "Bolo de banana c. canela": "R$35,00",
          "Bolo de amendoin com ninho": "R$35,00",
          "Bolo de limão c. musse": "R$35,00",
          "Bolo de laranja c. musse": "R$35,00"}

conteudo = []

for nome, preço in precos.items():
    conteudo.append(f"{nome} {preço}")

#print(conteudo)
texto = open("precos.txt", "r")
print(texto.read())
#try:
#    texto = open("precos.txt" "r")
#    print("Arquivo lido com sucesso")
#    texto.read()
#    texto = open("precos.txt", "w")
#    texto.read()
#except:
#    print("Não consegui ler o arquivo")
