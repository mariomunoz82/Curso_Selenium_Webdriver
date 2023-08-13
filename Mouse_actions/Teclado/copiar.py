# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:23:15 2023

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


t=.9
class base_test(unittest.TestCase):

    def setUp(self) :
        self.driver=webdriver.Chrome('C:\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        

    def test1 (self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form",t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'firstName')]", "Juan", t)
        act=ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up((Keys.CONTROL)).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys("c").key_up((Keys.CONTROL)).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up((Keys.CONTROL)).perform()
        time.sleep(2)
        
        

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
        