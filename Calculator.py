from tkinter import *

#DESKTOP>>>>
desktop = Tk()
desktop.title("CALCULATOR")
desktop.geometry("550x580+100+200")
desktop.resizable(False, False)
desktop.config(bg="#454448")

#LABEL>>>>
label_result = Label(desktop, text="", height=2, width=25, font=("times", 30, "bold"), background="red")
label_result.pack()

#BUTTONS>>>>
Button(desktop, text="C", height=1, width=5, bd=1, bg="red", fg="black", font=("times", 30, "bold"),
       command=lambda: clear()).place(x=10, y=100)
Button(desktop, text="/", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("/")).place(x=150, y=100)
Button(desktop, text="%", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("%")).place(x=290, y=100)
Button(desktop, text="*", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("*")).place(x=430, y=100)

Button(desktop, text="7", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("7")).place(x=10, y=200)
Button(desktop, text="8", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("8")).place(x=150, y=200)
Button(desktop, text="9", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("9")).place(x=290, y=200)
Button(desktop, text="-", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("-")).place(x=430, y=200)

Button(desktop, text="4", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("4")).place(x=10, y=300)
Button(desktop, text="5", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("5")).place(x=150, y=300)
Button(desktop, text="6", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("6")).place(x=290, y=300)
Button(desktop, text="+", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("+")).place(x=430, y=300)

Button(desktop, text="1", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("1")).place(x=10, y=400)
Button(desktop, text="2", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("2")).place(x=150, y=400)
Button(desktop, text="3", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("3")).place(x=290, y=400)
Button(desktop, text="0", height=1, width=11, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show("0")).place(x=10, y=500)

Button(desktop, text=".", height=1, width=5, bd=1, bg="#2a2d36", fg="white", font=("times", 30, "bold"),
       command=lambda: show(".")).place(x=290, y=500)
Button(desktop, text="=", height=4, width=5, bd=1, bg="yellow", fg="black", font=("times", 30, "bold"),
       command=lambda: calculate()).place(x=430, y=400)

#FUNCTION>>>>
equation = ""


def show(value):
    global equation
    equation = equation + value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        result = eval(equation)
    else:
        result = "ERROR"
        equation = ""
    label_result.config(text=result)


desktop.mainloop()
