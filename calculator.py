from tkinter import *

# globally define the expression variable
expression = ''

# function to update expression value
# in the text entry box

def press(num):
    global expression      # point out global expression variable
    expression += str(num)    # concatenation of string
    equation.set(expression)    # update the expression variable by set method

# function for final expression

def equal_press():
    # try and except statement is used for holding the errors like zero and division error
    try:
        global expression
        # eval function evaluate the expression and set function convert the result in string
        total = str(eval(expression))
        equation.set(total)

        # initialize the value of expression variable by empty string
        expression = ''

    # if error occur than handle by the except expression
    except:
        equation.set("error")
        expression = ''

# function for clear the value of text entry box

def clear():
    global expression
    expression = ''
    equation.set('')

# driver code

if __name__ == '__main__':
    # create gui window
    gui = Tk()    # initialize tkinter
    gui.configure(background='light green')   # set the gui config
    gui.title("simple calculator")  # set the title
    equation = StringVar()  # set the type of variable

    # create the text entry box for showing expression
    expression_feild = Entry(gui, textvariable=equation)
    expression_feild.grid(columnspan=4, ipadx=100)

    equation.set("Enter your expression")

    # entry number buttons
    btn0 = Button(gui, text="1", fg="black", command=lambda: press(1), height='1', width='7').grid(row=2, column=0)
    btn1 = Button(gui, text="2", fg="black", command=lambda: press(2), height='1', width='7').grid(row=2, column=1)
    btn2 = Button(gui, text="3", fg="black", command=lambda: press(3), height='1', width='7').grid(row=2, column=2)
    btn3 = Button(gui, text="4", fg="black", command=lambda: press(4), height='1', width='7').grid(row=3, column=0)
    btn4 = Button(gui, text="5", fg="black", command=lambda: press(5), height='1', width='7').grid(row=3, column=1)
    btn5 = Button(gui, text="6", fg="black", command=lambda: press(6), height='1', width='7').grid(row=3, column=2)
    btn6 = Button(gui, text="7", fg="black", command=lambda: press(7), height='1', width='7').grid(row=4, column=0)
    btn7 = Button(gui, text="8", fg="black", command=lambda: press(8), height='1', width='7').grid(row=4, column=1)
    btn8 = Button(gui, text="9", fg="black", command=lambda: press(9), height='1', width='7').grid(row=4, column=2)
    btn9 = Button(gui, text="0", fg="black", command=lambda: press(0), height='1', width='7').grid(row=5, column=0)

    # expression buttons
    plus = Button(gui, text="+", fg="black", command=lambda: press('+'), height='1', width='7').grid(row=2, column=3)
    minus = Button(gui, text="-", fg="black", command=lambda: press('-'), height='1', width='7').grid(row=3, column=3)
    mul = Button(gui, text="*", fg="black", command=lambda: press('*'), height='1', width='7').grid(row=4, column=3)
    div = Button(gui, text="/", fg="black", command=lambda: press('/'), height='1', width='7').grid(row=5, column=3)

    # for execute expressions
    equal = Button(gui, text="=", fg="black", command=equal_press, height='1', width='7').grid(row=5, column=2)
    cls = Button(gui, text="C", fg="black", command=clear, height='1', width='7').grid(row=5, column=1)

    gui.mainloop()





