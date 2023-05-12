from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ra = str(input("RA do aluno: ")).strip()
data = str(input("Data de nascimento: ")).strip()
digito = str(input("Dígito verificador: ")).strip()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 4)
texto = open("resultados_Felipe.txt", "a")
resultados = []
data.replace("", "/").strip()
for ano in range(2015, 2022):
    try:
        resultados.append(f"Ano de {ano}")
        #print(resultados)
        print(f"Ano de {ano}")
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
        print("\n")
        elementoNome = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]")))
        nomeRA = elementoNome[0]
        elementos = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div[4]/table")))
        frase = elementos[0]
        print(f"{frase.text}".strip().replace("\n", "").replace(" ", ""))
        print(f"\033[31mNome: {nomeRA.text}\033[m".upper().strip())
        print("\n")
        resultados.append(f"\033[32m{frase.text}\033[m")
        texto.writelines(f"{frase.text}")
        #.strip().replace("\n", ""). replace(" ", "")
        #print(resultados)
    except:
        print("\033[31mAno indisponível\033[m")
    #if len(elementos) > 0:
    #    frase = elementos[0]
    #    print(frase.text)
    #else:
    #    print("Ano não disponível")
    print("\n\n\n")
driver.quit()
