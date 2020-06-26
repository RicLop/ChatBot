from bot import rdbot
from whatsapp import whatsapp
import getpass
import os

meubot = rdbot()
whats = whatsapp()
whats.inicia("Rodrigo")
texto = "Iara iniciada. ja pode conversar comigo :)"
ultima_resposta = "Iara iniciada. ja pode conversar comigo :)"
ultimo_texto = "0"

while True:   
    texto = whats.escuta() 
    if texto != ultimo_texto and texto != ultima_resposta:   
        resposta = meubot.ler(texto)
        whats.escrever(resposta)
        ultima_resposta = resposta
        ultimo_texto = texto     