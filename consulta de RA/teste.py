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
pontos = 0
num = []
#boletim = {"bimestre1":[], "bimestre2":[],"bimestre":[],"bimestre":[]}
for ano in range(2015, 2022):
    try:
        try:
            print(f"Ano de \033[34m{ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
            print("\n")

            for notn in range(1, 13):
                for bim in range(2, 15, 4):
                    bimnot = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                    pontos += int(bimnot)
                    num.append(bimnot)
                    print(f"{bimnot}", end=" ")

                print()

            #for sec in range(1, 13):
            #    bim2 = wait.until(EC.presence_of_all_elements_located(
            #        (By.XPATH, f"/html/body/div/div/div[4]/table/tbody/tr[{sec}]/td[6]")))[0].text
            #    print(bim2)
            #for ter in range(1, 13):
            #    bim3 = wait.until(EC.presence_of_all_elements_located(
            #        (By.XPATH, f"/html/body/div/div/div[4]/table/tbody/tr[{ter}]/td[10]")))[0].text
            #    print(bim3)
            #for qua in range(1, 13):
            #    bim4 = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"/html/body/div/div/div[4]/table/tbody/tr[{qua}]/td[14]")))[0].text
            #    print(bim4)

        except:
            print("\n\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()
print(f"\033[33mPontos totais {pontos}\033[m"
      f"\n\033[32mMédia do aluno total: {pontos/int(num.count()):.2f}")
