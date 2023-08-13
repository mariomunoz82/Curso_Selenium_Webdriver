# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:58:11 2023

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
from selenium.webdriver import ActionChains


t=2
class base_test(unittest.TestCase):

    def setUp(self) :
        #self.driver=webdriver.Chrome('C:\Drivers\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        

    def test1 (self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons",t)
        
        ''' elemento1=driver.find_element("id","doubleClickBtn")
        act=ActionChains(driver)
        act.double_click(elemento1).perform()
        time.sleep(t)'''
        
        f.Click_Derecho("id", "rightClickBtn")
        

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
        