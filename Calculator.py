from tkinter import *

class calc:
    def __init__(self, a):
        a.title("Calculator")
        a.geometry("360x420")
        a.configure(bg="gray")
        a.resizable(False, False)

        self.equation = StringVar()
        self.e_value = ""

        Entry(a, width=17, bg='lightgrey',
              font=("Arial Bold", 28),
              textvariable=self.equation).place(x=0, y=0)

        # Row 1
        Button(a, text="(", width=10, height=3, command=lambda:self.show('(')).place(x=0,y=60)
        Button(a, text=")", width=10, height=3, command=lambda:self.show(')')).place(x=90,y=60)
        Button(a, text="%", width=10, height=3, command=lambda:self.show('%')).place(x=180,y=60)
        Button(a, text="/", width=10, height=3, command=lambda:self.show('/')).place(x=270,y=60)

        # Row 2
        Button(a, text="7", width=10, height=3, command=lambda:self.show(7)).place(x=0,y=120)
        Button(a, text="8", width=10, height=3, command=lambda:self.show(8)).place(x=90,y=120)
        Button(a, text="9", width=10, height=3, command=lambda:self.show(9)).place(x=180,y=120)
        Button(a, text="*", width=10, height=3, command=lambda:self.show('*')).place(x=270,y=120)

        # Row 3
        Button(a, text="4", width=10, height=3, command=lambda:self.show(4)).place(x=0,y=180)
        Button(a, text="5", width=10, height=3, command=lambda:self.show(5)).place(x=90,y=180)
        Button(a, text="6", width=10, height=3, command=lambda:self.show(6)).place(x=180,y=180)
        Button(a, text="-", width=10, height=3, command=lambda:self.show('-')).place(x=270,y=180)

        # Row 4
        Button(a, text="1", width=10, height=3, command=lambda:self.show(1)).place(x=0,y=240)
        Button(a, text="2", width=10, height=3, command=lambda:self.show(2)).place(x=90,y=240)
        Button(a, text="3", width=10, height=3, command=lambda:self.show(3)).place(x=180,y=240)
        Button(a, text="+", width=10, height=3, command=lambda:self.show('+')).place(x=270,y=240)

        # Row 5
        Button(a, text="C", width=10, height=3, command=self.clear).place(x=0,y=300)
        Button(a, text="0", width=10, height=3, command=lambda:self.show(0)).place(x=90,y=300)
        Button(a, text=".", width=10, height=3, command=lambda:self.show('.')).place(x=180,y=300)
        Button(a, text="=", width=10, height=3, command=self.solve).place(x=270,y=300)

    def show(self, value):
        self.e_value += str(value)
        self.equation.set(self.e_value)

    def clear(self):
        self.e_value = ""
        self.equation.set("")

    def solve(self):
        try:
            result = eval(self.e_value)
            self.equation.set(result)
            self.e_value = str(result)
        except:
            self.equation.set("Error")
            self.e_value = ""

root = Tk()
calculator = calc(root)
root.mainloop()
