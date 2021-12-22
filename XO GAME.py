from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("XO GAME")

lbl = Label(window,text="Player1:X",font=("Helvetiica",15),fg="blue")
lbl.grid(row = 0, column = 0)

            
lbl2 = Label(window,text="Player2:O",font=("Helvetiica",15),fg="blue")
lbl2.grid(row = 1, column = 0)

btn = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn.grid(row = 0, column = 1)

btn2 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn2.grid(row = 0, column = 2)

btn3 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn3.grid(row = 0, column = 3)

btn4 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn4.grid(row = 1, column = 1)

btn5 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn5.grid(row = 1, column = 2)

btn6 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn6.grid(row = 1, column = 3)

btn7 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn7.grid(row = 2, column = 1)

btn8 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn8.grid(row = 2, column = 2)

btn9 = Button(window,text="",bg = "red", width = 6, height = 1,font=("Helvetiica",15))
btn9.grid(row = 2, column = 3)

            
