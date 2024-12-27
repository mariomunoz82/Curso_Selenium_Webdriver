import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path


class base_test(unittest.TestCase):

    def setUp(self) :
        self.service=webdriver.ChromeService(executable_path=binary_path)
        self.driver=webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        t=2
    
    def test_compra_succesful (self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'user-name')]"))).send_keys("standard_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'password')]"))).send_keys("secret_sauce")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'login-button')]"))).click()
        time.sleep(1.5)
        
        mensaje=driver.find_element('xpath',"//span[@class='title'][contains(.,'Products')]").text
        if mensaje=='Products':
            print("Se ha logueado correctamente a la tienda en linea\n")
        else:
            print("Usted no se ha logueado a la tienda, favor verifique")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[contains(@class,'shopping_cart_link')]"))).click()
        print("El carrito esta vacio, favor realize una compra\n")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'continue-shopping')]"))).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-backpack')]"))).click()
        time.sleep(0.6)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-onesie')]"))).click()
        time.sleep(0.6)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'add-to-cart-test.allthethings()-t-shirt-(red)')]"))).click()
        time.sleep(0.6)
        
        labs_backpack=driver.find_element('xpath',"//button[contains(@id,'remove-sauce-labs-backpack')]").text
        labs_onesie=driver.find_element('xpath',"//button[contains(@id,'remove-sauce-labs-onesie')]").text
        t_shirt_red=driver.find_element('xpath',"//button[contains(@id,'remove-test.allthethings()-t-shirt-(red)')]").text

        if labs_backpack=='Remove':
            print("labs-backpack fue añadido al carrito de compras\n")
        if labs_onesie=='Remove':
            print("labs-onesie fue añadido al carrito de compras\n")

        if t_shirt_red=='Remove':
            print("t_shirt_red fue añadido al carrito de compras\n")
        else:
            print("Uno de los productos no fue añadido a la lista")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='shopping_cart_link'][contains(.,'3')]"))).click()

        carrito=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title'][contains(.,'Your Cart')]"))).text
        if carrito=='Your Cart':
            print("Estas en el carrito de compras\n")
        else:
            print("No estas en el carrito de compras\n")

        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'remove-test.allthethings()-t-shirt-(red)')]"))).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'checkout')]"))).click()

        time.sleep(2)

        nom=driver.find_element("xpath","//input[contains(@id,'first-name')]")
        nom.send_keys("Mario" + Keys.TAB +"Muñoz" + Keys.TAB + "503")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'continue')]"))).click()

        time.sleep(8)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'finish')]"))).click()

        compra=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//h2[@class='complete-header'][contains(.,'Thank you for your order!')]"))).text
        time.sleep(2)
        if compra=='Thank you for your order!':
            print("La compra se realizo con exito\n")
        else:
            print("No se pudo realizar la compra\n")
    """
    def test_sesion_expirada(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'user-name')]"))).send_keys("standard_user")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'password')]"))).send_keys("secret_sauce")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'login-button')]"))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(@id,'add-to-cart-sauce-labs-backpack')]"))).click()

        time.sleep(180)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='shopping_cart_link'][contains(.,'1')]"))).click()

        error_logueo=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//h3[contains(@data-test,'error')]"))).text
        if error_logueo=="Epic sadface: You can only access '/cart.html' when you are logged in.":
            print("Prueba exitosa")
    """    


    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()