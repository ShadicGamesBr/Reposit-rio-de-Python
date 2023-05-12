{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7adb8cbe-b867-470f-b773-8480ea5c708d",
   "metadata": {
    "is_executing": true
   },
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import matplotlib\n",
    "\n",
    "ra = str(input(\"RA do aluno: \")).strip()\n",
    "data = str(input(\"Data de nascimento: \")).strip()\n",
    "digito = str(input(\"Dígito verificador: \")).strip()\n",
    "driver = webdriver.Chrome()\n",
    "wait = WebDriverWait(driver, 4)\n",
    "#texto = open(\"resultados_Felipe.txt\", \"a\")\n",
    "resultados = []\n",
    "#data = f\"{data[0:2]+'/'+data[3:5]+'/'+data[6:10]}\"\n",
    "\n",
    "for ano in range(2015, 2022):\n",
    "    try:\n",
    "        print(f\"Ano de {ano}\")\n",
    "\n",
    "        driver.get(\n",
    "            f\"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}\")\n",
    "        print(\"\\n\")\n",
    "\n",
    "        elementos = wait.until(EC.presence_of_all_elements_located((By.XPATH, \"/html/body/div/div/div[4]/table\")))\n",
    "        frase = elementos[0]\n",
    "        print(frase.text)\n",
    "\n",
    "    except:\n",
    "        print(\"\\033[31mAno indisponível\\033[m\")\n",
    "    #if len(elementos) > 0:\n",
    "    #    frase = elementos[0]\n",
    "    #    print(frase.text)\n",
    "    #else:\n",
    "    #    print(\"Ano não disponível\")\n",
    "\n",
    "    print(\"\\n\\n\\n\")\n",
    "driver.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b88548e7-022a-44b8-be25-a7dc3093117c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
