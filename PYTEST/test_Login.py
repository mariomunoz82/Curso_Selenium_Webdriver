# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:27:42 2023

@author: Mario
"""

import time
import pytest
from selenium import webdriver
from PYTEST.Funciones import Funciones_Globales
from PYTEST.Page_Login import Funciones_Login

def test_Login1():
    driver=webdriver.Chrome("C:/Drivers/chromedriver.exe")
    fl=Funciones_Login(driver)
    fl.l1("mario.munoz@equifax.com","1234","No customer account found")
    fl.l2("", "1234566", "Please enter your email")
    fl.l3("admin@yourstore.com", "admin", "Dashboard")
    driver.close()   
 

    

    

   
    

    
