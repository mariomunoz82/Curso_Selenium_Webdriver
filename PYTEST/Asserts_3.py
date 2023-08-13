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
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t=.8


@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "txtUsername", "Admin", t)
    f.Texto_Mixto("id", "txtPassword", "admin123", t)
    f.Click_Mixto("id", "btnLogin", t)
    #print("Entrando al sistema")


def teardown_function():
    print("Fin de todos los Test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    etiqueta=f.SEX("//h1[contains(.,'Dashboard')]").text
    print(etiqueta)
    if(etiqueta=="Dashboa"):
        print("Adentro")
        assert etiqueta=="Dashboard"

    else:
        print("Afuera")
        assert etiqueta=="Dashboa", "No estas en la pagina de inicio"


