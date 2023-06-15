try:
    from datetime import datetime
    ano = datetime.now().year
    nasc = int(input("Em que ano você nasceu ?"))
    print(f"Em {ano} você vai fazer/fez {ano-nasc} anos!")
except:
    print("Por favor, digite apenas números para calcular a sua idade :)")