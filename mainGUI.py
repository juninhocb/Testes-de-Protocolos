from tkinter import *
from tkinter import ttk
from MQTT import MQTT
from HTTPS import HTTPS
from tkinter import messagebox

def showMain(root):
    
    key = False
    
    frm1 = Frame(root)
    frm1.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)
    
    labelPrincipal = Label(frm1, text = "Escolha um protocolo de comunicação", font = ("verdana", 12, "bold"))
    labelPrincipal.place (relx = 0.15, rely = 0.05, relwidth = 0.785, relheight = 0.10)
    
    btnMQTT = Button(frm1, text = "MQTT", font = ("verdana", 15, "bold"), bg = "#E6E6FA", command = lambda: MQTT(root, key))
    btnMQTT.place (relx = 0.1, rely = 0.2, width = 200, height = 200)
    
    btnHTTPS = Button(frm1, text = "HTTPS", font = ("verdana", 15, "bold"), bg = "#E0FFFF", command = lambda: HTTPS(root, key))
    btnHTTPS.place (relx= 0.55, rely = 0.2, width = 200, height = 200)
    