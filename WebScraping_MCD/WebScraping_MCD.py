# !pip install selenium
# !pip install webdriver-manager
# !pip install BeautifulSoup

# Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Navigation options
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Initializing web browser
driver.get('https://mcd.unison.mx/')
   
# get element 
element = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div/div/nav/div/ul/li[2]/a')
   
# create action chain object
action = ActionChains(driver)
   
# click the item
action.move_to_element(element).perform()
time.sleep(1)

# step 2
element = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div/div/nav/div/ul/li[2]/ul/li[1]/a')
action = ActionChains(driver)
action.click(element).perform()
time.sleep(1)

# Size of the window
driver.execute_script("window.scrollTo(0,2400)")
time.sleep(1)

element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/main/article/div/ul/li[6]/a')
action = ActionChains(driver)
action.click(element).perform()
time.sleep(1)

driver.execute_script("window.scrollTo(0,630)")
time.sleep(1)

page = requests.get(driver.current_url)
soup = BeautifulSoup(page.content, 'html.parser')

tabla = soup.find('div', {"class": "entry-content"}).find_all('li')

# List
listaEstudiantes = list()

for i in range(len(tabla)):
    estudiante = tabla[i].string
    listaEstudiantes.append(estudiante)
    

# Dataframe
df = pd.DataFrame({'ASPIRANTES ACEPTADOS 2022': listaEstudiantes})

df.to_csv('Lista_Estudiantes.csv', index=False, encoding='UTF-16le')

driver.quit()