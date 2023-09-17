from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from features.Funciones import Funciones_Globales


@given(u'Abriendo el navegador')
def step_impl(context):
    global driver,f
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)
    f=Funciones_Globales(context.driver)
    f.Navegar("https://demoqa.com/text-box",1)


@when(u'Cargando el nombre del "{user}"')
def step_impl(context,user):
    print(u'STEP: When Cargando el nombre del usuario')
    f.Texto_Mixto("xpath","//input[contains(@id,'userName')]",user,0.5)


@then(u'Cargando su "{email}".')
def step_impl(context,email):
    print(u'STEP: Then Cargando su email.')
    f.Texto_Mixto("xpath","//input[contains(@id,'userEmail')]",email,0.5)


@then(u'Cargando la "{direccion}"')
def step_impl(context,direccion):
    print(u'STEP: Then Cargando su direccion')
    f.Texto_Mixto("xpath","//textarea[contains(@id,'currentAddress')]",direccion,0.5)
    context.driver.close()