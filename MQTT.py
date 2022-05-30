from tkinter import *
from tkinter import ttk
from tkinter import Menu
from HTTPS import HTTPS
import paho.mqtt.client as mqtt
import time
import tkinter as tk
from tkinter import messagebox




f = ("verdana", 8)
Connected = False
cliente = ""
client = ""
btnState = False
subsState = False
listaE = ["Publisher", "Subscriber"]
messageRecive = ""
rcg = 0

#str(message.payload.decode("utf-8")
def on_message(client, userdata, message):
    print ("Message received: "  + str(message.payload.decode("utf-8")))
    print(message.payload)
    global messageRecive
    messageRecive = message.payload.decode("utf-8")
    tk.messagebox.showinfo(title = "Mensagem", message = "Recebida mensagem no topico: " + str(messageRecive))

def listFunc():
    
    if subsState == True:
        tk.messagebox.showinfo (title = "Aviso", message = "Desconecte para parar de ouvir")

def subs(text1, entry, comboE, btnList):
    
    topic = entry.get()
    ce = comboE.get()
    global subsState
        
    if topic != "" and Connected == True and ce == "Subscriber" and subsState == False:
        client.subscribe(topic)
        time.sleep(1)
        tk.messagebox.showinfo (title = "Aviso", message = "Inscrito no tópico " + topic + " com sucesso!")
        text1.delete("1.0", END)
        text1.config (state = "disable")
        comboE.config (state = "disable")
        entry.config (state = "disable")
        subsState = True
        btnList.config(text = "Ouvindo")
        
    elif Connected == False:
        tk.messagebox.showinfo(title = "Aviso", message = "Se conecte ao servidor primeiro")
        entry.delete(0, END)
        
    elif ce != "Subscriber":
        tk.messagebox.showinfo(title = "Aviso", message = "Selecione Subscriber para se inscrever")
        entry.delete(0, END)
    
    elif subsState == True:
        tk.messagebox.showinfo(title = "Aviso", message = "O software está escutando no momento")
    
    else:
        tk.messagebox.showinfo (title = "Aviso", message = "Favor preencher os campos: topic")
        entry.delete(0,END)
       

def enviarD(text, entry, comboE):
    
    textE = text.get("1.0", "end")
    textE2 = text.get("1.0", "end")[0:textE.find("")-1]
    topic = entry.get()
    ce = comboE.get()
    global subsState
        
    if textE2 != "" and topic != "" and Connected == True and ce == "Publisher" and subsState == False:
        client.publish(topic, textE2)
        time.sleep(1)
        tk.messagebox.showinfo (title = "Aviso", message = "Publicado com sucesso!")
        text.delete("1.0", END)
        entry.delete(0, END)
        
    elif Connected == False:
        tk.messagebox.showinfo(title = "Aviso", message = "Se conecte ao servidor primeiro")
        text.delete("1.0", END)
        entry.delete(0, END)
    
    elif subsState == True:
        tk.messagebox.showinfo(title = "Aviso", message = "O software está escutando no momento")
    
    
    elif ce != "Publisher":
        tk.messagebox.showinfo(title = "Aviso", message = "Selecione Publisher para publicar")
        text.delete("1.0", END)
        entry.delete(0, END)
    
    else:
        tk.messagebox.showinfo (title = "Aviso", message = "Favor preencher os campos: topic e texto")
        text.delete("1.0", END)
        entry.delete(0,END)
       

def on_connect(client, userdata, flags, rc):
    
    #função com mutex, ver se consigo depois acrescentar
    #btn.config (text = "conectando...", bg = "grey")
    global rcg
    rcg = rc
      
    if rc == 0:
  
        #print("Connected to broker", rc)
        messagebox.showinfo(title = "aviso", message = "Conecatado com o broker!")  
        global comboE 
        global Connected                #Use global variable
        Connected = True                #Signal connection
  
    else:
  
        print("Connection failed")

def voltarConn (fe1, fe2, fe3, btn):
    
    global btnState
    fe1.config(state = "normal")
    fe2.config(state = "normal")
    fe3.config(state = "normal")
    if btnState == False:
        btn.config(text = "Desconectado", bg= "red")
    fe1.delete(0,END)
    fe2.delete(0,END)
    fe3.delete(0,END)

def chooseConn (fe1, fe2, fe3, btn, comboE, text1, fe4, btnList):
    
    if btnState == False:
        
        conectar(fe1, fe2, fe3, btn, comboE, text1, fe4)
    else:
        
        desconectar (fe1, fe2, fe3, btn, comboE, text1, fe4, btnList)
    
    
    
def desconectar (fe1, fe2, fe3, btn, comboE, text1, fe4, btnList):
    
    global btnState
    global subsState
    subsState = False
    btnState = False
    btnList.config (text = "Normal")
    comboE.config(state = "normal")
    text1.config(state = "normal")
    fe4.config(state = "normal")
    text1.delete("1.0", END)
    comboE.set ("Selecione")
    fe4.delete(0, END)
    btn.config(text = "desconectado", bg = "red")
    client.loop_stop()
    client.disconnect()
    voltarConn (fe1, fe2, fe3, btn)
    
    
    

