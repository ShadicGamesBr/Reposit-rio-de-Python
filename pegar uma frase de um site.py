from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa=000107058875&nrDigRa=1&dsUfRa=SP&dtNascimento=23/06/2003&nrAnoLetivo=2020")

wait = WebDriverWait(driver, 20)
frase = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]")))
print(frase.text)
