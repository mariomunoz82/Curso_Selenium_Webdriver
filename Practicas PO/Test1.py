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
from Funciones.Page_Login import Pagina_Login

tg=.9
class base_test(unittest.TestCase):

    def setUp(self) :
        self.driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        
        

    def test1 (self):
        driver=self.driver
        f=Funciones_Globales(driver)
        # pg=Pagina_Login(driver)
        # pg.Login_Master("https://www.saucedemo.com/", "Rodrigo", "admin123", 1)
        f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", tg)
        #f.Select_Xpath_text("//select[contains(@name,'dropdown')]", "Drop Down Item 4", tg)
        #f.Select_Xpath_type("//select[contains(@name,'dropdown')]", "value", "dd5", tg)
        f.Upload_Xpath("//input[contains(@id,'fileinput')]", "E:\Cursos Udemy\Selenium con Python\Proyectos\Curso Selenium\Curso Selenium\Imagenes\demo1.jpg", tg)
        f.Clic_Mixto("id", "itsanimage", tg)
        f.Clic_Mixto("xpath", "//input[contains(@type,'submit')]", tg)
        # f.Clic_Xpath_Valida("//input[contains(@id,'itsanimage')]", tg)
        # f.Clic_Xpath_Valida("//input[contains(@type,'submit')]", tg)
        #f.Check_ID("wsf-1-label-36-row-1", tg)
        # for n in range(1,4):
        #     f.Check_Xpath_Multiples(2, "//label[contains(@for,'wsf-1-field-36-row-"+str(n)+"')]")
        
        # f.Texto_Mixto("xpath", "//input[contains(@id,'userName')]", "Mario", tg)
        # f.Texto_Mixto("id", "userEmail", "marioalexis.2007@gmail.com", tg)
        # f.Clic_Mixto("id", "submit", tg)
        
        f.salida()
        
       

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
        