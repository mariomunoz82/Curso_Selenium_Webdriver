# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:53:56 2023

@author: Mario
"""

import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from PYTEST.Funciones import Funciones_Globales

class Funciones_Login():

    def __init__(self,driver) :
        self.driver=driver
        
    def l1(self,email,clave,message):
        self.driver.maximize_window()
        f = Funciones_Globales(self.driver)
        f.Navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',2)
        f.Texto_Mixto("xpath" , "//input[contains(@id,'Email')]",email,.9)
        f.Texto_Mixto("xpath","//input[contains(@id,'Password')]",clave,.9)
        f.Clic_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",.9)
        e1=f.sex("//li[contains(.,'No customer account found')]")
        e1=e1.text
        print(e1)
        if (e1==message):
            print("Prueba de validacion exitosa")
        else:
            print("La prueba de validacion es exitosa") 
            
        
    def l2(self,email,clave,message):
        self.driver.maximize_window()
        f = Funciones_Globales(self.driver)
        f.Navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F', 2)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, .9)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, .9)
        f.Clic_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", .9)
        e1 = f.sex("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de email vacion correcta")
        else:
            print("La prueba de email vacio no pasa")
    
    def l3(self,email,clave,message):
        self.driver.maximize_window()
        f = Funciones_Globales(self.driver)
        f.Navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F', 2)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, .9)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, .9)
        f.Clic_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", .9)
        e1 = f.sex("//h1[contains(.,'Dashboard')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Prueba de Login Exitosa")
        else:
            print("Prueba Erronea")