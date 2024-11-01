# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service=webdriver.ChromeService(executable_path=binary_path)
driver=webdriver.Chrome(service=service)
try:
    
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[contains(@id,'firstName')]"))).send_keys("Mario")
    time.sleep(1)
    driver.find_element('xpath',"//input[contains(@id,'lastName')]").send_keys("Muñoz")
    time.sleep(1)
    driver.find_element('xpath',"//input[contains(@id,'userEmail')]").send_keys("marioalexis.2007@gmail.com")
    driver.find_element('xpath',"//label[@for='gender-radio-1'][contains(.,'Male')]").click()
    time.sleep(0.7)
    driver.find_element('xpath',"//input[contains(@id,'userNumber')]").send_keys("7585129700")
    time.sleep(0.7)
    driver.find_element('xpath',"//input[contains(@id,'dateOfBirthInput')]").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("April")
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1990" + Keys.RETURN)
    driver.find_element(By.XPATH,"//div[contains(@class, 'react-datepicker__day--015')]").click()
    time.sleep(1)
    
    driver.find_element('xpath',"//textarea[contains(@id,'currentAddress')]").send_keys("Direccion Falsa 1 2 3 y 4")
    time.sleep(0.7)
    
    driver.find_element(By.ID,"react-select-3-input").send_keys("NCR" + Keys.RETURN)
    time.sleep(0.7)
    
    driver.find_element('xpath',"//button[contains(@id,'submit')]").click()
    time.sleep(2)  
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'modal-header')]")))
    
finally:
    driver.quit()