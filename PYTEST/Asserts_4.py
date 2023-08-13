import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
# from Funciones import Funciones_Globales
# from Page_Login import Funciones_Login
# from selenium.webdriver import ActionChains
t=.8


@pytest.mark.run
def test_validar_if():
    print("Primer test")
    assert True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b, "No son iguales"
    assert a!=b, "Son iguales"
    assert a<b, "A no es menor que B"
    assert a>b, "A no es menor que B"


@pytest.mark.run
def test_tres():
    a=5
    b=10
    assert a==b, "No son iguales"

@pytest.mark.run
def test_cuatro():
    a=15
    b=10
    assert a>b, " a no es mayor que b"

@pytest.mark.run
def test_cinco():
    nombre="Rodri"

    assert nombre=="Rodrigo", "El nombre no es Rodrigo"


