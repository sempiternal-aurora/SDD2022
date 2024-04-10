import tkinter as tk

window = tk.Tk()
data_grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

#I like button
def click_my_button(text, r, c):
    print("The button was clicked")
    text.set(":)")

stringvar_grid = []
button_grid = []

for i in range(0,10):
    my_button_text = tk.StringVar()
    my_button_text.set("gay")

    my_button = tk.Button(window, textvariable=my_button_text, command=lambda: click_my_button(my_button_text, 1, 0))
    button_grid.append(my_button)
    my_button.pack()

window.mainloop()