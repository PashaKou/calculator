from tkinter import *


def button_press(x):
    global equation_text
    equation_text += str(x)

    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax error")
    except ZeroDivisionError:
        equation_label.set("Error")


def delete_one():
    global equation_text
    try:
        list_char = []
        for elem in equation_text:
            list_char += [elem]
        list_char.pop()
        char = ""
        for elem in list_char:
            char += elem
        equation_text = char
        equation_label.set(equation_text)
    except IndexError:
        equation_label.set("Error")


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


def change():
    global equation_text
    try:
        list_char = []
        for elem in equation_text:
            list_char += [elem]
        for i in range(len(list_char)):
            if list_char[i] == "+" or list_char[i] == "-":
                if list_char[i] == "-":
                    list_char[i] = "+"
                else:
                    list_char[i] = "-"
        char = ""
        for elem in list_char:
            char += elem
        equation_text = char
        equation_label.set(equation_text)
    except IndexError:
        equation_label.set("Error")


# window control -------------------------------------------------------------------------
window = Tk()
window.title("Calculator")
window.geometry("270x360")
window.resizable(False,False)

#  label control --------------------------------------------------------------------------
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, width=24, height=2, font=("Consolas", 30), bg="light yellow")
label.pack()

# buttons ------------------------------------------------------------------
frame = Frame(window)
frame.pack()
button1 = Button(frame, text=1, height=2, width=6, font=30, command=lambda: button_press(1))
button1.grid(row=3, column=0)
button2 = Button(frame, text=2, height=2, width=6, font=30, command=lambda: button_press(2))
button2.grid(row=3, column=1)
button3 = Button(frame, text=3, height=2, width=6, font=30, command=lambda: button_press(3))
button3.grid(row=3, column=2)
button4 = Button(frame, text=4, height=2, width=6, font=30, command=lambda: button_press(4))
button4.grid(row=2, column=0)
button5 = Button(frame, text=5, height=2, width=6, font=30, command=lambda: button_press(5))
button5.grid(row=2, column=1)
button6 = Button(frame, text=6, height=2, width=6, font=30, command=lambda: button_press(6))
button6.grid(row=2, column=2)
button7 = Button(frame, text=7, height=2, width=6, font=30, command=lambda: button_press(7))
button7.grid(row=1, column=0)
button8 = Button(frame, text=8, height=2, width=6, font=30, command=lambda: button_press(8))
button8.grid(row=1, column=1)
button9 = Button(frame, text=9, height=2, width=6, font=30, command=lambda: button_press(9))
button9.grid(row=1, column=2)
button0 = Button(frame, text=0, height=2, width=6, font=30, command=lambda: button_press(0))
button0.grid(row=4, column=1)

# other buttons ------------------------------------------------------
button_dot = Button(frame, text=".", height=2, width=6, font=30, command=lambda: button_press("."))
button_dot.grid(row=4, column=0)

button_equal = Button(frame, text="=", height=2, width=6, font=30, command=equals, bg="orange")
button_equal.grid(row=4, column=2)

button_plus = Button(frame, text="+", height=2, width=6, font=30, command=lambda: button_press("+"))
button_plus.grid(row=4, column=3)

button_sub = Button(frame, text="-", height=2, width=6, font=30, command=lambda: button_press("-"))
button_sub.grid(row=3, column=3)

button_multi = Button(frame, text="*", height=2, width=6, font=30, command=lambda: button_press("*"))
button_multi.grid(row=2, column=3)

button_div = Button(frame, text="/", height=2, width=6, font=30, command=lambda: button_press("/"))
button_div.grid(row=1, column=3)

button_del = Button(frame, text="<=", height=2, width=6, font=30, command=delete_one)
button_del.grid(row=0, column=2)

button_del = Button(frame, text="EXIT", height=2, width=6, font=30, command=quit)
button_del.grid(row=0, column=3)

button_del = Button(frame, text="+/-", height=2, width=6, font=30, command=change)
button_del.grid(row=0, column=0)

button_dell_all = Button(frame, text="C", height=2, width=6, font=30, command=clear, bg="#56c5f5")
button_dell_all.grid(row=0, column=1)

menu_bar = Menu(window)
window.config(menu=menu_bar)


