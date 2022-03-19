from tkinter import *



class Calculator:
    def __init__(self, janela):
        self.buttons = Frame(janela)
        self.buttons.pack()

        ##Number buttons

        self.button1 = Button(self.buttons, text='1', font='Arial')
        self.button1.grid(column=0, row=3, padx=5, pady=5)

        self.button2 = Button(self.buttons, text='2', font='Arial')
        self.button2.grid(column=1, row=3, padx=5, pady=5)

        self.button3 = Button(self.buttons, text='3', font='Arial')
        self.button3.grid(column=2, row=3, padx=5, pady=5)

        self.button4 = Button(self.buttons, text='4', font='Arial')
        self.button4.grid(column=0, row=2, padx=5, pady=5)

        self.button5 = Button(self.buttons, text='5', font='Arial')
        self.button5.grid(column=1, row=2, padx=5, pady=5)

        self.button6 = Button(self.buttons, text='6', font='Arial')
        self.button6.grid(column=2, row=2, padx=5, pady=5)

        self.button7 = Button(self.buttons, text='7', font='Arial')
        self.button7.grid(column=0, row=1, padx=5, pady=5)

        self.button8 = Button(self.buttons, text='8', font='Arial')
        self.button8.grid(column=1, row=1, padx=5, pady=5)

        self.button9 = Button(self.buttons, text='9', font='Arial')
        self.button9.grid(column=2, row=1, padx=5, pady=5)

        self.button0 = Button(self.buttons, text='0', font='Arial')
        self.button0.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky=EW)

        ##Operation buttons

        self.buttoncomma = Button(self.buttons, text=',', font='Arial')
        self.buttoncomma.grid(column=2, row=4, padx=5, pady=5)

        self.buttonequal = Button(self.buttons, text='=', font='Arial')
        self.buttonequal.grid(column=3, row=3, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonplus = Button(self.buttons, text='+', font='Arial')
        self.buttonplus.grid(column=3, row=1, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonminus = Button(self.buttons, text='-', font='Arial')
        self.buttonminus.grid(column=3, row=0, padx=5, pady=5)

        self.buttonmultiplication = Button(self.buttons, text='*', font='Arial')
        self.buttonmultiplication.grid(column=2, row=0, padx=5, pady=5)

        self.buttondivision = Button(self.buttons, text='/', font='Arial')
        self.buttondivision.grid(column=1, row=0, padx=5, pady=5)

        self.buttonclear = Button(self.buttons, text='C', font='Arial')
        self.buttonclear.grid(column=0, row=0, padx=5, pady=5)


root = Tk()

Calculator(root)

root.mainloop()
