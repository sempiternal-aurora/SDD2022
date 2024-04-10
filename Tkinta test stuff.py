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
        answer_label = tk.Label(self, textvariable = self.answer)
        answer_label.grid(row = 1, column = 4)

    def change_operator(self):
        current_op = self.operator.get()
        if current_op == "+": self.operator.set("-")
        elif current_op == "-": self.operator.set("x")
        elif current_op == "x": self.operator.set("÷")
        elif current_op == "÷": self.operator.set("^")
        elif current_op == "^": self.operator.set("+")

    def calc_answer(self):
        answer = 0
        operators = {"+":"+", "-":"-", "x":"*", "÷":"/", "^":"**"}
        current_op = operators[self.operator.get()]
        n1 = self.number1.get()
        n2 = self.number2.get()
        try:
            answer = eval(n1 + current_op + n2)
            self.answer.set(answer)
        except:
            self.answer.set("?")

class Page_Three(tk.Frame): #my gif
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        self.image_frames = self.load_image()
        self.image_index = 0

        label = tk.Label(self, text="Page Three")
        label.pack()

        button_page1 = tk.Button(self, text = "Go to page 1", command = lambda: container.show_frame(Page_One))
        button_page1.pack()

        self.animation = tk.Label(self, image = self.image_frames[self.image_index])
        self.animation.pack()

        self.after(100, self.animate())
    
    def load_image(self):
        target = "image0.gif"
        frames = []
        for i in range(25):
            frame = tk.PhotoImage(file = target, format = "gif -index %i"%(i))
            frames.append(frame)
        return frames

    def animate(self, *args):
        if self.image_index < len(self.image_frames) - 1: self.image_index += 1
        else: self.image_index = 0
        next_image = self.image_frames[self.image_index]
        self.animation.configure(image = next_image)
        self.after(100, self.animate)

my_app = App_Window("SDD 2021", "600x600")
my_app.mainloop()