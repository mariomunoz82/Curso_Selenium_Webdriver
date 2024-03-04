# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:03:32 2023

@author: Mario
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

t=0.8

opts=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/automation-practice-form')
sleep(2)
driver.maximize_window()


pm=driver.find_element(By.XPATH,"//input[contains(@id,'firstName')]")
pm.clear()
pm.send_keys("Mario")
print("Ingresando al elemento: {}".format(pm))
sleep(t)

pa=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[contains(@id,'lastName')]")))
pa.clear()
pa.send_keys("Munoz")
sleep(t)


email=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//input[contains(@id,'userEmail')]")))
email.clear()
email.send_keys("marioalexis.2007@gmail.com")
sleep(t)


driver.execute_script("window.scrollTo(0,100)")
gender=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//label[@for='gender-radio-1'][contains(.,'Male')]")))
gender.click()
sleep(t)

driver.execute_script("window.scrollTo(0,300)")

phone =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'userNumber')]")))
phone.clear()
phone.send_keys("202206761")


DoB=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id,'dateOfBirthInput')]")))
DoB.clear()

calendar=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'day--today')]")))
calendar.click()
sleep(1)


hobbies=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]")))
hobbies.click()
sleep(t)


hobbies=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//label[@for='hobbies-checkbox-3'][contains(.,'Music')]")))
hobbies.click()
sleep(t)

picture=driver.find_element(By.XPATH,"//input[contains(@id,'uploadPicture')]")
picture.send_keys("C:/Users/Mario/Pictures/demo1.jpg")
sleep(2)

driver.execute_script("window.scrollTo(0,2000)")
CurrentA=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//textarea[contains(@id,'currentAddress')]")))
CurrentA.clear()
CurrentA.send_keys("Direccion1")

driver.execute_script("window.scrollTo(2000,7000)")
state=Select(driver.find_element(By.ID,"#state"))
state.select_by_index(1)
sleep(1.2)


driver.close()