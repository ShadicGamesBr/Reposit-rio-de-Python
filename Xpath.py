from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ra = str(input("RA do aluno: ")).strip()
data = str(input("Data de nascimento: ")).strip()
digito = str(input("Dígito verificador: ")).strip()
driver = webdriver.Chrome()

for ano in range(2015, 2022):
    print(f"\033[34mAno de {ano}\033[m")
    driver.get(
        f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa=1&dsUfRa=SP&dtNascimento=23/06/2003&nrAnoLetivo={000+ano}")
    print("\n")
    wait = WebDriverWait(driver, 15)
    elementos = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div[4]/table")))
    nome = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]")))
    if len(elementos) > 0:
        frase = elementos[0]
        print(frase.text)
    else:
        print("Ano não disponível")

    print("\n\n\n")
driver.quit()
