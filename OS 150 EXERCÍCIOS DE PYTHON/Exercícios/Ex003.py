try:
    temp = float(input("Temperatura em \033[m35Cº:\033[m "))
    print(f"Temperatura em \033[m32fº:\033[m {temp*1.8+32}")
except:
    print("Não consegui converter a temperatura, considere usar apenas números.")