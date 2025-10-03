# PROJECT NO 6 GUI BASED TEXT EDITOR APP
 
import tkinter as tk
from tkinter import filedialog,messagebox #to show file and message box

def new_file():
    text.delete(1.0,tk.END) # delete all previous text 

def open_file():
    file_path =filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text File" , "*.txt")])
    if file_path:
        with open(file_path, 'r') as file: #r - read only mode
            text.delete(1.0, tk.END)     
            text.insert(tk.END,file.read())  #insert text till end and read file 

def save_file(): #fn
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files" , "*.txt")])
    if file_path:
        with open(file_path, 'w') as file: #Open file in write mode 
            file.write(text.get(1.0 ,tk.END)) 
            messagebox.showinfo("INFO" , "File Saved Successfully 🫡")

root = tk.Tk()
root.title("My Notepad..😉")
root.geometry("800x600") #*

menu =tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label = "File" , menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save" , command=save_file)
file_menu.add_separator
file_menu.add_command(label="Exit" , command=root.quit)  #exit 

text = tk.Text(root , wrap=tk.WORD , font=("Helvetica", 15), fg="black")
text.pack(expand=tk.YES, fill=tk.BOTH)    


root.mainloop()


# NOTE:- 
# Learnings :- I used to know how Tkinter Module is used and how it works also i learn about filedialog,messagebox and other fucntions and their use.

# I'm Doing all these program to learn more about how can i not just learn python but actually i can take hands on practies and some confidence on myself.

# and Also im starting learning AI so that i can do more work in lesser time to make work faster and efficient 
# also after some day i will start doing DSA in python so that i can explore more in this indurtry (IT).

# Thanks for reading and you can checkout my other projects too. 

