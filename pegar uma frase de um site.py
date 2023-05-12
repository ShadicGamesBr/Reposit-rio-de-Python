from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
texto = open("R.AsCaçados.txt", "a")
for raNum in range(106090000, 107409999):
#for raNum in range(107058872, 107058877):
    try:

        ano = "2019"
        digito = 1
        #raNum = "000107058871"
        data = "22/06/2004"
        driver = webdriver.Chrome()
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa=000{+raNum}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={ano}")
        wait = WebDriverWait(driver, 8)
        nome = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]")))
        print(f"\033[32m{nome.text}\033[m")
        print(f"\033[32m{raNum}\033[m")
        texto.writelines(f"Nome: {nome.text}, RA: {raNum},Data: {data}, Digito: {digito}\n")
        texto.flush()
        driver.close()
        sleep(10)

    except:
        print(f"\033[31mRA de 000{raNum} Não deu certo\033[m")

print("\033[36mFim do programa\033[m")
