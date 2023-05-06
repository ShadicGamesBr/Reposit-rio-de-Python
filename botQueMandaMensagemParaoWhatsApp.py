from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(r"C:\Users\ShadicGamesBr\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://web.whatsapp.com/")

# aguarda até que o usuário faça login escaneando o QR code
input("Pressione enter após escanear o código QR")

# busca e clica no contato/grupo desejado
contato = driver.find_element(By.XPATH, '//*[@title="Felipe Kauan"]')
contato.click()

# espera até que o campo de mensagem esteja disponível
input_box = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
)

# envia a mensagem
input_box.send_keys("sua mensagem" + Keys.ENTER)
