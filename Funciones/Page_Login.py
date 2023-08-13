# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:17:39 2023

@author: Mario
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 12 01:16:30 2023

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
from Funciones.Funciones import Funciones_Globales

class Pagina_Login():

    def __init__(self,driver) :
        self.driver=driver
        
    def Login_Master(self,Url,texto,clave,Tiempo):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar(Url, Tiempo)
        f.Texto_Xpath_Valida("//input[contains(@id,'user-name')]", texto, Tiempo)
        f.Texto_Xpath_Valida("//input[contains(@id,'password')]", clave, Tiempo)
        f.Clic_Xpath_Valida("//input[contains(@id,'login-button')]", Tiempo)

