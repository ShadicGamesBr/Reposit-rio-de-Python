print("Aplicativo de Teste e Tarefas")
apps = ["Calculadora", "Jogos", "Manual do usuário", "Relógio", "Cache do aparelho"]
print()
for ele in apps:
    print(f"\033[32m{ele}\033[m")
esc = int(input("\nApp: "))


if esc == 1:
    print(f"{apps[0]}")
    import Calculadora
if esc == 2:
    