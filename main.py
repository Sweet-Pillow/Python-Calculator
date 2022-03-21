from tkinter import *


class Calculator:
    def __init__(self, janela):
        
        janela.title('Calculator 5000')


        self.display = Text(janela, width=13, height=2, font='Arial')
        self.display.tag_configure('justify-configuration', justify='right')
        self.display.insert('0.0', '00')
        self.display.tag_add('justify-configuration', '0.0')
        self.display.grid(column=0, row=0, columnspan=4)

        ##Number buttons

        self.button1 = Button(janela, text='1', font='Arial', command=self.b1)
        self.button1.grid(column=0, row=4, padx=5, pady=5)

        self.button2 = Button(janela, text='2', font='Arial', command=self.b2)
        self.button2.grid(column=1, row=4, padx=5, pady=5)

        self.button3 = Button(janela, text='3', font='Arial', command=self.b3)
        self.button3.grid(column=2, row=4, padx=5, pady=5)

        self.button4 = Button(janela, text='4', font='Arial', command=self.b4)
        self.button4.grid(column=0, row=3, padx=5, pady=5)

        self.button5 = Button(janela, text='5', font='Arial', command=self.b5)
        self.button5.grid(column=1, row=3, padx=5, pady=5)

        self.button6 = Button(janela, text='6', font='Arial', command=self.b6)
        self.button6.grid(column=2, row=3, padx=5, pady=5)

        self.button7 = Button(janela, text='7', font='Arial', command=self.b7)
        self.button7.grid(column=0, row=2, padx=5, pady=5)

        self.button8 = Button(janela, text='8', font='Arial', command=self.b8)
        self.button8.grid(column=1, row=2, padx=5, pady=5)

        self.button9 = Button(janela, text='9', font='Arial', command=self.b9)
        self.button9.grid(column=2, row=2, padx=5, pady=5)

        self.button0 = Button(janela, text='0', font='Arial', command=self.b0)
        self.button0.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky=EW)

        ##Operation buttons

        self.buttoncomma = Button(janela, text=',', font='Arial', command=self.b_comma)
        self.buttoncomma.grid(column=2, row=5, padx=5, pady=5)

        self.buttonequal = Button(janela, text='=', font='Arial')
        self.buttonequal.grid(column=3, row=4, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonplus = Button(janela, text='+', font='Arial', command=self.b_plus)
        self.buttonplus.grid(column=3, row=2, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonminus = Button(janela, text='-', font='Arial', command=self.b_minus)
        self.buttonminus.grid(column=3, row=1, padx=5, pady=5)

        self.buttonmultiplication = Button(janela, text='*', font='Arial', command=self.b_multiplication)
        self.buttonmultiplication.grid(column=2, row=1, padx=5, pady=5)

        self.buttondivision = Button(janela, text='/', font='Arial', command=self.b_division)
        self.buttondivision.grid(column=1, row=1, padx=5, pady=5)

        self.buttonclear = Button(janela, text='C', font='Arial', command=self.clear_display)
        self.buttonclear.grid(column=0, row=1, padx=5, pady=5)

    def b1(self):
        self.empty_verification()
        self.display.insert(END, '1')
        self.display.tag_add('justify-configuration', '0.0')

    def b2(self):
        self.empty_verification()
        self.display.insert(END, '2')
        self.display.tag_add('justify-configuration', '0.0')
    
    def b3(self):
        self.empty_verification()
        self.display.insert(END, '3')
        self.display.tag_add('justify-configuration', '0.0')

    def b4(self):
        self.empty_verification()
        self.display.insert(END, '4')
        self.display.tag_add('justify-configuration', '0.0')

    def b5(self):
        self.empty_verification()
        self.display.insert(END, '5')
        self.display.tag_add('justify-configuration', '0.0')

    def b6(self):
        self.empty_verification()
        self.display.insert(END, '6')
        self.display.tag_add('justify-configuration', '0.0')

    def b7(self):
        self.empty_verification()
        self.display.insert(END, '7')
        self.display.tag_add('justify-configuration', '0.0')

    def b8(self):
        self.empty_verification()
        self.display.insert(END, '8')
        self.display.tag_add('justify-configuration', '0.0')

    def b9(self):
        self.empty_verification()
        self.display.insert(END, '9')
        self.display.tag_add('justify-configuration', '0.0')

    def b0(self):
        self.empty_verification()
        self.display.insert(END, '0')
        self.display.tag_add('justify-configuration', '0.0')

    def b_multiplication(self):
        if self.display.get("1.0", "end-1c") != '00' and self.display.get("1.0", "end-1c")[-1] != '*' and self.display.get("1.0", "end-1c")[-1] not in ['+','-','/',',']:
            self.display.insert(END, '*')
            self.display.tag_add('justify-configuration', '0.0')
    
    def b_plus(self):
        if self.display.get("1.0", "end-1c") != '00' and self.display.get("1.0", "end-1c")[-1] != '+' and self.display.get("1.0", "end-1c")[-1] not in ['*','-','/',',']:
            self.display.insert(END, '+')
            self.display.tag_add('justify-configuration', '0.0')
    
    def b_minus(self):
        if self.display.get("1.0", "end-1c") != '00' and self.display.get("1.0", "end-1c")[-1] != '-' and self.display.get("1.0", "end-1c")[-1] not in ['+','*','/',',']:
            self.display.insert(END, '-')
            self.display.tag_add('justify-configuration', '0.0')
    
    def b_division(self):
        if self.display.get("1.0", "end-1c") != '00' and self.display.get("1.0", "end-1c")[-1] != '/' and self.display.get("1.0", "end-1c")[-1] not in ['+','-','*',',']:
            self.display.insert(END, '/')
            self.display.tag_add('justify-configuration', '0.0')
    
    def b_comma(self):
        if self.display.get("1.0", "end-1c") != '00' and self.display.get("1.0", "end-1c")[-1] != ',' and self.display.get("1.0", "end-1c")[-1].isnumeric():
            self.display.insert(END, ',')
            self.display.tag_add('justify-configuration', '0.0')

    def empty_verification(self):
        print(f'{self.display.get("1.0", "end-1c")}')
        if self.display.get("1.0", "end-1c") == '00':
            self.display.delete(1.0, END)

    def clear_display(self):
        self.display.delete(1.0, END)
        self.display.insert(END, '00')
        self.display.tag_add('justify-configuration', '0.0')

if __name__ == '__main__':

    root = Tk()

    Calculator(root)

    root.mainloop()
