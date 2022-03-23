from cgitb import text
from tkinter import *
from tkinter import font


class Calculator:
    def __init__(self, janela):
        
        janela.title('Calculator 5000')
        janela.resizable(False, False)
        janela.attributes('-toolwindow', True)

        self.default_font = font.Font(family='Consolas', weight='bold')

        self.display = Text(janela, width=13, height=2, font=self.default_font)
        self.display.tag_configure('justify-configuration', justify='right')
        self.display.insert('0.0', '00')
        self.display.tag_add('justify-configuration', '0.0')
        self.display.grid(column=0, row=0, columnspan=4)

        ##Number buttons

        self.button1 = Button(janela, text='1', font=self.default_font, command=self.b1)
        self.button1.grid(column=0, row=4, padx=5, pady=5)

        self.button2 = Button(janela, text='2', font=self.default_font, command=self.b2)
        self.button2.grid(column=1, row=4, padx=5, pady=5)

        self.button3 = Button(janela, text='3', font=self.default_font, command=self.b3)
        self.button3.grid(column=2, row=4, padx=5, pady=5)

        self.button4 = Button(janela, text='4', font=self.default_font, command=self.b4)
        self.button4.grid(column=0, row=3, padx=5, pady=5)

        self.button5 = Button(janela, text='5', font=self.default_font, command=self.b5)
        self.button5.grid(column=1, row=3, padx=5, pady=5)

        self.button6 = Button(janela, text='6', font=self.default_font, command=self.b6)
        self.button6.grid(column=2, row=3, padx=5, pady=5)

        self.button7 = Button(janela, text='7', font=self.default_font, command=self.b7)
        self.button7.grid(column=0, row=2, padx=5, pady=5)

        self.button8 = Button(janela, text='8', font=self.default_font, command=self.b8)
        self.button8.grid(column=1, row=2, padx=5, pady=5)

        self.button9 = Button(janela, text='9', font=self.default_font, command=self.b9)
        self.button9.grid(column=2, row=2, padx=5, pady=5)

        self.button0 = Button(janela, text='0', font=self.default_font, command=self.b0)
        self.button0.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky=EW)

        ##Operation buttons

        self.buttoncomma = Button(janela, text=',', font=self.default_font, command=self.b_comma)
        self.buttoncomma.grid(column=2, row=5, padx=5, pady=5)

        self.buttonequal = Button(janela, text='=', font=self.default_font, command=self.b_equal)
        self.buttonequal.grid(column=3, row=4, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonplus = Button(janela, text='+', font=self.default_font, command=self.b_plus)
        self.buttonplus.grid(column=3, row=2, rowspan=2, padx=5, pady=5, sticky=NS)

        self.buttonminus = Button(janela, text='-', font=self.default_font, command=self.b_minus)
        self.buttonminus.grid(column=3, row=1, padx=5, pady=5)

        self.buttonmultiplication = Button(janela, text='*', font=self.default_font, command=self.b_multiplication)
        self.buttonmultiplication.grid(column=2, row=1, padx=5, pady=5)

        self.buttondivision = Button(janela, text='/', font=self.default_font, command=self.b_division)
        self.buttondivision.grid(column=1, row=1, padx=5, pady=5)

        self.buttonclear = Button(janela, text='C', font=self.default_font, command=self.clear_display)
        self.buttonclear.grid(column=0, row=1, padx=5, pady=5)

    def b1(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '1')
            self.display.tag_add('justify-configuration', '0.0')

    def b2(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '2')
            self.display.tag_add('justify-configuration', '0.0')
    
    def b3(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '3')
            self.display.tag_add('justify-configuration', '0.0')

    def b4(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '4')
            self.display.tag_add('justify-configuration', '0.0')

    def b5(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '5')
            self.display.tag_add('justify-configuration', '0.0')

    def b6(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '6')
            self.display.tag_add('justify-configuration', '0.0')

    def b7(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '7')
            self.display.tag_add('justify-configuration', '0.0')

    def b8(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '8')
            self.display.tag_add('justify-configuration', '0.0')

    def b9(self):
        if self.full_line_verification():
            self.empty_verification()
            self.display.insert(END, '9')
            self.display.tag_add('justify-configuration', '0.0')

    def b0(self):
        if self.full_line_verification():
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
            self.status_comma = True
            for j in reversed(self.display.get("1.0", "end-1c")):
                if j == ',':
                    self.status_comma = False
                    break

                elif j in ['*', '/', '+', '-']:
                    break

            if self.status_comma:
                self.display.insert(END, ',')
                self.display.tag_add('justify-configuration', '0.0')
                self.status_comma = True

    def empty_verification(self):
        print(f'{self.display.get("1.0", "end-1c")}')
        if self.display.get("1.0", "end-1c") == '00':
            self.display.delete(1.0, END)
    
    def full_line_verification(self):
        if len(self.display.get("1.0", "end-1c")) < 13:
            return True
    
    def b_equal(self):

        self.result = self.display.get("1.0", "end-1c").replace(',', '.')
        if self.result[-1] in ['*', '/', '+', '-']:
            self.result = self.result[:-1]

        try:    
            eval(self.result)
        except ZeroDivisionError:
            print('ZeroDivision')
        else:
            self.result = self.display.get("1.0", "end-1c").replace(',', '.')    
            if self.result[-1] in ['*', '/', '+', '-']:
                self.result = self.result[:-1]
            
            print(f'Result = {self.result}')
            self.display.insert(END, '\n=' + f'{eval(self.result):.2f}'.replace('.', ','))
            self.display.tag_add('justify-configuration', '0.0', 'end')

    def clear_display(self):
        self.display.delete(1.0, END)
        self.display.insert(END, '00')
        self.display.tag_add('justify-configuration', '0.0')

if __name__ == '__main__':

    root = Tk()

    Calculator(root)

    root.mainloop()
