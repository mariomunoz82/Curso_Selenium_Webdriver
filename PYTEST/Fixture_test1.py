import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
t=.5
driver=""
f=""

def SetUp_Function(function):
    global driver, f
    options = Options()
    driver=webdriver.Chrome(options=options)
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    driver.implicitly_wait(20)
    print("Inicando nuestros test")
    
def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    f = Funciones_Globales(driver)
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchProductName')]", "computer", t)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-products')]", t)

def test_dos():
    #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath","//a[@href='/Admin/Product/Create']",t)
    f.Texto_Mixto("xpath","//input[@id='Name']","Laptop Dell",t)
    f.Texto_Mixto("xpath","//textarea[contains(@id,'ShortDescription')]","Laptop modelo nuevo tipo dell",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    f.Click_Mixto("xpath","//div[@class='tox-collection__item-label'][contains(.,'New document')]",t)
    driver.switch_to.frame(0)
    #f.Texto_Mixto("id","tinymce","Descripción Larga",t)
    campo=driver.find_element_by_id("tinymce")
    campo.send_keys("Descripción Larga"+Keys.TAB+"34567")
    time.sleep(4)
    #f.Texto_Mixto("xpath","//input[contains(@id,'Sku')]","5464",t)