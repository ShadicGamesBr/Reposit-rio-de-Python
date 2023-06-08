from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from matplotlib import pyplot as plt

#ra = str(input("RA do aluno: ")).strip()
#data = str(input("Data de nascimento: ")).strip()
#digito = str(input("Dígito verificador: ")).strip()
#data.replace("", "/").strip()
ra = '107058875'
data = "23/06/2003"
digito = '1'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)
num = []
disciplina = []
for ano in range(2015, 2022):
    try:

        print(f"\nAno de \033[34m{ano}\033[m")
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
        print("\n")

        discinota = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"/html/body/div/div/div[4]/table/#tbody/tr{noth}/td[1]")))[0].text

        disciplina.append(discinota)

        for notn in range(1, 13): #faz 12 vezes para cada disciplina


            for bim in range(2, 17, 4):
                bimnot = wait.until(EC.presence_of_all_elements_located((By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text #pega nota e bimestre o noth é para cada nota, e o bim, ele avança um bimestre.
                num.append(bimnot)

                print(f"{discinota} {bimnot}", end=" ")
            print()
        print("\n\n\n")
    except:
        print("")
driver.quit()
print()