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

    def pagina(self):
        driver=self.driver
        driver.get("https://books.toscrape.com/")
        time.sleep(1)

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()