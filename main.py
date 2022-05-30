from tkinter import *
from tkinter import ttk
from tkinter import Menu
from chamaMenu import *
from mainGUI import *
from tkinter import messagebox

#configurações da tela inicial
root = Tk()
root.iconbitmap("D:\Desktop\jr\Python\Tkinter\MQTT_Post_V2\images\mainIcon.ico")
root.geometry("600x300")
root.resizable(False, False)
root.title("Teste de comunicação")
    

class Main():
    
    def __init__(self):
        
        criaMenu(root)
        showMain(root)
        root.mainloop()


Main()

    
    
