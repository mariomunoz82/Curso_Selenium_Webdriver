# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:40:09 2023

@author: MARIO
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

#driver=webdriver.Chrome("C:/Drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)


driver.get('https://demoqa.com/text-box')
driver.maximize_window()
t=1.2
#driver.implicitly_wait(10) # Espera un tiempo determinado para poder localizar un objeto


#*********SELECTORES por XPATH***************************
nom=driver.find_element("xpath","//input[contains(@id,'userName')]")
nom.send_keys("Mario")
time.sleep(t)

driver.find_element("xpath","//input[contains(@id,'userEmail')]").send_keys("marioalexis.2007@gmail.com")
time.sleep(t)

driver.find_element("xpath","//textarea[contains(@id,'currentAddress')]").send_keys("Direccion1")
time.sleep(t)

driver.find_element("xpath","//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion2")
time.sleep(t)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

driver.find_element("xpath","//button[contains(@id,'submit')]").click()
time.sleep(t) 

#*********SELECTORES POR ID***************************
"""nom=driver.find_element("id","userName").send_keys("Mario")
time.sleep(1)

nom=driver.find_element("id","userEmail").send_keys("marioalexis.2007@gmail.com")
time.sleep(1)

nom=driver.find_element("id","currentAddress").send_keys("Direccion1")
time.sleep(1)

nom=driver.find_element("id","permanentAddress").send_keys("Direccion2")
time.sleep(1)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

nom=driver.find_element("id","submit").click()
time.sleep(3)"""

#**************SELECTORES POR CSS*********

"""nom=driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("Mario")
time.sleep(1)

nom=driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("marioalexis.2007@gmail.com")
time.sleep(1)"""

#************KEYS.TAB*****

"""nom=driver.find_element("xpath","//input[contains(@id,'userName')]")
nom.send_keys("Mario")
nom.send_keys(Keys.TAB + "marioalexis.2007@gmail.com" + Keys.TAB + "Direccion1" + Keys.TAB + "Direccion2" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(4)"""

#**************Test de Navegacion*******************

"""driver.get("https://www.youtube.com/watch?v=E-u_uSJcWm0")
time.sleep(t)

driver.get("https://es.savefrom.net/254/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(2)")
time.sleep(t)"""

# test con explicity wait
"""driver.get("https://www.seleniumeasy.com/selenium-tutorials/click-element-using-javascriptexecutor")

btn=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"")))
btn.click()"""

#******************* TEST CON CHECKBOX************************
'''driver.get('https://testingqarvn.com.es/prueba-de-campos-checkbox/')

nom1=driver.find_element("xpath","//input[contains(@id,'wsf-1-field-29')]")
nom1.send_keys("Mario")
nom1.send_keys(Keys.TAB + "Muñoz" + Keys.TAB + "marioalexis.2007@gmail.com" + Keys.TAB + "222206761" + Keys.TAB + "Direccion1")

driver.find_element("id","wsf-1-label-36-row-2").click()

driver.find_element("id","wsf-1-label-36-row-3").click()

driver.find_element("id","wsf-1-field-34").click()

btn0=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//label[contains(@id,'wsf-1-label-36-row-1')]")))
btn0.click()

time.sleep(t)'''


#************* TEST CON COMBO BOX********************************************

'''driver.get('https://testingqarvn.com.es/combobox/')

ds=Select(driver.find_element("xpath","//select[contains(@id,'wsf-1-field-53')]"))
#ds=Select(diaSelect)

ds.select_by_visible_text("Linux")
time.sleep(t)

ds.select_by_index(2)
time.sleep(t)

ds.select_by_value("Windows")
time.sleep(t)

# Se Aplica el mismo metodo para los elementos MULTI SELECT'''

#************* TRY CATCH********************
"""driver.get('https://testingqarvn.com.es/combobox/')

try:
    ds=Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//select[@id='wsf-1-field-53']"))))
    ds.select_by_index(0)
    time.sleep(t)
    ds.select_by_index(1)
    time.sleep(t)
    ds.select_by_index(2)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no fue encontrado")
    

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='wsf-1-field-45']"))).send_keys("Mario")
time.sleep(t)"""

#******************UPLOAD FILES******************************/
"""driver.get('https://testpages.herokuapp.com/styled/file-upload-test.html')

try:
    Buscar=WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='fileinput']")))
    Buscar.send_keys("E:\Cursos Udemy\Selenium con Python\Proyectos\Curso Selenium\Curso Selenium\Imagenes\demo1.jpg")
    time.sleep(t)
    driver.find_element("xpath","//input[@id='itsanimage']").click()
    driver.find_element("xpath","//input[@type='submit']").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no fue encontrado")"""
    
#*************TEST SCROLL SOBRE EL ELEMENTO********************************
    
'''driver.get('https://pixabay.com/es/')

try:
    Buscar=WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,'Descubre más')]")))
    Buscar=driver.find_element("xpath","//span[contains(text(),'Descubre más')]")
    driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(10)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no fue encontrado")'''
    
 #*************TEST LINK********************************   
'''driver.get("https://www.seleniumeasy.com/")   
links=driver.find_elements(By.TAG_NAME,"a")

print("El numero de links que hay en la pagina es: ",len(links))

for num in links:
    print(num.text)
    
driver.find_element(By.LINK_TEXT,"Selenium").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Selenium with Java").click()
time.sleep(3)'''

#************* ALERTS MODAL*********************

'''driver.get("https://testpages.herokuapp.com/alerts.html")

driver.find_element("xpath","//input[contains(@id,'confirmexample')]").click()
time.sleep(5)'''

# ************* CONDICIONALES CON IF****************
'''driver.get("https://demoqa.com/")
titulo=driver.find_element("xpath","//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())

btn1=driver.find_element("xpath","(//div[contains(@class,'card-up')])[1]")

if (titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(t)
else:
    print("No existe la imagen")

driver.get("https://demoqa.com/text-box")
btn=driver.find_element("xpath","//button[@type='button'][contains(.,'Submit')]")
print(btn.is_enabled())

if(btn.is_enabled()==True):
    print("Puedes dar click")
else:
    print("No puedes dar click")'''

# ************* validar por valor de texto***************
# driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
# btn=driver.find_element("xpath","//button[@type='submit'][contains(.,'Send')]")
# btn.click()
# time.sleep(t)

# name_val=driver.find_element("xpath","//small[@class='help-block'][contains(.,'Please supply your first name')]")
# name=name_val.text
# #print("El valor del error es: "+name)
# if name=="Please supply your first name":
#     #print("Falta el nombre")
#     cn=driver.find_element ("xpath","//input[contains(@name,'first_name')]")
#     cn.send_keys("Rodrigo")
#     time.sleep(2)
#     print("Nombre correcto")
# else:
#     print("Falta el nombre")

# time.sleep(t)
# ap_val=driver.find_element("xpath","//small[@class='help-block'][contains(.,'Please supply your last name')]")
# ap=ap_val.text
# #print("El valor del error es: "+name)
# if ap=="Please supply your last name":
#     ap=driver.find_element("xpath","//input[contains(@name,'last_name')]")
#     ap.send_keys("Villanueva")
#     time.sleep(2)
#     print("Ap Correcto")
# else:
#     print("Falta el apellido")

# print(btn.is_enabled())
# if(btn.is_enabled()==False):
#     print("Faltan campos por llenar")
# else:
#     print("Listo todo ok")
    
driver.close()

