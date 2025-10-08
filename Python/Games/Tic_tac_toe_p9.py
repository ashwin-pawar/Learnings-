import tkinter as tk
from tkinter import messagebox

def Check_winner():
    for combo in [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:  #possible combination
     if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons [combo[2]]["text"]!="":
        buttons[combo[0]].config(bg ="green")
        buttons[combo[1]].config(bg ="green")
        buttons[combo[2]].config(bg ="green")
        messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]["text"]} Win 🎉")
        winner = True
        root.after(500,reset_board)
        return

def button_click(index):
   global current_player
   if buttons[index]["text"] == "" and not winner:
      buttons[index]["text"] = current_player
      Check_winner()
      if not winner:
        toggle_player() #next user pe shift ho jayega 

def toggle_player():
   global current_player
   current_player  = "X" if current_player == "O" else "O"
   label.config(text=f"Player {current_player}'s Turn ")

def reset_board():
    global winner, current_player
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    winner = False
    current_player = "X"
    label.config(text=f"Player {current_player}'s Turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width = 6, height = 2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i % 3)

current_player = "X"
winner = False  # variable will check either game is ongoing or end 
label = tk.Label(root, text =f"Player {current_player}'s Turn" , font = ("normal", 16))

label.grid(row=3, column =0, columnspan=3) #it will create grid into 3*3 

root.mainloop()