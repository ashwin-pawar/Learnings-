import tkinter as tk
from time import strftime # we can modify time and date according to needs

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H: %M:%S %p \n %D') # define Hour,Minutes,Seconds And Date
    label.config(text=string)
    label.after(1000,time)  #after each 1 seconds our time will change 

label = tk.Label(root, font=('calibri' , 50 , 'bold'), background= 'yellow' ,  foreground='red') # you can change font,size,background and foreground color
label.pack( anchor='center')

time()    # time fucntion excute and it will show time and date 

root.mainloop()
