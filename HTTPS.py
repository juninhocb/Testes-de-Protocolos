from tkinter import *
from tkinter import ttk
from tkinter import Menu
import requests
import json
from tkinter import messagebox
'''
estadoac1 = requests.post(url='http://localhost:4001/estado', json = "ac1")
    aux = estadoac1.json()
'''
f = ("verdana", 8)
stats = ""
r = ""


def enviar(end, metd, inp, out):
    
    metodo = metd.get()
    endereco = end.get()
    mensagem = inp.get("1.0", END)
    mensagemModel = ""
    global r
    global stats
    
    if metodo == "GET - TEXT":
        
        try:
            r = requests.get (url = endereco, data = mensagem)
            if r.status_code == 200:
                messagebox.showinfo (title = "Aviso", message = "Requisição enviada com sucesso!")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
            elif r.status_code == 405:
                messagebox.info(title = "Aviso", message = "Erro --Server not allowed-- Método não permitido ")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            else:
                messagebox.info(title = "Aviso", message = "Requisição sem sucesso, verifique o código do erro")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
            
        except:
            messagebox.showerror(title = "Aviso", message = "Não foi possível fazer a requisição, verifique o código de erro")
            out.config (state = "normal")
            out.insert(INSERT, r.status_code)
            out.config (state = "disable")
    
    elif metodo == "POST - TEXT":
        
        try:
            r = requests.post (url = endereco, data = mensagem)
            if r.status_code == 200:
                messagebox.showinfo (title = "Aviso", message = "Requisição enviada com sucesso!")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.insert(INSERT, r.json())
                out.config (state = "disable")
            
            elif r.status_code == 405:
                messagebox.info(title = "Aviso", message = "Erro --Server not allowed-- Método não permitido ")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            else:
                messagebox.info(title = "Aviso", message = "Requisição sem sucesso, verifique o código do erro")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
            
        except:
            messagebox.showerror(title = "Aviso", message = "Não foi possível fazer a requisição, verifique o código de erros")
            out.config (state = "normal")
            out.delete("1.0", END)
            out.insert(INSERT, r.status_code)
            out.config (state = "disable")
    
    elif metodo == "GET - JSON":
        
        mensagemModel = json.loads(mensagem)
        
        try: 
            r = requests.get (url = endereco, json = mensagemModel)
            if r.status_code == 200:
                messagebox.showinfo (title = "Aviso", message = "Requisição enviada com sucesso!")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
            elif r.status_code == 405:
                messagebox.info(title = "Aviso", message = "Erro --Server not allowed-- Método não permitido ")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            else:
                messagebox.info(title = "Aviso", message = "Requisição sem sucesso, verifique o código do erro")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
        except:
            messagebox.showerror(title = "Aviso", message = "Não foi possível fazer a requisição, verifique o código de erros")
            out.config (state = "normal")
            out.delete("1.0", END)
            out.insert(INSERT, r.status_code)
            out.config (state = "disable")
        
    elif metodo == "POST - JSON":
        
        mensagemModel = json.loads(mensagem)
        
        try: 
            r = requests.post (url = endereco, json = mensagemModel)
            if r.status_code == 200:
                messagebox.showinfo (title = "Aviso", message = "Requisição enviada com sucesso!")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.insert(INSERT, r.json())
                out.config (state = "disable")
            
            elif r.status_code == 405:
                messagebox.info(title = "Aviso", message = "Erro --Server not allowed-- Método não permitido ")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            else:
                messagebox.info(title = "Aviso", message = "Requisição sem sucesso, verifique o código do erro")
                out.config (state = "normal")
                out.delete("1.0", END)
                out.insert(INSERT, r.status_code)
                out.config (state = "disable")
            
        except:
            messagebox.showerror(title = "Aviso", message = "Não foi possível fazer a requisição")
            out.config (state = "normal")
            out.delete("1.0", END)
            out.insert(INSERT, r.status_code)
            out.config (state = "disable")
    else:
        
        messagebox.showerror(title = "Aviso", message = "Selecione uma requisição válida!!!")
    


def HTTPS(root, key):
    
    frm1 = Frame(root)
    label1 = Label (frm1, text = "Protocolo HTTPS", font = ("verdana", 12, 'bold'))
    label2 = Label (frm1, text = "Endereço", font = f)
    entry1 = Entry (frm1, font = f)
    comboE = ttk.Combobox (frm1, values = ["GET - TEXT", "POST - TEXT", "GET - JSON", "POST - JSON"])
    label3 = Label (frm1, text = "Input", font = f)
    text1 = Text (frm1)
    label4 = Label (frm1, text = "Output", font = f)
    text2 = Text (frm1, state = "disable")
    btnEnv = Button (frm1, text = "Enviar", command = lambda: enviar(entry1, comboE, text1, text2))
    
    if key == False:
        
        frm1.place (relx = 0.05, rely = 0.05, relwidth = 0.95, relheight = 0.95)
        
        label1.place (relx = 0.325, rely = 0.025, relwidth = 0.35, relheight = 0.07)
            
        label2.place (relx = 0.05, rely = 0.15, relwidth = 0.1, relheight = 0.07)
    
        entry1.insert (0, "exemplo: http://127.0.0.1:4000/teste")
        entry1.place (relx = 0.17, rely = 0.15, relwidth = 0.6, relheight = 0.07)
        
        comboE.set("Selecione")
        comboE.place (relx = 0.79, rely = 0.15, relwidth = 0.2, relheight = 0.07)
        
        label3.place (relx = 0.04, rely = 0.45, relwidth = 0.1, relheight = 0.07)
       
        text1.place (relx = 0.17, rely = 0.25, relwidth = 0.52, relheight = 0.5)
    
        label4.place (relx = 0.69, rely = 0.45, relwidth = 0.1, relheight = 0.07)
        
        text2.place (relx = 0.79, rely = 0.25, relwidth = 0.2, relheight = 0.5)
    
        btnEnv.place (relx = 0.4, rely = 0.8, relwidth = 0.2, relheight = 0.15)
    
    else:
        
        frm1.place_forget()
        label1.place_forget()
        label2.place_forget()
        label3.place_forget()
        label4.place_forget()
        text1.place_forget()
        text2.place_forget()
        entry1.place_forget()
        comboE.place_forget()
        btnEnv.place_forget()
    
        
    
    
    
    
    