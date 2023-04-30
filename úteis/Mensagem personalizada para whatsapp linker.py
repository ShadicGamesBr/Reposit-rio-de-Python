#número fixo

try:


      while True:
            #Número fixo
            numero = str("55 17 99774-0269").replace(" ", "").replace("-", "")
            print("\n\nOlá! Gostaria de encomendar um bolo caseiro de [sabor desejado]. Qual é o tamanho disponível para entrega e qual é o valor? Obrigado!")
            #número personalizado
            #numero = str(input("Insira o número para o Whatsapp: ")).replace(" ", "").replace("-", "")
            print(f"\033[0;36mEnviar para {numero}\033[m")
            mensagem = str(input("Digite aqui a mensagem personalizada: ")).replace(" ", "%20").replace(".", "%2E").replace("?", "%3f").replace("=", "%3D").replace("+", "%2B").replace("/", "2F").replace("-", "%2D").replace("!", "%21")
            mensagem.replace(" ", "%20").strip()
            print(f"Copie e cole esse endereço da web:\n"
                  f"\033[0;34mhttps://wa.me/{numero}?text={mensagem}\033[m")
            per = str(input("Quer continuar ?"))
            if per in "n":
                  print(f"\033[0;31mFim do programa\033[m")
                  break
except:
      print("Erro, verifique o número do WhatsApp ou Verifique se a mensagem está correta")
