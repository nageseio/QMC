from tkinter import *
from tkinter import messagebox
from qmc import quine_mccluskey
import tkinter.messagebox
 
def message():
	messagebox.showinfo("Truth Table: Input", "The function that is minimized can be entered via a truth table that represents the function S = f(xn,...,x1, x0).")
	
def copy():
	main.clipboard_clear()
	main.clipboard_append(eText.get())
	
def show_answer():
    Ans = quine_mccluskey.main(num1.get().split())
    eText.set(Ans)

main = Tk()

main.title("Quine-McCluskey algorithm")

menubar = Menu(main)
menubar.add_command(label="Helper", command=message)

# display the menu
main.config(menu=menubar)

Label(main, text="Truth table(S):").grid(row=0)
Label(main, text="Boolean expression:").grid(row=1, pady= 15)

eText = tkinter.StringVar()
num1 = Entry(main)
num2 = Entry(main, textvariable = eText)

num1.grid(row=0,column=1)
num2.grid(row=1,column=1)

Button(main,text='Generate',command=show_answer).grid(row=0,column=2,sticky=W,pady=5)
Button(main,text='copy',command=copy).grid(row=1,column=2,sticky=W,pady=5)

mainloop()
