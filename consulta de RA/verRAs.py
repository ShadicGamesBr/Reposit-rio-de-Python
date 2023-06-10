from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from matplotlib import pyplot as plt
from copy import deepcopy

ra = '107058875'
data = "23/06/2003"
digito = '1'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7)
arte = []
for ano in range(2015, 2016):
    try:
        try:
            print(f"Ano de \033[34m{ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
            print("\n")
            notaBim = {}
            notas_disciplina =[]
            for notn in range(1, 13): #seleciona cada disciplina
                for bim in range(2, 17, 4): #pega um número de 4 em 4 para selecionar a coluna certa para pegar as notas de cada bimestre
                    bimnot = wait.until(EC.presence_of_all_elements_located((By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                    if bimnot in ('10') or bimnot in ('123456789'):
                        print(f"\033[32m{bimnot}\033[m", end=" ")
                        notas_disciplina.append(bimnot)
                    else:
                        print("", end="")
                print()
        except:
            print("\n\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()
print(arte)
