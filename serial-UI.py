from cProfile import label
from ctypes import sizeof
from turtle import width
import serial
from tkinter import filedialog as dlg
import re
from pprint import pprint
from tkinter import * 
import asyncio
from time import sleep

master = Tk() 
master.geometry("200x150")
master.configure(background="#dde") 


class app():
    def __init__(self):
        self.label=Label(master, text= 'ESCOLHER ARQUIVO', background="#dde")
        self.label.pack(pady=10)
        self.bttn=Button(master, text='Escolher',command=self.dir)
        self.bttn.pack(pady = 20)



    def dir(self):
        self.path =dlg.askopenfilename()
        with open(f'{self.path}') as f:
            self.tudo = f.read()
        self.comandos=(re.findall('(>.*<)', self.tudo))        
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.function_asyc())
        self.loop.close()
        self.OpenWindow()

    def OpenWindow(self):
        self.newWindow = Toplevel(master) 
        self.newWindow.title("New Window") 
        self.newWindow.geometry("220x300")
        self.newWindow.configure(background="#dde") 
        Label(self.newWindow, text ="IDS CONFIGURADOS!!",background="#dde", foreground="#009", anchor=W).pack()
        Label(self.newWindow, text=f'{self.id1}',background="#dde", foreground="#009").pack()
        Label(self.newWindow, text=f'{self.id2}',background="#dde", foreground="#009").pack()

    async def function_asyc(self):
        ser = serial.Serial('COM13', 19200)
        ser2 = serial.Serial('COM9', 19200)	
        for i in range(len(self.comandos)):
            self.linha = str.encode(self.comandos[i])
            ser.write(self.linha)
            ser2.write(self.linha)
            sleep(0.02)
        s = ser.readline()
        s2 = ser2.readline()
        s1 = s.decode()
        s3 = s2.decode()
        self.id1=re.findall('ID=....',s1)
        self.id1 = ''.join(self.id1).strip('ID=')
        self.id2=re.findall('ID=....',s3)
        self.id2 = ''.join(self.id2).strip('ID=')
        pprint(s1)
        pprint(s3)
        # pprint(self.StrA)
app()
mainloop()



