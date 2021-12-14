from gpiozero import CPUTemperature
import psutil
from tkinter import Label, Frame, Tk, LabelFrame


class Variables:
    def __init__(self):
        self.temp = 0
        self.cpu_percent = 0
        self.cpu_freq = 0
        self.mem = 0
        self.disq = 0
        
var = Variables()

def temp():
    
    tempe = CPUTemperature(min_temp=0, max_temp=100)
    var.temp =  str(format(round(tempe.temperature)))
    
def usa() :
    
    var.cpu_percent = psutil.cpu_percent()
      
def freq():
    var.cpu_freq = psutil.cpu_freq(percpu=False)
    var.cpu_freq = var.cpu_freq.current

def memo():
    memoi = psutil.virtual_memory()
    var.mem = round(memoi.free / 1000000000, 2)
    
def disk():
    disqu = psutil.disk_usage('/')
    var.disq = round(disqu.free / 1000000000, 2)
    
def refresh():
    temp()
    usa()
    freq()
    memo()
    disk()
    label_temp.configure(text=var.temp+' C')
    label_percent.configure(text=str(var.cpu_percent)+' %')
    label_freq.configure(text=str(var.cpu_freq)+' MHz')
    label_mem.configure(text=str(var.mem)+' Gb')
    label_disk.configure(text=str(var.disq)+' Gb')
    fen.after(1000, refresh)
    

    

fen = Tk()
fen.title('Info System')
fen.geometry('150x225+1760+40')

fram_temp = LabelFrame(fen, text='Temperature CPU')
label_temp = Label(fram_temp, text=str(var.temp)+' C')

fram_percent = LabelFrame(fen, text='Utilisation CPU')
label_percent = Label(fram_percent, text=str(var.cpu_percent)+' %')

fram_freq = LabelFrame(fen, text='Frequence CPU')
label_freq = Label(fram_freq, text=str(var.cpu_freq)+' MHz')

fram_mem = LabelFrame(fen, text='Memoires Dispo')
label_mem = Label(fram_mem, text=str(var.mem)+' Gb')

fram_disk = LabelFrame(fen, text='HDD Disponible')
label_disk = Label(fram_disk, text=str(var.disq)+' Gb')

fram_temp.pack()
label_temp.pack()

fram_percent.pack()
label_percent.pack()

fram_freq.pack()
label_freq.pack()

fram_mem.pack()
label_mem.pack()

fram_disk.pack()
label_disk.pack()
refresh()
fen.mainloop()

    


    
    
   
    
    
  






    

