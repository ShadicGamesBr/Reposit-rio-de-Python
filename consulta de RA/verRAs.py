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
disciplinas = ['Arte', 'Biologia', 'Filosofia', 'Física', 'Geografia', 'História', 'Inglês', 'Português', 'Matemática', 'Química', 'Sociologia']
#boletim = {"bimestre1":[], "bimestre2":[],"bimestre":[],"bimestre":[]}
for ano in range(2015, 2022):
    try:
        try:
            print(f"Ano de \033[34m{ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
            print("\n")

            for notn in range(1, 13):
                print(f'\033[36m{disciplinas[notn]}\033[m', end=" :")
                for bim in range(2, 15, 4):
                    bimnot = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]'))).text
                    pontos += int(bimnot)
                    num.append(bimnot)
                    print(f"{bimnot}", end=" ")

                print()
        except:
            print("\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()

print(f"\033[33mPontos totais {pontos}\033[m"
          f"\n\033[32mMédia do aluno total: {pontos/int(len(num)):.2f}")
for quant in range(10, -1, -1):
    print(f"Quantidade de {quant}: {num.count(f'{quant}')}")

