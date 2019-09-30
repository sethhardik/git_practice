


from tkinter import *



# def hello():
#     a = ent.get()
#     strVar.set(a)
#
#
# root = Tk()
#
# strVar = StringVar()
# strVar.set('Coding')
# label = Label(root, textvariable=strVar)
# label.pack()
#
# btn = Button(root, text="Click Me", command=hello)
# btn.pack()
#
# ent = Entry(root)
# ent.pack()
#
# root.mainloop()



window = Tk()

def click(btnVal):
    a = strVar.get()
    if btnVal == 'C':
        a = ''
    elif btnVal == '=':
        a = eval(a)
    else:
        a = a + str(btnVal)
    strVar.set(a)

strVar = StringVar()
strVar.set("")
label = Label(window, textvariable=strVar)
label.grid(row=0, column=0, columnspan=3)

clearBtn = Button(window, text="C",
                  width=5, height=2,
                  command=lambda:click('C'))
clearBtn.grid(row=0, column=3)

btn7 = Button(window, text="7",
              width=5, height=2,
              command=lambda:click(7))
btn7.grid(row=1, column=0)

btn8 = Button(window, text="8",
              width=5, height=2,
              command=lambda:click(8))
btn8.grid(row=1, column=1)

btn9 = Button(window, text="9",
              width=5, height=2,
              command=lambda:click(9))
btn9.grid(row=1, column=2)

btnDiv = Button(window, text="/", width=5, height=2, command=lambda:click('/'))
btnDiv.grid(row=1, column=3)

btn4 = Button(window, text="4", width=5, height=2, command=lambda:click(4))
btn4.grid(row=2, column=0)

btn5 = Button(window, text="5", width=5, height=2, command=lambda:click(5))
btn5.grid(row=2, column=1)

btn6 = Button(window, text="6", width=5, height=2, command=lambda:click(6))
btn6.grid(row=2, column=2)

btnPlus = Button(window, text="+", width=5, height=2, command=lambda:click('+'))
btnPlus.grid(row=2, column=3)

btnEqual = Button(window, text="=", width=5, height=2, command=lambda:click('='))
btnEqual.grid(row=3, column=3)

window.mainloop()






















