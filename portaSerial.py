import serial
from tkinter import filedialog as dlg
import re
from pprint import pprint
from tkinter import * 
import asyncio
from time import sleep
import serial.tools.list_ports


class app():
    def __init__(self):
        self.path =dlg.askopenfilename()
        with open(f'{self.path}') as f:
            self.tudo = f.read()
        self.comandos=(re.findall('(>.*<)', self.tudo))
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.function_asyc())
        self.loop.close()

    async def function_asyc(self):
        ports = serial.tools.list_ports.comports()
        for p in ports:
            print(p.device)
            ser = serial.Serial(f'{p.device}', 19200)
            for i in range(len(self.comandos)):
                self.linha = str.encode(self.comandos[i])
                ser.write(self.linha)
                sleep(0.02)
            s = ser.readline()
            s1 = s.decode()
            id=re.findall(';ID=....;',s1)
            pprint(s1)
            print(id)

app()



