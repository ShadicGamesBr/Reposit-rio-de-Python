from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#ra = str(input("RA do aluno: ")).strip()
#data = str(input("Data de nascimento: ")).strip()
#digito = str(input("Dígito verificador: ")).strip()
#data.replace("", "/").strip()
ra = '107058875'
data = "23/06/2003"
digito = '1'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7)
num = []
disciplina = {"1bim":[],"2bim":[],"3bim":[],"4bim":[]}
for ano in range(2015, 2022):
    try:
        try:
            print(f"Ano de \033[34m{ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
            print("\n")

            for notn in range(1, 13): #seleciona cada disciplina
                for bim in range(2, 15, 4): #pega um número de 4 em 4 para selecionar a coluna certa para pegar as notas de cada bimestre
                    bimnot = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                    num.append(bimnot)
                    print(f"{bimnot}", end=" ")
                print()
                

            
        except:
            print("\n\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()