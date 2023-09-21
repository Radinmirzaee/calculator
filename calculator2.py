from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
    except ZeroDivisionError:
        equation_label.set("Can't devide by zero")
        equation_text = ""
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def clears():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window,width=24,height=4,textvariable=equation_label)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,height=4,width=9,text=1,command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,height=4,width=9,text=2,command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,height=4,width=9,text=3,command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,height=4,width=9,text=4,command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,height=4,width=9,text=5,command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,height=4,width=9,text=6,command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,height=4,width=9,text=7,command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,height=4,width=9,text=8,command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,height=4,width=9,text=9,command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,height=4,width=9,text=0,command=lambda: button_press(0))
button0.grid(row=3,column=0)

decimal = Button(frame,height=4,width=9,text=".",command=lambda: button_press("."))
decimal.grid(row=3,column=1)

equals = Button(frame,height=4,width=9,text="=",command=equal)
equals.grid(row=3,column=2)

plus = Button(frame,height=4,width=9,text="+",command=lambda: button_press("+"))
plus.grid(row=0,column=3)

minus = Button(frame,height=4,width=9,text="-",command=lambda: button_press("-"))
minus.grid(row=1,column=3)

multiply = Button(frame,height=4,width=9,text="*",command=lambda: button_press("*"))
multiply.grid(row=2,column=3)

divide = Button(frame,height=4,width=9,text="/",command=lambda: button_press("/"))
divide.grid(row=3,column=3)

clear = Button(window,height=4,width=9,text="clear",command=clears)
clear.pack()



window.mainloop()