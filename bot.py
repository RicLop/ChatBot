from datetime import datetime
from difflib import SequenceMatcher
import getpass
import unicodedata
import time
import os
import re

class rdbot:    
    def __init__(self):
        self.nome_bot = "Iara"
        self.usuario = getpass.getuser()
        self.caminho = os.getcwd() + "/database/cerebro.txt"         
        
    def ler(self, texto):   
        texto = self.remover_acentos(texto)
        resposta = self.entender_texto(texto)
        if (resposta != ""):
            return(resposta) #print(self.nome_bot + ": " + resposta)
        else:
            return("Não sei como responder isso desculpe")
            #resposta = input(self.usuario + ": ")
            #self.escrever(texto + ">" + resposta + ".")               

    def remover_acentos(self, texto):
        texto = texto.lower()
        
        if "?" in texto:
            texto = texto.replace('?', '')
        
        if "iara" in texto:
            texto = texto.replace("iara", '')
            
        nfkd_form = unicodedata.normalize('NFKD', texto)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def entender_texto(self, texto):
        resposta = ""
        with open(self.caminho, "r+") as f:
            lines = [re.sub(r'^.*?{0}'.format(self.usuario+": "), '', line.rstrip()) for line in f] 
            for line in lines:             
                if self.comparar_textos(texto.lower(), line.lower().split(">")[0]):
                    resposta = line.split(">")[1]         
                
        return(resposta)   

    def comparar_textos(self, texto, texto_no_arquivo):
        porcentagem_semelhanca = SequenceMatcher(None, texto, texto_no_arquivo).ratio()  
        return (porcentagem_semelhanca >= 0.6)            

    #def escrever(self, texto):      
    #    with open(self.caminho, "a+") as f:       
    #        f.writelines("\n" + texto)     
