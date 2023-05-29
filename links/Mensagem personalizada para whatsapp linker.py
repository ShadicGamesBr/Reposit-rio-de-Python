#número fixo

try:
      while True:
            texto = open("WhatsAppLink.txt", "w")
            #aplica = str(input("Nome do Aplicativo: "))
            #aplica = "jacke Bolos".replace(" ", "%20").strip()
            #imagem = str(input("Código 64 da imagem: "))
            #Número fixo
            numero = str("55 17 99774-0269").replace(" ", "").replace("-", "")
            #numero = str("55 17 991777462").replace(" ", "").replace("-", "")
            print("\n\nOlá! Gostaria de encomendar um bolo caseiro de [sabor desejado]. Qual é o tamanho disponível para entrega e qual é o valor? Obrigado!")
            #número personalizado
            #numero = str(input("Insira o número para o Whatsapp: ")).replace(" ", "").replace("-", "")
            print(f"\033[0;36mEnviar para {numero}\033[m")
            mensagem = str(input("Digite aqui a mensagem personalizada: ")).replace(" ", "%20").replace(".", "%2E").replace("?", "%3f").replace("=", "%3D").replace("+", "%2B").replace("-", "%2D").replace("!", "%21")
            mensagem.replace(" ", "%20").replace("/", "%2F").strip()
            print(f"Copie e cole esse endereço da web:\n"
                  f"https://wa.me/{numero}/?text={mensagem}")
            #texto.writelines(f"https://wa.me/{numero}/?text={mensagem}&source={aplica}&data={imagem}".replace(" ", "").strip().replace("\n", ""))
            texto.flush()
            per = str(input("Quer continuar ?"))
            if per in "n":
                  print(f"\033[0;31mFim do programa\033[m")
                  break
except:
      print("Erro, verifique o número do WhatsApp ou Verifique se a mensagem está correta")
