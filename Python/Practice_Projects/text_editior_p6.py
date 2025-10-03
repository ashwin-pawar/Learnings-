# PROJECT NO 6 GUI BASED TEXT EDITOR APP
 
import tkinter as tk
from tkinter import filedialog,messagebox #to show file and message box

def new_file():
    text.delete(1.0,tk.END) # delete all previous file and text 

def open_file():
    file_path =filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text File" , "*.txt")])
    if file_path:
        with open(file_path, 'r') as file: #r - read mode initally read mode
            text.delete(1.0, tk.END)      # delete all data or text inside file 
            text.insert(tk.END,file.read())  #insert tect till end and read file 

def save_file(): #fn
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files" , "*.txt")])
    if file_path:
        with open(file_path, 'w') as file: #Open file in write mode 
            file.write(text.get(1.0 ,tk.END))  #open file in write mode and get text till end 
            messagebox.showinfo("INFO" , "File Saved Successfully 🫡")

root = tk.Tk()
root.title("My Notepad..😉")
root.geometry("800x600") #*


menu =tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label = "File" , menu=file_menu) #cascade ky krta hai aur gpt se puchna padega 

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save" , command=save_file)
file_menu.add_separator #idk kis kam ata hai dekh na padega
file_menu.add_command(label="Exit" , command=root.quit)  #exit 

#Text widget and customizing text and other things
text = tk.Text(root , wrap=tk.WORD , font=("Helvetica", 15), fg="black")
text.pack(expand=tk.YES, fill=tk.BOTH)    


root.mainloop()
