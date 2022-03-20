from tkinter import *


class Calculator:
    def __init__(self, janela):
        
        janela.title('Calculator 5000')


        self.display = Text(janela, width=13, height=2, font='Arial')
        self.display.tag_configure('justify-configuration', justify='right')
        self.display.insert(END, '00')
        self.display.tag_add('justify-configuration', '1.0')
        self.display.grid(column=0, row=0, columnspan=4)

        ##Number janela

        self.button1 = Button(janela, text='1', font='Arial')
        self.button1.grid(column=0, row=4, padx=5, pady=5)

        self.button2 = Button(janela, text='2', font='Arial')
        self.button2.grid(column=1, row=4, padx=5, pady=5)

        self.button3 = Button(janela, text='3', font='Arial')
        self.button3.grid(column=2, row=4, padx=5, pady=5)

        self.button4 = Button(janela, text='4', font='Arial')
        self.button4.grid(column=0, row=3, padx=5, pady=5)

        self.button5 = Button(janela, text='5', font='Arial')
        self.button5.grid(column=1, row=3, padx=5, pady=5)

        self.button6 = Button(janela, text='6', font='Arial')
        self.button6.grid(column=2, row=3, padx=5, pady=5)

        self.button7 = Button(janela, text='7', font='Arial')
        self.button7.grid(column=0, row=2, padx=5, pady=5)

        self.button8 = Button(janela, text='8', font='Arial')
        self.button8.grid(column=1, row=2, padx=5, pady=5)

        self.button9 = Button(janela, text='9', font='Arial')
        self.button9.grid(column=2, row=2, padx=5, pady=5)

        self.button0 = Button(janela, text='0', font='Arial')
        self.button0.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky=EW)

        ##Operation janela

        self.buttoncomma = Button(janela, text=',', font='Arial')
        self.buttoncomma.grid(column=2, row=5, padx=5, pady=5)

        self.buttonequal = Button(janela, text='=', font='Arial')
        self.buttonequal.grid(column=3, row=4, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonplus = Button(janela, text='+', font='Arial')
        self.buttonplus.grid(column=3, row=2, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonminus = Button(janela, text='-', font='Arial')
        self.buttonminus.grid(column=3, row=1, padx=5, pady=5)

        self.buttonmultiplication = Button(janela, text='*', font='Arial')
        self.buttonmultiplication.grid(column=2, row=1, padx=5, pady=5)

        self.buttondivision = Button(janela, text='/', font='Arial')
        self.buttondivision.grid(column=1, row=1, padx=5, pady=5)

        self.buttonclear = Button(janela, text='C', font='Arial')
        self.buttonclear.grid(column=0, row=1, padx=5, pady=5)


if __name__ == '__main__':

    root = Tk()

    Calculator(root)

    root.mainloop()
