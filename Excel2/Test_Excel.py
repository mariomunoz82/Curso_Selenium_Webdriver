# -*- coding: utf-8 -*-
"""
Created on Fri May 26 07:38:53 2023

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
from ..Funciones.Funciones import Funciones_Globales
from Funciones_Ex import *

tg=.3
class base_test(unittest.TestCase):

    def setUp(self) :
        self.driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        t=tg

    def test1 (self):
        driver=self.driver
        f=Funciones_Globales(driver)
        fe=Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        ruta="E:\Cursos Udemy\Selenium con Python\Proyectos\Curso Selenium\Curso Selenium\Excel2\Datos_ok.xlsx"
        filas=fe.getRowCount(ruta, "Hoja1")
        
        for r in range(2,filas+1):
            nombre=fe.readData(ruta, "Hoja1", r, 1)
            email=fe.readData(ruta, "Hoja1", r, 2)
            dir1=fe.readData(ruta, "Hoja1", r, 3)
            dir2=fe.readData(ruta, "Hoja1", r, 4)
            
            f.Texto_Mixto("id", "userName", nombre, tg)
            f.Texto_Mixto("id", "userEmail", email, tg)
            f.Texto_Mixto("id", "currentAddress", dir1, tg)
            f.Texto_Mixto("id", "permanentAddress", dir2, tg)
            f.Clic_Mixto("id", "submit", tg)
            
            e=f.Existe("id", "name",tg )
            if e=="Existe":
                print("El elemento se inserto correctamente")
                fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Hoja1", r, 5, "Error")

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()