def dark():
    global button1, button0, button7, button8, button9, button2, button3, button4, button6, button5, button_del, \
        button_dell_all, button_div, button_multi, button_plus, button_dot, button_sub
    label.config(background="#030787", foreground="white")
    button1 = Button(frame, text=1, height=2, width=6, font=30, command=lambda: button_press(1), bg="black",
                     fg="white")
    button1.grid(row=3, column=0)
    button2 = Button(frame, text=2, height=2, width=6, font=30, command=lambda: button_press(2), bg="black",
                     fg="white")
    button2.grid(row=3, column=1)
    button3 = Button(frame, text=3, height=2, width=6, font=30, command=lambda: button_press(3), bg="black",
                     fg="white")
    button3.grid(row=3, column=2)
    button4 = Button(frame, text=4, height=2, width=6, font=30, command=lambda: button_press(4), bg="black",
                     fg="white")
    button4.grid(row=2, column=0)
    button5 = Button(frame, text=5, height=2, width=6, font=30, command=lambda: button_press(5), bg="black",
                     fg="white")
    button5.grid(row=2, column=1)
    button6 = Button(frame, text=6, height=2, width=6, font=30, command=lambda: button_press(6), bg="black",
                     fg="white")
    button6.grid(row=2, column=2)
    button7 = Button(frame, text=7, height=2, width=6, font=30, command=lambda: button_press(7), bg="black",
                     fg="white")
    button7.grid(row=1, column=0)
    button8 = Button(frame, text=8, height=2, width=6, font=30, command=lambda: button_press(8), bg="black",
                     fg="white")
    button8.grid(row=1, column=1)
    button9 = Button(frame, text=9, height=2, width=6, font=30, command=lambda: button_press(9), bg="black",
                     fg="white")
    button9.grid(row=1, column=2)
    button0 = Button(frame, text=0, height=2, width=6, font=30, command=lambda: button_press(0), bg="black",
                     fg="white")
    button0.grid(row=4, column=1)

    button_dot = Button(frame, text=".", height=2, width=6, font=30, command=lambda: button_press("."), bg="black",
                        fg="white")
    button_dot.grid(row=4, column=0)

    button_plus = Button(frame, text="+", height=2, width=6, font=30, command=lambda: button_press("+"), bg="black",
                         fg="white")
    button_plus.grid(row=4, column=3)

    button_sub = Button(frame, text="-", height=2, width=6, font=30, command=lambda: button_press("-"), bg="black",
                        fg="white")
    button_sub.grid(row=3, column=3)

    button_multi = Button(frame, text="*", height=2, width=6, font=30, command=lambda: button_press("*"), bg="black",
                          fg="white")
    button_multi.grid(row=2, column=3)

    button_div = Button(frame, text="/", height=2, width=6, font=30, command=lambda: button_press("/"), bg="black",
                        fg="white")
    button_div.grid(row=1, column=3)

    button_del = Button(frame, text="<=", height=2, width=6, font=30, command=delete_one, bg="black",
                        fg="white")
    button_del.grid(row=0, column=2)

    button_del = Button(frame, text="EXIT", height=2, width=6, font=30, command=quit, bg="black",
                        fg="white")
    button_del.grid(row=0, column=3)

    button_del = Button(frame, text="+/-", height=2, width=6, font=30, command=change, bg="black",
                        fg="white")
    button_del.grid(row=0, column=0)


def light():
    global button1, button0, button7, button8, button9, button2, button3, button4, button6, button5, button_del, \
        button_dell_all, button_div, button_multi, button_plus, button_dot, button_sub
    label.config(background="light yellow", foreground="black")
    button1 = Button(frame, text=1, height=2, width=6, font=30, command=lambda: button_press(1))
    button1.grid(row=3, column=0)
    button2 = Button(frame, text=2, height=2, width=6, font=30, command=lambda: button_press(2))
    button2.grid(row=3, column=1)
    button3 = Button(frame, text=3, height=2, width=6, font=30, command=lambda: button_press(3))
    button3.grid(row=3, column=2)
    button4 = Button(frame, text=4, height=2, width=6, font=30, command=lambda: button_press(4))
    button4.grid(row=2, column=0)
    button5 = Button(frame, text=5, height=2, width=6, font=30, command=lambda: button_press(5))
    button5.grid(row=2, column=1)
    button6 = Button(frame, text=6, height=2, width=6, font=30, command=lambda: button_press(6))
    button6.grid(row=2, column=2)
    button7 = Button(frame, text=7, height=2, width=6, font=30, command=lambda: button_press(7))
    button7.grid(row=1, column=0)
    button8 = Button(frame, text=8, height=2, width=6, font=30, command=lambda: button_press(8))
    button8.grid(row=1, column=1)
    button9 = Button(frame, text=9, height=2, width=6, font=30, command=lambda: button_press(9))
    button9.grid(row=1, column=2)
    button0 = Button(frame, text=0, height=2, width=6, font=30, command=lambda: button_press(0))
    button0.grid(row=4, column=1)

    button_dot = Button(frame, text=".", height=2, width=6, font=30, command=lambda: button_press("."))
    button_dot.grid(row=4, column=0)

    button_plus = Button(frame, text="+", height=2, width=6, font=30, command=lambda: button_press("+"))
    button_plus.grid(row=4, column=3)

    button_sub = Button(frame, text="-", height=2, width=6, font=30, command=lambda: button_press("-"))
    button_sub.grid(row=3, column=3)

    button_multi = Button(frame, text="*", height=2, width=6, font=30, command=lambda: button_press("*"))
    button_multi.grid(row=2, column=3)

    button_div = Button(frame, text="/", height=2, width=6, font=30, command=lambda: button_press("/"))
    button_div.grid(row=1, column=3)

    button_del = Button(frame, text="<=", height=2, width=6, font=30, command=delete_one)
    button_del.grid(row=0, column=2)

    button_del = Button(frame, text="EXIT", height=2, width=6, font=30, command=quit)
    button_del.grid(row=0, column=3)

    button_del = Button(frame, text="+/-", height=2, width=6, font=30, command=change)
    button_del.grid(row=0, column=0)


fileMenu = Menu(menu_bar, tearoff=0, font=("MV Boli", 10))
menu_bar.add_cascade(label="Theme", menu=fileMenu)
fileMenu.add_command(label="Dark", command=dark)
fileMenu.add_command(label="Light", command=light)

window.mainloop()
