from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ra = str(input("RA do aluno: ")).strip()
data = str(input("Data de nascimento: ")).strip()
digito = str(input("Dígito verificador: ")).strip()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
for ano in range(2014, 2023):
    try:
        print(f"\033[34mAno de {ano}\033[m")
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}")
        print("\n")

        elementos = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div[4]/table")))
        frase = elementos[0]
        print(f"\033[32m{frase.text}\033[m")

    except:
        print("\033[31mAno indisponível\033[m")
    #if len(elementos) > 0:
    #    frase = elementos[0]
    #    print(frase.text)
    #else:
    #    print("Ano não disponível")

    print("\n\n\n")
driver.quit()
