import tkinter as tk

class App_Window(tk.Tk):
    def __init__(self, name, size):
        tk.Tk.__init__(self) #Make a Tk GUI window object as a part of this object
        self.title(name)
        self.geometry(size)
        main_window_frame = tk.Frame(self) #Define and make a frame object in this window object
        main_window_frame.pack()        #Pack the frame to be visible in the window

        self.frames = {}
        for f in (Page_One, Page_Two, Page_Three):
            frame = f(main_window_frame, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        self.show_frame(Page_One)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class Page_One(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack()

        button_page2 = tk.Button(self, text = "Go to page 2", command = lambda: container.show_frame(Page_Two))
        button_page2.pack()
        button_page3 = tk.Button(self, text = "Go to page 3", command = lambda: container.show_frame(Page_Three))
        button_page3.pack()


class Page_Two(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        self.number1 = tk.StringVar()
        self.number2 = tk.StringVar()
        self.operator = tk.StringVar()
        self.answer = tk.StringVar()
        self.operator.set("+")

        label = tk.Label(self, text="Page Two")
        label.grid(row = 0, column = 2)

        button_page1 = tk.Button(self, text = "Home", command = lambda: container.show_frame(Page_One))
        button_page1.grid(row = 2, column = 2)

        number_entry1 = tk.Entry(self, textvariable = self.number1)
        number_entry1.grid(row = 1, column = 0)
        number_entry2 = tk.Entry(self, textvariable = self.number2)
        number_entry2.grid(row = 1, column = 2)
        
        operator_button = tk.Button(self, textvariable = self.operator, command = lambda: self.change_operator())
        operator_button.grid(row = 1, column = 1)
        equals_button = tk.Button(self, text = "=", command = lambda: self.calc_answer())
        equals_button.grid(row = 1, column = 3)
        answer_entry = tk.Entry(self, textvariable = self.answer)
        answer_entry.grid(row = 1, column = 4)

    def change_operator(self):
        if self.operator.get() == "+":
            self.operator.set("-")
        elif self.operator.get() == "-":
            self.operator.set("x")
        elif self.operator.get() == "x":
            self.operator.set("÷")
        elif self.operator.get() == "÷":
            self.operator.set("^")
        elif self.operator.get() == "^":
            self.operator.set("+")

    def calc_answer(self):
        n1 = float(self.number1.get())
        n2 = float(self.number2.get())
        if self.operator.get() == "+":
            self.answer.set(str(n1 + n2))
        elif self.operator.get() == "-":
            self.answer.set(str(n1 - n2))
        elif self.operator.get() == "x":
            self.answer.set(str(n1 * n2))
        elif self.operator.get() == "÷":
            self.answer.set(str(n1 / n2))
        elif self.operator.get() == "^":
            self.answer.set(str(n1 ** n2))

class Page_Three(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page Three")
        label.pack()

        button_page1 = tk.Button(self, text = "Go to page 1", command = lambda: container.show_frame(Page_One))
        button_page1.pack()

my_app = App_Window("SDD 2021", "600x600")
my_app.mainloop()