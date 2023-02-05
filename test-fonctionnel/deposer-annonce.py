import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import xlsxwriter
import os
from datetime import datetime

PATH = "web Drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = "http://localhost:3000"
driver.get(url)
start_time = time.time()

annonce = {
    "title" : "Annonce de teste",
    "description" : "une annonce d'un immobilier",
    "surface" : "200",
    "prix" : "20000000",
    "wilaya" : "16",
    "commune" : "1",
    "link" : "https://maps.app.goo.gl/yg7wPM9UvZxqNvEG9"
}

try:
    # ------------------------------ Authentification ----------------------------------
    google = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.ID, "Signin")))
    account = driver.find_element(By.TAG_NAME, 'iframe')
    account.click()

    # ------------------------------ Coordonnées d'authentification ----------------------------------
    main_window_handle = driver.current_window_handle
    window_handles = driver.window_handles
    for handle in window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            break
    email = WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    print("a", email[0].text, "a")
    email.send_keys("kw_aissaoui@esi.dz")
    driver.switch_to.window(main_window_handle)
    # ------------------------------ Publier Annonce ----------------------------------
    button = WebDriverWait(driver, 200).until(EC.presence_of_all_elements_located((By.ID, "publier")))
    button.click()
    sections = WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "infos")))
    inputs = []
    sections[0].find_element(By.TAG_NAME, "input").send_keys(annonce["title"])
    sections[1].find_element(By.TAG_NAME, "input").send_keys(annonce["description"])
    sections[2].find_element(By.TAG_NAME, "input").send_keys(annonce["surface"])
    sections[3].find_element(By.TAG_NAME, "input").send_keys(annonce["prix"])
    sections[6].find_element(By.TAG_NAME, "input").send_keys(annonce["link"])
    send = WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "send")))
    send.click()
    print("Temps d'éxécution : --- %s seconds ---" % (time.time() - start_time))
    print(" *****************************  END  *****************************")

except Exception as e:
    print(e)
    print("\n \n --- FIN SCRIPT WITH ERROR -- \n \n")
driver.quit()
