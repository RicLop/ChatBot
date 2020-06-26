import os
import time
import re
import requests
import json
from selenium import webdriver

class whatsapp:
    def __init__(self):
        self.chrome = os.getcwd() + "/drivers/chromedriver"
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-data-dir="+os.getcwd()+"/profile")
        
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def inicia(self, contato):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(contato))
        self.contato.click()
        time.sleep(5)
        
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3uMse')
        self.caixa_de_mensagem.send_keys("Iara iniciada. ja pode conversar comigo :)")
        time.sleep(1)
        
        self.botao_enviar = self.driver.find_element_by_class_name('_1U1xa')
        self.botao_enviar.click()
        time.sleep(1)

    def escuta(self):
        post = self.driver.find_elements_by_class_name('_274yw:not(_1qPwk)')
        ultimo = len(post) - 1
        texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto    
    
    def escrever(self, resposta):
        self.caixa_de_mensagem.send_keys(resposta)
        time.sleep(2)
        self.botao_enviar = self.driver.find_element_by_class_name('_1U1xa')
        self.botao_enviar.click()        
        time.sleep(2)