def conectar (fe1, fe2, fe3, btn, comboE, text1, fe4):
    
    #e1 = nome do broker e2 = nome do cliente e3 = porta
    fe1.config(state= "disabled")
    fe2.config(state= "disabled")
    fe3.config(state= "disabled")
    global cliente
    global client
    global btnState
    e1 = fe1.get()
    e2 = fe2.get()
    e3 = fe3.get()
    ce = comboE
        
    if (e1 == "" or e2 == "" or e3 == ""):
        
        messagebox.showinfo(title = "Ok", message = "Favor, preencher os campos!")    
        voltarConn(fe1, fe2, fe3, btn)
        
    else:
        
        cliente = e2
        client = mqtt.Client(cliente)   #conecta o cliente com o nome do cliente passado por parâmetro
        client.on_connect= on_connect  #disponibiliza a função de callback on_connect, quando retornar resposta do servidor
        client.on_message= on_message 
        try:
            client.connect(e1) #conecta-se ao broker com o endereço passado
            btn.config (text = "conectado", bg = "green")
            text1.config(state = "normal")
            fe4.config(state = "normal")
            comboE.config(state = "normal")
            btnState = True
            time.sleep(4)
            client.loop_start()
            
        except:
            fe1.config(state = "normal")
            fe2.config(state = "normal")
            fe3.config(state = "normal")
            if rcg ==0:
                messagebox.showerror(title = "aviso", message = "Conexão falhou, verifique o endereço do broker")
            else:
                messagebox.showerror (title = "aviso", message = "Falha ao tentar conectar-se com o broker RC: " + str(rcg))
            
        
        
        
            
            
        
def MQTT (root, key):
    
    frm1 = Frame (root)
    label1 = Label (root, text = "Protocolo MQTT", font = ("verdana", 12, 'bold'))
    label2 = Label (root, text = "Broker", font = f)
    entry1 = Entry (root)
    label3 = Label (root, text = "Cliente", font = f)
    entry2 = Entry (root)
    label4 = Label (root, text = "Porta", font = f)
    entry3 = Entry (root)
    btnConn = Button (root, text = "Desconectado", bg = "red",  command = lambda: chooseConn(entry1, entry2, entry3, btnConn, comboE, text1, entry4, btnList))
    label5 = Label(root, text = "Tópico", font = f)
    entry4 = Entry (root, state = "disabled")
    comboE = ttk.Combobox (root, values = listaE, state = "disabled")
    label6 = Label(root, text = "Input", font = f)
    text1 = Text(root, state = "disabled")
    btnEnv = Button(root, text = "Enviar", font = f, command = lambda: enviarD(text1, entry4, comboE))
    btnInsc = Button(root, text = "Inscrever", font = f, command = lambda: subs(text1, entry4, comboE, btnList))
    btnList = Button (root, text = "Normal", command = lambda: listFunc() )
    
    if key == False:
        
        frm1.place (relx = 0.05, rely = 0.05, relwidth = 0.95, relheight = 0.95)
    
        label1.place (relx = 0.325, rely = 0.025, relwidth = 0.35, relheight = 0.07)
    
        label2.place (relx = 0.05, rely = 0.12, relwidth = 0.1, relheight = 0.07)
    
        entry1.place (relx = 0.07, rely = 0.2, relwidth = 0.35, relheight = 0.07)
    
        label3.place (relx = 0.42, rely = 0.12, relwidth = 0.125, relheight = 0.07)
    
        entry2.place (relx = 0.45, rely = 0.2, relwidth = 0.3, relheight = 0.07)
    
        label4.place (relx = 0.74, rely = 0.12, relwidth = 0.125, relheight = 0.07)
    
        entry3.place (relx = 0.78, rely = 0.2, relwidth = 0.1, relheight = 0.07)
    
        btnConn.place (relx = 0.4, rely = 0.3, relwidth = 0.2, relheight = 0.15)
    
        label5.place (relx = 0.22, rely = 0.5, relwidth = 0.2, relheight = 0.07)
    
        entry4.place(relx = 0.36, rely = 0.5, relwidth = 0.2, relheight = 0.07)
    
        comboE.set ("Selecione")
        comboE.place (relx = 0.07, rely = 0.5, relwidth = 0.2, relheight = 0.07)
    
        label6.place (relx = 0.05, rely = 0.63, relwidth = 0.1, relheight = 0.07)
    
        text1.place (relx = 0.15, rely = 0.63, relwidth = 0.75, relheight = 0.07)

        btnEnv.place (relx = 0.575, rely = 0.5, relwidth = 0.15, relheight = 0.07)
    
        btnInsc.place (relx = 0.75, rely = 0.5, relwidth = 0.15, relheight = 0.07)
    
        btnList.place (relx = 0.4, rely = 0.75, relwidth = 0.2, relheight = 0.15)
    
    else:
        
        frm1.place_forget()
        label1.place_forget()
        label2.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        label6.place_forget()
        text1.place_forget()
        entry1.place_forget()
        entry2.place_forget()
        entry3.place_forget()
        entry4.place_forget()
        comboE.place_forget()
        btnEnv.place_forget()
        btnConn.place_forget()
        btnInsc.place_forget()
        btnList.place_forget()
        
    
    
    