from gpiozero import CPUTemperature
import psutil
from tkinter import Label, Tk, LabelFrame
import os
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
    label_temp.configure(text=str(var.temp)+' C')
    label_percent.configure(text=str(var.cpu_percent)+' %')
    label_freq.configure(text=str(var.cpu_freq)+' MHz')
    label_mem.configure(text=str(var.mem)+' Gb')
    label_disk.configure(text=str(var.disq)+' Gb')
    fen.after(1000, refresh)
    

reso = os.popen("xrandr -q -d :0").readlines()[0]
width = reso.split()[7]
height = reso.split()[9][:-1]
haut = str(225)
lar = str(150)
print(width, height)
if width == '1920' and height == '1080':
    width_place = str(round(int(width)/29.5))
    height_place = str(round(int(height)*1.635))
    empla = lar+'x'+haut+'+'+height_place+'+'+width_place
if width == '1280' and height == '1024':
    width_place = str(round(int(width)/20))
    height_place = str(round(int(height)*1.1))
    empla = lar+'x'+haut+'+'+height_place+'+'+width_place
if width == '1440' and height == '900':
    width_place = str(round(int(width)/22))
    height_place = str(round(int(height)*1.4275))
    empla = lar+'x'+haut+'+'+height_place+'+'+width_place
if width == '800' and height == '600':
    width_place = str(round(int(width)/12.5))
    height_place = str(round(int(height)*1.075))
    empla = lar+'x'+haut+'+'+height_place+'+'+width_place
if width == '640' and height == '480':
    width_place = str(round(int(width)/10))
    height_place = str(round(int(height)*1.01))
    empla = lar+'x'+haut+'+'+height_place+'+'+width_place

    
#'150x225+,1760+40'
fen = Tk()
fen.title('Info System')
fen.geometry(empla)

fram_temp = LabelFrame(fen, text='Temperature CPU')
label_temp = Label(fram_temp, text=str(var.temp)+' C')

fram_percent = LabelFrame(fen, text='Utilisation CPU')
label_percent = Label(fram_percent, text=str(var.cpu_percent)+' %')

fram_freq = LabelFrame(fen, text='Frequence CPU')
label_freq = Label(fram_freq, text=str(var.cpu_freq)+' MHz')

fram_mem = LabelFrame(fen, text='Memoires Disponible')
label_mem = Label(fram_mem, text=str(var.mem)+' Gb')

fram_disk = LabelFrame(fen, text='HDD Disponible')
label_disk = Label(fram_disk, text=str(var.disq)+' Gb')

fram_temp.pack(fill="both")
label_temp.pack()

fram_percent.pack(fill="both")
label_percent.pack()

fram_freq.pack(fill="both")
label_freq.pack()

fram_mem.pack(fill="both")
label_mem.pack()

fram_disk.pack(fill="both")
label_disk.pack()

refresh()
fen.mainloop()

    


    
    
   
    
    
  






    


