# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:51:33 2023


@author: Mario
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()

t=2

driver.get("https://testpages.herokuapp.com/basic_html_form.html")

driver.find_element("xpath","//input[contains(@type,'text')]").send_keys("mam38" + Keys.TAB + "mam42" + Keys.TAB + "Este es el primer reto del curso de selenium")

driver.find_element("xpath","//input[contains(@type,'file')]").send_keys("E:\Cursos Udemy\Selenium con Python\Proyectos\Curso Selenium\Curso Selenium\Imagenes\demo1.jpg")
driver.find_element("xpath","//input[contains(@value,'cb1')]").click()
time.sleep(t)
driver.find_element("xpath","//input[contains(@value,'cb2')]").click()
time.sleep(t)
driver.find_element("xpath","//input[contains(@value,'cb3')]").click
driver.find_element("xpath","//input[contains(@value,'rd3')]").click()

try:
    lista=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[7]/td[1]/select[1]")))
    lista=Select(driver.find_element("xpath","//tbody/tr[7]/td[1]/select[1]"))
    lista.select_by_index(1)
    lista.select_by_index(3)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no fue encontrado")

lista2=Select(driver.find_element("xpath","//select[contains(@name,'dropdown')]"))    
lista2.select_by_index(3)

driver.find_element("xpath","//input[contains(@type,'submit')]").click()

time.sleep(2)

driver.close()