# -*- coding: utf-8 -*-
"""
Created on Fri May 12 01:16:30 2023

@author: Mario
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

class Funciones_Globales():

    def __init__(self,driver) :
        self.driver=driver

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t
    
    def Navegar(self,Url,Tiempo):
        self.driver.get(Url)
        #self.driver.maximize_window()
        print("Ingresando a la url "+str(Url))
        t=time.sleep(Tiempo)
        return t
    
    def sex(self,selector):
        val=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,selector)))
        #val=self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val=self.driver.find_element("xpath",selector)
        return val
        
    def SEI(self,selector):
        val=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,selector)))
       # val=self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val=self.driver.find_element("id",selector)
        return val
              
    def Select_Xpath_type(self,xpath,tipo,dato,Tiempo):
        try:
            val=self.sex(xpath)
            val=Select(val)
            if tipo=="text":
                val.select_by_visible_text(dato)
            elif tipo=="index":
                val.select_by_index(dato)
            elif tipo=="value":
                val.select_by_value(dato)
            print("El campo seleccionado es {}".format(dato))
            t=time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se pudo encontrar el elemento",xpath)  
           
    def Upload_Xpath(self,xpath,ruta,Tiempo):
        
        try:
            val=self.sex(xpath)
            val.send_keys(ruta)
            print("Se carga la imagen de {}".format(ruta))
            t=time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se pudo encontrar el elemento",xpath)     
        
    def Check_ID(self,id,Tiempo):
        try:
            val=self.SEI(id)
            val.click()
            print("Click en el elemento {}".format(id))
            t=time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se pudo encontrar el elemento",id)
            
    def Check_Xpath_Multiples(self,Tiempo,*args):
        
        try:
            for num in args:
                val=self.sex(num)
                val.click()
                print("Click en el elemento {}".format(num))
                t=time.sleep(Tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se pudo encontrar el elemento",num) 
         
    def Texto_Mixto(self,tipo,selector,texto,Tiempo):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector,texto))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector,texto))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
                
    def Click_Mixto(self,tipo,selector,Tiempo):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                val.click()
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)  
                
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                val.click()
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)  
                
    def Existe(self,tipo,selector,Tiempo):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                print("El elemento {} -> existe  ".format(selector))
                t=time.sleep(Tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
                return "No Existe"
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                print("El elemento {} -> existe  ".format(selector))
                t=time.sleep(Tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
                return "No Existe"
            
                
    def salida(self):
        print("se termina la prueba exitosamente")
             
            
            
    def Double_Click(self,tipo,selector,Tiempo=2):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                act=ActionChains(self.driver)
                act.double_click(val).perform()
                print("Dobleclick en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                act=ActionChains(self.driver)
                act.double_click(val).perform()
                print("Dobleclick en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
                
    def Click_Derecho(self,tipo,selector,Tiempo=.9):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                act=ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClickDerecho en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                act=ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClicDerecho en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)   
                
    def Mouse_DragDrop(self,tipo,selector,destino,Tiempo=.9):
        if tipo=="xpath":
            try:
                val=self.sex(selector)
                val2=self.sex(destino)
                act=ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Se solto el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                val=self.SEI(selector)
                val2=self.SEI(destino)
                act=ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("ClicDerecho en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)          
   
    def Mouse_DragDropXY(self,tipo,selector,x,y,Tiempo=.9):
        if tipo=="xpath":
            try:
                self.driver.switch_to.frame(0)
                val=self.sex(selector)
                act=ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("Se solto el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                self.driver.switch_to.frame(0)
                val=self.SEI(selector)
                act=ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("ClicDerecho en el elemento: {} ".format(selector))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)         
    
    def ClickXY(self,tipo,selector,x,y,Tiempo=1.5):
        if tipo=="xpath":
            try:
               # self.driver.switch_to.frame(0)
                val=self.sex(selector)
                act=ActionChains(self.driver)
                act.move_to_element_with_offset(val,x,y).click().perform()
                print("Click en el elemento: {} coordenada {},{}".format(selector,x,y))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)
        elif tipo=="id":
            try:
                self.driver.switch_to.frame(0)
                val=self.SEI(selector)
                act=ActionChains(self.driver)
                act.move_to_element_with_offset(val,x,y).click().perform()
                print("Click en el elemento: {} coordanda {},{}".format(selector,x,y))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se pudo encontrar el elemento",selector)         
        
         
         
       
