# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 00:49:15 2023

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
        self.driver=webdriver.Chrome('C:\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        

    def test1 (self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",t)
        
        f.Texto_Mixto("xpath", "//input[contains(@class,'oxd-input oxd-input--focus')]", "Admin", t)
        f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
        f.Clic_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
        
        menu1=driver.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")
        menu2=driver.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]")
        menu3=driver.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[6]/a[1]")
        
        act=ActionChains(driver)
        act.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).click().perform()
        
        
        

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
        
        