from tkinter import *
from tkinter import ttk
from tkinter import Menu
from MQTT import MQTT
from HTTPS import HTTPS
from tkinter import messagebox

keyH = False
keyM = False


## funções
def ajuda(root):
    textoAjuda = "Programa criado com o intuito de testar a conexão com o servidor pelos protocolos MQTT e HTTPS, o usuário poderá escolher no menu qual protocolo quer utilizar e preencher os campos para realização dos testes."
    
    window = Toplevel(root)
    window.geometry("300x200")
    window.resizable(False, False)
    window.grab_set()
    window.title("Ajuda")
    
    frm2 = Frame(window)
    frm2.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight  = 0.95)
    
    labelAjuda = Label(frm2, text = "Informações", font = ("verdana", 10, "bold"))
    labelAjuda.place (relx = 0.31, rely = 0.05)
    
    textAjuda = Text(frm2, font = ("verdana", 8) )
    textAjuda.place(relx= 0.07, rely = 0.2, width = 250, height = 100)
    textAjuda.insert("1.0", textoAjuda)
    
    
    btnVoltar = Button(frm2, text = "voltar", command = window.destroy)
    btnVoltar.place (relx = 0.375, rely = 0.775, width = 50, height = 25)


def abreMQTT(root):

    messagebox.showinfo(title = "Aviso", message = "As configurações serão resetadas!")
    global keyH
    global keyM
    keyH = True
    keyM = False
    HTTPS(root, keyH)
    MQTT(root, keyM)

def abreHTTPS(root):

    messagebox.showinfo(title = "Aviso", message = "As configurações serão resetadas!")
    global keyM
    global keyH
    keyM = True
    keyH = False
    MQTT(root, keyM)
    HTTPS(root, keyH)
    
def criaMenu(root):
    
    #criando menus
    menubar = Menu(root)
    root.config(menu = menubar)
    
    #menus
    protocolos_menu = Menu(menubar, tearoff = False)
    protocolos_menu.add_command(
        label = "MQTT",
        command = lambda: abreMQTT(root)
        )

    protocolos_menu.add_command(
        label = "HTTPS",
        command = lambda: abreHTTPS(root)
        )

    menubar.add_cascade(
        label="Protocolos",
        menu=protocolos_menu
    )

    help_menu = Menu(menubar, tearoff = False)
    help_menu.add_command(
        label = "Ajuda",
        command = lambda: ajuda(root)
    
        )
    menubar.add_cascade(
        label="Ajuda",
        menu=help_menu
    )


    exit_menu = Menu(menubar, tearoff = False)
    exit_menu.add_command(
        label = "Sair",
        command = root.destroy
    
        )

    menubar.add_cascade(
        label="Sair",
        menu=exit_menu
    )
