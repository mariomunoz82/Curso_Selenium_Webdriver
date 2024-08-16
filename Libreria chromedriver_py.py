from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time

service=webdriver.ChromeService(executable_path=binary_path)
driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/")
time.sleep(5)

driver.quit()