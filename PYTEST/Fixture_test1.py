# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:28:47 2023

@author: Mario
"""

import time
import pytest
from selenium import webdriver
from PYTEST.Funciones import Funciones_Globales


driver=""
def SetUp_Function(function):
    global driver
    driver=webdriver.Chrome("C:/Drivers/chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    print("Iniciando nuestros test")
    
def teardown_function(function):
    print("Fin de los test")
    driver.close()
