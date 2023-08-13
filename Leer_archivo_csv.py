# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:51:38 2023

@author: Mario
"""

import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import pandas as pd

driver=webdriver.Chrome('C:\Drivers\chromedriver.exe')

df=pd.read_csv("DatosAlumnos.csv", encoding='latin-1')
t=.5

dict_lenguaje={"PHP":"//label[contains(@id,'wsf-1-label-42-row-1')]",
               "PYTHON": "//label[contains(@id,'wsf-1-label-42-row-2')]",
               "JS": "//label[contains(@id,'wsf-1-label-42-row-3')]"}

dict_radio={"CypressIO": "//label[contains(@id,'wsf-1-label-44-row-1')]",
            "WebdriverIO": "//label[contains(@id,'wsf-1-label-44-row-2')]",
            "Selenium": "//label[contains(@id,'wsf-1-label-44-row-3')]"}
#print(dict_radio["SeleniumIO"])

for row, datos in df.iterrows():
    nombre=datos["Nombre"]
    apellido=datos["Apellido"]
    email=datos["email"]
    telefono=datos["phone"]
    direccion=datos["Direccion"]
    lenguaje=datos["Lenguaje"]
    radio=datos["Radio"]
    
    driver.get("https://testingqarvn.com.es/radio-buttons/")
    driver.find_element("xpath","//input[contains(@id,'wsf-1-field-37')]").send_keys(nombre)
    time.sleep(t)
    driver.find_element("xpath","//input[contains(@id,'wsf-1-field-38')]").send_keys(apellido)
    time.sleep(t)
    driver.find_element("xpath","//input[contains(@id,'wsf-1-field-39')]").send_keys(email)
    time.sleep(t)
    driver.find_element("xpath","//input[contains(@id,'wsf-1-field-40')]").send_keys(telefono)
    time.sleep(t)
    driver.find_element("xpath","//textarea[contains(@id,'wsf-1-field-41')]").send_keys(direccion)
    time.sleep(t)
    driver.find_element("xpath",dict_lenguaje[lenguaje]).click()
    time.sleep(t)
    driver.find_element("xpath",dict_radio[radio]).click()
    driver.find_element("xpath","//button[contains(@id,'wsf-1-field-43')]").click()
    
    


driver.close()